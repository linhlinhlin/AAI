"""AAI Lab: analysis on the shipped demo class, local-only HTTP boundary and review storage."""

import json
import threading
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer

import pytest

from misconceptions.lab import analysis, study
from misconceptions.lab.cpack_source import CPackSource
from misconceptions.lab.phrases import condition_phrase
from misconceptions.lab.server import LabService, LocalServer, make_handler, serve
from misconceptions.learning_sandbox import SandboxUnavailable

MAX_ZERO = """#include <stdio.h>
int main(void){int n,a[100];scanf("%d",&n);for(int i=0;i<n;i++)scanf("%d",&a[i]);
int best=0;for(int i=0;i<n;i++){if(a[i]>best)best=a[i];}printf("%d\\n",best);return 0;}
"""


class FixtureSandbox:
    """Answers like a program that starts the maximum at 0; never runs code."""

    def __init__(self, available=True):
        self.available = available

    def health(self):
        return {"ready": self.available, "message": "Synthetic test fixture"}

    def evaluate(self, source, tests):
        if not self.available:
            raise SandboxUnavailable("Docker is not available in this fixture.")
        if "broken" in source:
            return {"verdict": "compile_error", "diagnostics": "main.c:1: error", "tests": [],
                    "passed": 0, "total": len(tests)}
        runs = []
        for test in tests:
            values = [int(x) for x in test["input"].split()][1:]
            output = f"{max([0, *values])}\n"
            runs.append({"test_id": test["test_id"], "output": output, "exit_code": 0, "limit": None,
                         "outcome": "pass" if output == test["expected"] else "fail"})
        passed = sum(r["outcome"] == "pass" for r in runs)
        return {"verdict": "accepted" if passed == len(runs) else "needs_work", "diagnostics": "",
                "tests": runs, "passed": passed, "total": len(runs)}


@pytest.fixture
def service(tmp_path):
    return LabService(tmp_path / "lab", sandbox=FixtureSandbox(), cpack=CPackSource(root=tmp_path))


def by_title(report):
    return {group["title"]: group for group in report["groups"]}


def test_demo_class_groups_carry_evidence_rule_and_hypothesis(service):
    report = service.analysis("class", "max-array", "auto")
    assert report["stats"] == {"students": 10, "failing": 8, "passed": 2}
    groups = by_title(report)
    assert set(groups) == {"Khởi tạo giá trị lớn nhất bằng 0 nên sai với mảng toàn âm",
                           "Bỏ sót phần tử cuối mảng"}
    for group in report["groups"]:
        assert group["hypothesis"]["matched"] == group["size"] == 4
        assert group["rule"]["support"] == group["rule"]["matched"] == 4
        assert len(group["tests"]) == 6 and group["review"]["status"] == "open"
        assert group["members"][0]["id"] == group["representative"]
    initial = groups["Khởi tạo giá trị lớn nhất bằng 0 nên sai với mảng toàn âm"]
    failing = {row["name"] for row in initial["tests"] if row["failing"]}
    assert failing == {"Một phần tử", "Toàn số âm"}
    assert initial["observations"][0]["text"] == "In ra 0 thay vì kết quả"


def test_group_with_different_mechanisms_is_flagged_not_named(service):
    report = service.analysis("class", "sum-range", "auto")
    mixed = [group for group in report["groups"] if group["mixed"]]
    assert len(mixed) == 1 and mixed[0]["hypothesis"] is None
    assert {item["title"] for item in mixed[0]["mixed"]} == {
        "In lại n, chưa tính tổng từ 1 đến n", "Dùng n nhân n thay cho tổng từ 1 đến n",
        "Công thức đang tính tổng đến n−1, thiếu số n"}
    assert mixed[0]["title"].startswith("Đạt “Tổng rỗng” nhưng sai")


def test_swap_mechanisms_are_separated(service):
    titles = set(by_title(service.analysis("class", "swap", "auto")))
    assert titles == {"Hoán vị trên bản sao tham số nên a, b ở main không đổi",
                      "Ghi đè một giá trị trước khi lưu lại nên hai số in ra trùng nhau"}


def test_problem_without_submissions_is_empty(service):
    report = service.analysis("class", "mean-two", "auto")
    assert report["status"] == "empty" and report["groups"] == []
    with pytest.raises(ValueError):
        service.analysis("class", "max-array", "9")
    with pytest.raises(ValueError):
        service.analysis("class", "no-such-problem", "auto")


def test_submission_observations_drop_coincidental_matches(service):
    report = service.analysis("class", "max-array", "auto")
    group = by_title(report)["Khởi tạo giá trị lớn nhất bằng 0 nên sai với mảng toàn âm"]
    detail = service.submission("class", "max-array", group["representative"])
    failing = [t for t in detail["tests"] if t["outcome"] != "pass"]
    assert [t["observations"] for t in failing] == [["In ra 0 thay vì kết quả"]] * 2
    assert detail["hypothesis"]["source"] == "exercise_rule"


def test_verified_run_joins_the_class_once(service):
    result = service.run("max-array", MAX_ZERO)
    assert result["passed"] == 4 and result["hypothesis"]["category"] == "INITIALIZATION"
    with pytest.raises(ValueError):
        service.add_to_class(result["run_id"], "  ")
    added = service.add_to_class(result["run_id"], "Nguyễn An")
    assert added["problem_id"] == "max-array"
    with pytest.raises(ValueError):
        service.add_to_class(result["run_id"], "Nguyễn An")
    report = service.analysis("class", "max-array", "auto")
    assert report["stats"]["students"] == 11
    group = by_title(report)["Khởi tạo giá trị lớn nhất bằng 0 nên sai với mảng toàn âm"]
    assert "Nguyễn An" in {member["author"] for member in group["members"]}
    compile_error = service.run("max-array", "int main( broken")
    assert compile_error["verdict"] == "compile_error" and "run_id" not in compile_error


def test_reviews_follow_the_group_key(service):
    group = service.analysis("class", "max-array", "auto")["groups"][0]
    service.store.save_review("class:max-array", group["key"], "confirmed", "Chữa trên bảng.")
    again = service.analysis("class", "max-array", "3")
    assert next(g for g in again["groups"] if g["key"] == group["key"])["review"]["status"] == "confirmed"
    with pytest.raises(ValueError):
        service.store.save_review("class:max-array", group["key"], "maybe", "")


def test_cpack_without_local_replay_explains_how_to_build_it(service):
    listing = service.problems("cpack")
    assert listing["available"] is False and len(listing["steps"]) == 3
    assert service.problems("class")["available"] is True


def test_conditions_read_as_clauses():
    names = {"t1": "Toàn số âm"}
    assert condition_phrase("test:t1", "fail", names) == "sai test “Toàn số âm”"
    assert condition_phrase("dev:t1:numbers", "zero", names) == "ở test “Toàn số âm”, in ra 0 thay vì kết quả"
    assert condition_phrase("agg:prefix", "empty", names) == "không in gì"
    assert condition_phrase("agg:numbers", "none", names) is None


def test_study_summary_uses_readable_rules():
    summary = study.summary()
    assert [h["id"] for h in summary["hypotheses"]] == ["H1a", "H1b", "H2", "H3", "H4", "H5"]
    assert all(not part.startswith(("agg:", "code:")) for rule in summary["rules"] for part in rule["if"])
    supports = [rule["support"] for rule in summary["rules"]]
    assert supports == sorted(supports, reverse=True)
    assert {row["key"] for row in summary["ari"]["real"]["rows"]} >= {"outcomes", "deviation"}


def test_frozen_rules_stay_loadable():
    assert analysis.frozen_rules()["rules"]


def test_second_start_reuses_the_running_app_instead_of_sharing_the_port(service, capsys):
    holder = {"port": 0}
    server = LocalServer(("127.0.0.1", 0), make_handler(service, holder))
    holder["port"] = port = server.server_address[1]
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        with pytest.raises(OSError):
            LocalServer(("127.0.0.1", port), make_handler(service, holder))
        serve(service, port, open_browser=False)  # Returns at once: the running copy keeps the port.
        assert "already running" in capsys.readouterr().out
    finally:
        server.shutdown()
        server.server_close()
        worker.join(timeout=3)


@pytest.fixture
def client(tmp_path):
    lab = LabService(tmp_path / "lab", sandbox=FixtureSandbox(available=False), cpack=CPackSource(root=tmp_path))
    holder = {"port": 0}
    server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(lab, holder))
    holder["port"] = server.server_address[1]
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    conn = HTTPConnection("127.0.0.1", holder["port"], timeout=10)
    host = f"127.0.0.1:{holder['port']}"

    def request(method, path, body=None, headers=None):
        supplied = {"Host": host} | (headers or {})
        data = body if isinstance(body, bytes) else json.dumps(body).encode() if body is not None else None
        conn.request(method, path, data, supplied)
        response = conn.getresponse()
        return response, response.read()

    yield request, host
    conn.close()
    server.shutdown()
    server.server_close()
    worker.join(timeout=3)


def test_http_serves_the_app_only_to_this_machine(client):
    request, host = client
    response, page = request("GET", "/")
    assert response.status == 200 and b"AAI Lab" in page
    assert "default-src 'self'" in response.getheader("Content-Security-Policy")
    assert request("GET", "/", headers={"Host": "evil.example"})[0].status == 403
    write = {"Content-Type": "application/json", "X-AAI-Lab": "1"}
    review = {"source": "class", "problem": "max-array", "group": "INITIALIZATION:x", "status": "confirmed"}
    assert request("POST", "/api/review", review, {"Content-Type": "application/json"})[0].status == 403
    assert request("POST", "/api/review", review, write | {"Origin": "http://evil.example"})[0].status == 403
    assert request("POST", "/api/review", review, write | {"Origin": f"http://{host}"})[0].status == 200
    assert request("POST", "/api/review", b"{}", write | {"Content-Length": "200000"})[0].status == 400
    response, body = request("POST", "/api/run", {"problem": "max-array", "code": MAX_ZERO}, write)
    assert response.status == 503 and "Docker" in json.loads(body)["error"]
    response, body = request("GET", "/api/analysis?source=class&problem=max-array&k=auto")
    assert response.status == 200 and json.loads(body)["groups"][0]["review"]["status"] in {"open", "confirmed"}
    assert request("GET", "/api/problems?source=cpack")[0].status == 200
    assert request("GET", "/api/nothing")[0].status == 404
