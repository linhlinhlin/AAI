"""Opt-in: authored programs only, never the research corpus (AAI_RUN_DOCKER_TESTS=1)."""

import base64
import os

import pytest

from misconceptions.replay import ReplayPool, image_id

pytestmark = pytest.mark.skipif(os.environ.get("AAI_RUN_DOCKER_TESTS") != "1",
                                reason="requires Docker and the aai-c-replay image")

PROGRAMS = {
    "ok": '#include <stdio.h>\nint main(void){int a,b;scanf("%d %d",&a,&b);printf("%d\\n",a+b);return 0;}\n',
    "compile_error": "int main(void){ return x; }\n",
    "warning": '#include <stdio.h>\nint main(void){int u; printf("%d\\n",1); return 0;}\n',
    "loop": "int main(void){ for(;;){} return 0; }\n",
    "flood": '#include <stdio.h>\nint main(void){ for(;;) printf("aaaaaaaaaaaaaaaa\\n"); return 0; }\n',
    "kill_parent": '#include <signal.h>\n#include <unistd.h>\n#include <stdio.h>\n'
                   'int main(void){ printf("%d %d\\n", kill(getppid(), 9), kill(1, 9)); return 0; }\n',
}


def test_replay_runner_isolates_and_reports_raw_behaviour():
    with ReplayPool(2, image_id()) as pool:
        futures = {name: pool.submit({"id": name, "source": source,
                                      "flags": ["-std=c99", "-Wall"] if name == "kill_parent"
                                      else ["-ansi", "-pedantic", "-Wall", "-Wextra"],
                                      "tests": [{"id": "t0", "input": "2 3\n"}]})
                   for name, source in PROGRAMS.items()}
        result = {name: future.result() for name, future in futures.items()}
    ok = result["ok"]["tests"][0]
    assert base64.b64decode(ok["stdout_b64"]) == b"5\n" and ok["exit_code"] == 0
    assert result["compile_error"]["compile"]["returncode"] != 0 and not result["compile_error"]["tests"]
    assert result["warning"]["compile"]["returncode"] == 0
    assert not result["warning"]["compile"]["warning_free"]
    loop = result["loop"]["tests"][0]
    assert loop["timeout"] or loop["signal"] == 24
    assert result["flood"]["tests"][0]["output_truncated"]
    # The student program cannot signal the server or init: both kill() calls fail.
    assert base64.b64decode(result["kill_parent"]["tests"][0]["stdout_b64"]) == b"-1 -1\n"
