"use strict";
const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => [...document.querySelectorAll(selector)];
const state = {token: "", datasets: [], artifacts: [], rows: [], result: null, busy: false};
const esc = (value) => String(value ?? "").replace(/[&<>"']/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const pretty = (value) => JSON.stringify(value, null, 2);
const labels = {agglomerative:"Gom cụm phân cấp",kmeans:"K-means",exact:"Chữ ký test giống nhau",combined:"Test và cấu trúc",outcomes:"Kết quả test",structural:"Cấu trúc mã",eligible:"Đủ điều kiện",parse_error:"Lỗi phân tích cú pháp",incomplete:"Chưa đủ kết quả test",execution_error:"Lỗi thực thi",no_failure:"Không có test trượt",pass:"Đạt",fail:"Không đạt",not_run:"Chưa chạy",runtime_error:"Lỗi thực thi",timeout:"Hết thời gian",__unknown__:"Chưa xác định",ACCEPTED:"Đạt",WRONG_ANSWER:"Kết quả không đúng",ok:"Hợp lệ",error:"Có lỗi",unsupported:"Chưa hỗ trợ","0":"Không ghi nhận","1":"Có"};
const label = value => value == null ? "Chưa xác định" : (labels[value] ?? String(value));
const featureNames = {for:"Vòng lặp for",while:"Vòng lặp while",do:"Vòng lặp do",if:"Câu lệnh if",range:"Lời gọi range",return:"Lệnh return",inclusive_comparison:"So sánh ≤ hoặc ≥",strict_comparison:"So sánh < hoặc >",subscript:"Truy cập theo chỉ số",zero_index:"Truy cập chỉ số 0",one_index:"Truy cập chỉ số 1",pointer_declarator:"Khai báo con trỏ",pointer_parameter:"Tham số con trỏ",array_parameter:"Tham số mảng",address_of:"Lấy địa chỉ &",dereference:"Giải tham chiếu *",update:"Tăng hoặc giảm ++/--",augassign:"Gán kết hợp như +=",parse:"Phân tích cú pháp"};
function featureLabel(key) { return key.startsWith("test:") ? `Ca kiểm thử ${key.slice(5)}` : featureNames[key.replace(/^ast:(c_)?/,"")] || key; }
function technicalDetails(value) { return `<details class="technical-details"><summary>Dữ liệu kỹ thuật để đối chiếu (JSON)</summary><pre>${esc(pretty(value))}</pre></details>`; }
function clusterDistribution(groups) { return Object.entries(groups).map(([id,count])=>`${id === "None" || id === "null" ? "Chưa gán cụm" : "Cluster " + esc(id)} — ${esc(count)} bài`).join("; ") || "Chưa có bài"; }
function evidenceContext(id) { return ({C_BRANCH_ATTACHMENT:"cấu trúc điều khiển if–else",C_SWAP_BY_VALUE:"tham số và lời gọi hàm hoán vị",OUTPUT_PRESENTATION:"chuỗi ký tự trong mã"})[id] || "mẫu cấu trúc trong mã"; }
function explanationSections(value) {
  return [["code_pattern","Mẫu cấu trúc mã"],["behavioral_pattern","Mẫu hành vi quan sát"],["hypothesis","Giả thuyết"],["caveat","Giới hạn suy luận"],["suggested_follow_up","Bước kiểm tra tiếp theo"]].map(([key,title])=>`<section class="rule-section"><h4>${title}</h4><ul>${value[key].map(item=>`<li>${esc(item)}</li>`).join("")}</ul></section>`).join("");
}
const number = (value) => value == null ? "Chưa xác định" : typeof value === "number" ? Number(value.toFixed(3)).toString() : String(value);
const download = (id, label = "Tải JSON ↓") => `<a class="secondary link-button" href="/api/artifact?id=${encodeURIComponent(id)}&download=1">${esc(label)}</a>`;
const table = (headers, rows, extra = "") => `<table class="${extra}"><thead><tr>${headers.map(h=>`<th>${esc(h)}</th>`).join("")}</tr></thead><tbody>${rows.join("")}</tbody></table>`;
const reason = {
  identical_training_features: "Các mẫu train có đặc trưng giống nhau; chưa đủ thông tin để tách cụm.",
  no_varying_structural_features: "Không có đặc trưng cấu trúc biến thiên trong tập train.",
  k_requires_more_training_rows_or_distinct_patterns: "Số cụm k quá lớn so với số mẫu hoặc mẫu đặc trưng khác nhau. Hãy giảm k.",
  single_cluster: "Chỉ tạo được một cụm.", fewer_than_four_eligible_rows: "Cần ít nhất 4 bài làm đủ điều kiện.",
  fewer_than_two_independent_groups: "Không đủ hai nhóm độc lập để chia train/holdout.",
  fewer_than_three_training_rows: "Tập train có ít hơn 3 bài. Hãy giảm tỷ lệ holdout."
};
function error(message) { $("#error").textContent = message; $("#error").hidden = false; }
async function api(url, options = {}) {
  const response = await fetch(url, options);
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `HTTP ${response.status}`);
  return data;
}
function guarded(fn) { return async (...args) => { try { await fn(...args); } catch(e) { error(e.message); } }; }
function page(name) {
  $$(".page").forEach(el=>el.hidden = el.id !== `page-${name}`);
  $$("nav button").forEach(el=>el.classList.toggle("active", el.dataset.page === name));
  history.replaceState(null, "", `#${name}`);
  if (name === "compare") updateConfig();
}
async function refresh() {
  const data = await api("/api/bootstrap");
  Object.assign(state, data);
  const previous = $("#dataset").value;
  $("#dataset").innerHTML = state.datasets.map(d=>`<option value="${esc(d.id)}">${esc(d.problem)} · ${esc(d.language.toUpperCase())}${d.id.startsWith("data/demo") ? " · demo tổng hợp" : ""}</option>`).join("");
  $("#dataset").value = state.datasets.some(d=>d.id === previous) ? previous : (state.datasets.find(d=>d.problem === "2825")?.id || state.datasets[0]?.id || "");
  updateConfig(); renderArtifacts();
}
function config() {
  return {method: $("#method").value, feature_mode: $("#feature-mode").value,
    k: Number($("#k").value), seed: Number($("#seed").value),
    test_weight: Number($("#test-weight").value)/100, test_fraction: Number($("#fraction").value)};
}
function updateConfig() {
  const d = state.datasets.find(d=>d.id === $("#dataset").value);
  $("#dataset-summary").textContent = d ? `${d.count} bài làm · ${d.tests} tests · ${d.language.toUpperCase()}` : "Chưa có dữ liệu";
  const c = config();
  $("#weight-value").textContent = `${$("#test-weight").value}%`;
  const exact = c.method === "exact";
  if (exact) $("#feature-mode").value = "outcomes";
  $("#k").disabled = exact; $("#feature-mode").disabled = exact;
  $("#test-weight").disabled = exact || c.feature_mode !== "combined";
  $("#method-note").textContent = exact ? "Exact signatures chỉ dùng outcomes; k và trọng số cấu trúc không áp dụng." : "Cùng bài, cùng test suite. Chỉ đọc log đã có; không chạy mã sinh viên.";
  $("#compare-config").textContent = d ? `Bài ${d.problem} · ${label(c.method)} · k=${c.k} · seed=${c.seed} · holdout ${c.test_fraction*100}%` : "Chọn dữ liệu ở trang Thí nghiệm.";
}
async function job(payload, onComplete) {
  if (state.busy) throw new Error("Một tác vụ đang chạy. Vui lòng đợi.");
  state.busy = true; $("#error").hidden = true;
  $$(".run-button").forEach(b=>b.disabled = true);
  const notice = $("#job-status"); notice.hidden = false; notice.classList.add("busy");
  notice.textContent = "Đang xử lý… Bạn có thể chuyển trang; kết quả sẽ được lưu khi hoàn tất.";
  try {
    const queued = await api("/api/jobs", {method:"POST", headers:{"Content-Type":"application/json","X-Workbench-Token":state.token}, body:JSON.stringify(payload)});
    let result;
    do {
      await new Promise(resolve=>setTimeout(resolve, 650));
      result = await api(`/api/job?id=${encodeURIComponent(queued.id)}`);
      if(result.progress) notice.textContent=result.progress;
    } while (["queued", "running"].includes(result.status));
    if (result.status === "failed") throw new Error(result.error);
    const failedCheck = result.result.kind === "check" && !result.result.passed;
    notice.textContent = failedCheck ? "Kiểm tra chưa đạt. Xem log bên dưới; kết quả đã được lưu." : "Đã hoàn tất và lưu kết quả mới trong results/web_runs/.";
    await onComplete(result.result, result.download);
    await refresh();
  } catch (e) { notice.textContent = "Tác vụ chưa hoàn tất. Xem thông báo lỗi."; throw e; }
  finally { state.busy = false; notice.classList.remove("busy"); $$(".run-button").forEach(b=>b.disabled = false); }
}
async function inspectDataset(id) {
  const data = await api(`/api/dataset?id=${encodeURIComponent(id)}`);
  state.rows = data.rows; state.inspected = id;
  $("#data-title").textContent = `${data.manifest.problem_id} · ${data.rows.length} bài · suite ${data.manifest.suite_version}`;
  renderSamples(); return data;
}
function renderSamples() {
  const query = $("#sample-search").value.toLowerCase();
  const rows = state.rows.filter(r=>r.submission_id.toLowerCase().includes(query));
  $("#sample-list").innerHTML = rows.length ? table(["Bài làm", "Test đạt", "Trạng thái xử lý", "Bằng chứng"], rows.map(r=>`<tr><td><code>${esc(r.submission_id)}</code></td><td>${Object.values(r.outcomes).filter(v=>v==="pass").length}/${Object.keys(r.outcomes).length}</td><td>${esc(label(r.route))}</td><td><button class="secondary" data-sample="${esc(r.submission_id)}">Xem →</button></td></tr>`)) : '<div class="empty-small">Không có bài làm phù hợp.</div>';
}
function openSample(id) {
  const row = state.rows.find(r=>r.submission_id === id);
  if (!row) return error("Hãy mở đúng dataset của kết quả trước khi xem bài làm.");
  $("#dialog-title").textContent = id;
  const logs = row.logged_tests;
  $("#dialog-body").innerHTML = `<p class="source-meta">${esc(row.language)} · ${esc(label(row.route))} · student ID: ${esc(row.student_id ?? "không có")}<br>Số dòng dưới đây tính trên source chuẩn hóa, đã bỏ header log lịch sử.</p><div class="evidence-grid"><div><h3>Source sinh viên</h3><pre class="code-view">${esc(row.source_code.split("\n").map((line,i)=>`${String(i+1).padStart(3)}  ${line}`).join("\n"))}</pre></div><div><h3>OAV được trích</h3><div class="table-wrap">${table(["Thuộc tính", "Giá trị"],Object.entries(row.oav).map(([key,value])=>`<tr><td><code>${esc(featureLabel(key))}</code></td><td class="${value === "pass" ? "pass" : value === "fail" ? "fail" : ""}">${esc(label(value))}</td></tr>`))}</div></div></div><h3>Test evidence · log lịch sử</h3>${logs.length ? `<div class="table-wrap">${table(["Test","Verdict","Input","Expected","Actual"],logs.map(t=>`<tr><td>${esc(t.test_id)}</td><td>${esc(label(t.verdict))}</td><td><code>${esc(t.input)}</code></td><td><code>${esc(t.expected)}</code></td><td><code>${esc(t.output)}</code></td></tr>`))}</div>` : `<p class="caption">Dataset này chỉ cung cấp trạng thái outcomes, không có log input/expected/actual riêng.</p>${table(["Ca kiểm thử","Kết quả"],Object.entries(row.outcomes).map(([id,value])=>`<tr><td>${esc(id)}</td><td>${esc(label(value))}</td></tr>`))}`}`;
  $("#detail-dialog").showModal();
}
function renderRun(report, saved) {
  state.result = report; $("#empty-result").hidden = true; $("#run-result").hidden = false;
  const ok = report.status === "ok";
  $("#run-result").innerHTML = `<div class="result-head"><h2>Kết quả · ${esc(report.provenance?.dataset?.problem_id ?? "thí nghiệm")}</h2>${download(saved)}</div><div class="panel"><div class="result-head"><span class="status-pill ${ok ? "" : "warn"}">${ok ? "Đã phân cụm" : "Chưa thể phân cụm"}</span><span class="caption">${esc(label(report.method))} · ${esc(label(report.feature_mode))}</span></div>${!ok ? `<p class="result-notice">${esc(reason[report.reason] || report.reason)}</p>` : ""}<div class="tabs"><button data-result-tab="teacher" class="active">Tổng quan lớp</button><button data-result-tab="mapping">Duyệt & chỉnh sửa</button><button data-result-tab="clusters">Cụm & bài làm</button><button data-result-tab="rules">Luật giải thích</button><button data-result-tab="oav">Ma trận OAV</button><button data-result-tab="details">Thông số & routing</button></div><div id="result-content"></div></div>`;
  resultTab("teacher");
}
function renderTeaching(report) {
  const teaching = report.teaching;
  const learned = report.explanation;
  if (!teaching) return '<p>Chạy lại thí nghiệm để tạo luật diễn giải mới.</p>';
  const cards = teaching.summaries.map(summary=>{
    const findings = teaching.findings.filter(f=>f.rule_id === summary.rule_id);
    const e = summary.explanation;
    if (!e) return '<p>Chạy lại thí nghiệm để dùng mẫu giải thích mới.</p>';
    return `<article class="teaching-rule"><span class="status-pill ${summary.category === "presentation_issue" ? "" : "warn"}">${summary.category === "presentation_issue" ? "Sai khác output" : "Giả thuyết cần xác nhận"}</span><h3>${esc(e.title)}</h3><h4>NẾU — OAV nhận diện chuyên môn</h4><div class="table-wrap">${oavTable(findings[0].conditions_oav || [])}</div><p><b>THÌ — giả thuyết lỗi:</b> ${esc(e.title)}</p>${explanationSections(e)}<p class="caption">${summary.n_submissions} bài khớp · tập xây dựng ${summary.by_split.train || 0} · tập giữ lại ${summary.by_split.holdout || 0} · ngoài phân cụm ${summary.by_split.unassigned || 0}.</p><p class="caption"><b>Phân bố:</b> ${clusterDistribution(summary.by_cluster)}</p>${findings.map(f=>`<details class="rule-evidence"><summary>${esc(f.submission_id)} · ${f.cluster == null ? "chưa gán cụm" : "Cluster " + esc(f.cluster)} · ${f.tests.length} ca kiểm thử dẫn chứng</summary><div class="actions"><button class="secondary" data-sample="${esc(f.submission_id)}">Mở toàn bộ bài làm →</button></div><h4>Evidence 1 — ${esc(evidenceContext(f.rule_id))}</h4><p class="caption">Đoạn mã cho thấy mẫu cấu trúc đang được kiểm tra; chưa phải dấu vết thực thi.</p>${f.source.map(source=>`<p class="caption">Vị trí đối chiếu: dòng ${source.line_start}–${source.line_end} trong mã đã chuẩn hóa</p><pre>${esc(source.code)}</pre>`).join("")}<h4>Evidence 2 — output thực tế trong log</h4><p class="caption">Đối chiếu kết quả mong đợi và kết quả được ghi lại cho cùng đầu vào. Không chạy lại mã trong lượt này.</p><div class="table-wrap">${table(["Ca kiểm thử","Đầu vào","Kết quả mong đợi","Output thực tế"],f.tests.map(t=>`<tr><td>${esc(t.test_id)}</td><td><pre>${esc(t.input)}</pre></td><td><pre>${esc(t.expected)}</pre></td><td><pre>${esc(t.output)}</pre></td></tr>`))}</div></details>`).join("")}</article>`;
  }).join("");
  return `<h3>Giả thuyết từ bộ nhận diện chuyên môn</h3><p class="caption">Các gợi ý dưới đây chưa phải nhãn xác nhận cho toàn bộ cụm.</p><div class="result-notice">${teaching.n_matched}/${teaching.n_analyzed} bài khớp ít nhất một mẫu.</div>${cards || '<p>Chưa có mẫu phù hợp hoặc thiếu bằng chứng.</p>'}`;
}
function resultTab(name) {
  const r = state.result; if (!r) return;
  $$("[data-result-tab]").forEach(b=>b.classList.toggle("active", b.dataset.resultTab === name));
  const box = $("#result-content");
  if (name === "teacher") { box.innerHTML=teacherDashboard(r);
  } else if (name === "mapping") { box.innerHTML=mappingPanel(r);
  } else if (name === "clusters") {
    const groups = {};
    Object.entries({...r.train_assignments,...r.holdout_assignments}).forEach(([id,cluster])=>(groups[cluster] ||= []).push(id));
    box.innerHTML = `<p class="legend">Nền xanh: medoid đại diện · H: holdout · còn lại: train.</p>` + Object.entries(groups).map(([cluster,ids])=>`<article class="cluster"><div class="cluster-title"><strong><span class="cluster-number">${esc(cluster)}</span>Cụm ${esc(cluster)}</strong><span>${ids.length} bài</span></div><div class="cluster-members">${ids.map(id=>`<button class="member ${r.medoids?.[cluster] === id ? "medoid" : ""}" data-sample="${esc(id)}">${esc(id)}${id in (r.holdout_assignments || {}) ? " · H" : ""}</button>`).join("")}</div></article>`).join("");
    if (!Object.keys(groups).length) box.innerHTML = '<div class="empty-small">Chưa có assignments. Xem lý do hoặc routing.</div>';
  } else if (name === "rules") {
    box.innerHTML = teacherRules(r) + renderTeaching(r);
  } else if (name === "oav") {
    const features = r.features || [];
    box.innerHTML = `<p class="caption">Chỉ những đặc trưng được sử dụng ở lượt chạy này. Trọng số ghi trong tiêu đề cột.</p><div class="table-wrap">${table(["Submission",...features.map(f=>`${featureLabel(f.name)} (${number(f.weight)})`)],Object.entries(r.oav || {}).map(([id,values])=>`<tr><td>${esc(id)}</td>${features.map(f=>`<td class="${values[f.name] === "pass" ? "pass" : values[f.name] === "fail" ? "fail" : ""}">${esc(label(values[f.name]))}</td>`).join("")}</tr>`),"oav")}</div>`;
  } else {
    box.innerHTML = `<p>Tập giữ lại được gán theo bài đại diện của các cụm đã xây dựng. Thiếu mã sinh viên thì chưa bảo đảm hai tập độc lập theo sinh viên.</p>${table(["Thông tin","Giá trị"],[["Số bài xây dựng cụm",r.split?.train_ids?.length],["Số bài giữ lại",r.split?.holdout_ids?.length],["Số bài thiếu mã sinh viên",r.identity?.missing_student_ids],["Số bài giữ lại hòa khoảng cách",r.holdout_assignment_ties],...Object.entries(r.route_counts || {}).map(([key,value])=>[label(key),value])].map(([key,value])=>`<tr><td>${esc(key)}</td><td>${esc(number(value))}</td></tr>`))}${technicalDetails(r)}`;
  }
}
function renderCompare(result, saved) {
  $("#compare-result").innerHTML = table(["Arm", "Trạng thái", "Đặc trưng", "Cụm", "Silhouette", "Fidelity / majority"],Object.entries(result.results).map(([arm,r])=>`<tr><td><strong>${esc(arm)}</strong></td><td>${esc(r.status === "ok" ? "OK" : reason[r.reason] || r.reason)}</td><td>${r.features?.length ?? "—"}</td><td>${r.n_clusters ?? "—"}</td><td>${number(r.silhouette_train)}</td><td>${number(r.explanation?.holdout_fidelity)} / ${number(r.explanation?.holdout_majority_baseline_fidelity)}</td></tr>`)) + `<div class="actions">${download(saved,"Tải toàn bộ A/B/C ↓")}${Object.keys(result.results).map(arm=>`<button class="secondary" data-view-arm="${esc(arm)}">Xem chi tiết ${esc(arm)}</button>`).join("")}</div>`;
  state.comparison = {result,saved};
}
function renderArtifacts() {
  const query = $("#artifact-search").value.toLowerCase();
  const files = state.artifacts.filter(r=>r.id.toLowerCase().includes(query));
  $("#artifact-list").innerHTML = `<p class="caption">${files.length} file · hiển thị tối đa 150 kết quả, nhập thêm để thu hẹp.</p>`+table(["File", "Kích thước", "Thao tác"],files.slice(0,150).map(f=>`<tr><td class="file-path">${esc(f.id)}</td><td>${Math.ceil(f.size/1024)} KB</td><td>${f.id.endsWith(".zip") ? "" : `<button class="secondary" data-artifact="${esc(f.id)}">Xem</button>`} ${download(f.id,"Tải ↓")}${f.id.startsWith("results/web_runs/") && f.id.endsWith("/result.json") ? `<button class="secondary" data-open-run="${esc(f.id)}">Mở dashboard</button>` : ""}</td></tr>`));
}
async function openArtifact(id) {
  const data = await api(`/api/artifact?id=${encodeURIComponent(id)}`);
  $("#dialog-title").textContent = id;
  $("#dialog-body").innerHTML = `${download(id,"Tải file ↓")}<p class="caption">SHA-256: <code>${esc(data.sha256)}</code></p><pre>${esc(data.text)}</pre>`;
  $("#detail-dialog").showModal();
}
function renderFuture() {
  const items = [
    ["Biên dịch & chạy code", "Sandbox chạy test trực tiếp trên bài nộp; hiện chỉ sử dụng log có sẵn."],
    ["Đặc trưng ngữ nghĩa nâng cao", "Mở rộng bộ luật hiện có sang assignment trong điều kiện, phạm vi vòng lặp và luồng dữ liệu tổng quát."],
    ["ILA quy nạp luật", "Hiện dùng cây quyết định nông để giải thích cụm; ILA chưa được tích hợp."],
    ["Chấm bài trực tiếp trên web", "Editor annotation, khóa vòng chấm và tài khoản reviewer độc lập."],
    ["Adjudication có người phụ trách", "Luồng giải quyết bất đồng với lịch sử quyết định; không tự phán quyết bằng AI."],
    ["Đánh giá cơ chế / tập mới", "Sampling được khóa, nhãn cơ chế, pairwise precision/recall và kiểm tra leakage."],
    ["Adapter C++ / Java / LMS", "Nhập dữ liệu gốc của hệ thống khác; hiện nhận schema manifest + JSONL của dự án."],
    ["Hiệu quả giảng dạy", "Đo thời gian review và giá trị phản hồi trong lớp thực tế, chưa có kết quả kiểm chứng."]
  ];
  $("#future-features").innerHTML = items.map(([title,text])=>`<article class="panel"><span class="future-label">SẮP CÓ · CHƯA TRIỂN KHAI</span><h2>${esc(title)}</h2><p>${esc(text)}</p><button disabled class="secondary">Chưa khả dụng</button></article>`).join("");
}

$$("nav button").forEach(b=>b.addEventListener("click",()=>page(b.dataset.page)));
$(".brand").addEventListener("click",()=>page("experiment"));
$$("#experiment-form input, #experiment-form select").forEach(el=>el.addEventListener("input",updateConfig));
$("#experiment-form").addEventListener("submit",guarded(async event=>{
  event.preventDefault();
  const dataset = $("#dataset").value;
  await job({action:"run",dataset,config:config()},async (result,saved)=>{
    await inspectDataset(dataset);state.resultDataset=dataset;state.runSource=saved;state.runArm="run";state.mappingReviewer="";renderRun(result.results.run,saved);
  });
}));
$("#compare-run").addEventListener("click",guarded(async()=>{
  if ($("#method").value === "exact") throw new Error("Exact signatures không có arm structural. Hãy chọn average-linkage hoặc K-means ở Thí nghiệm.");
  if (!$("#experiment-form").reportValidity()) return;
  await job({action:"compare",dataset:$("#dataset").value,config:config()},async(result,saved)=>{
    await inspectDataset(result.dataset);renderCompare(result,saved);
  });
}));
$("#inspect-current").addEventListener("click",guarded(()=>inspectDataset($("#dataset").value)));
$("#sample-search").addEventListener("input",renderSamples);
$("#artifact-search").addEventListener("input",renderArtifacts);
$("#upload-dataset").addEventListener("click",guarded(async()=>{
  const manifest = $("#manifest-file").files[0], submissions = $("#submissions-file").files[0];
  if (!manifest || !submissions) throw new Error("Chọn đủ manifest JSON và submissions JSONL.");
  await job({action:"upload",manifest:await manifest.text(),submissions:await submissions.text(),evidence:await $("#evidence-file").files[0]?.text()},async(result)=>{
    await refresh();$("#dataset").value = result.dataset;updateConfig();await inspectDataset(result.dataset);
  });
}));
$("#open-codebook").addEventListener("click",guarded(()=>openArtifact("results/itsp/human_review/CODEBOOK.md")));
$$("[data-annotation]").forEach(b=>b.addEventListener("click",guarded(async()=>{
  const files = await Promise.all([...$("#annotation-files").files].map(async f=>({name:f.name,text:await f.text()})));
  if (!files.length) throw new Error("Chọn file annotation trước khi thực hiện.");
  await job({action:"annotation",mode:b.dataset.annotation,files,coordinator_confirmed:$("#coordinator-confirmed").checked},(result,saved)=>{
    $("#annotation-result").innerHTML = `<div class="actions">${download(result.output,"Tải annotation output ↓")}${download(saved,"Tải log & provenance ↓")}</div><p class="caption">${esc(result.notice)}</p><p>${result.mode === "validate" ? `${result.value.valid_files} file có cấu trúc hợp lệ.` : "Đã xử lý file. Xem kết quả chi tiết bên dưới; thiếu đánh giá được giữ ở trạng thái chưa xác định."}</p>${technicalDetails(result.value)}`;
  });
})));
$$("[data-check]").forEach(b=>b.addEventListener("click",guarded(()=>job({action:"check",check:b.dataset.check},(result,saved)=>{
  $("#check-result").innerHTML = `<div class="result-head"><h2>${result.passed ? "Kiểm tra đạt" : "Kiểm tra chưa đạt"}</h2>${download(saved,"Tải log ↓")}</div>${result.log ? `<pre>${esc(result.log)}</pre>` : `<p>${result.checked != null ? `Đã đối chiếu ${result.checked} file; ${result.mismatches?.length || 0} file không khớp.` : `Đã kiểm tra gói gồm ${result.audit?.n_samples ?? "—"} hồ sơ và ${result.audit?.n_zip_files ?? "—"} file.`}</p>${technicalDetails(result)}`}<p class="caption">Kết quả kỹ thuật không chứng minh nhãn misconception đúng.</p>`;
}))));
document.addEventListener("click",guarded(async event=>{
  const b = event.target.closest("[data-sample], [data-result-tab], [data-artifact], [data-view-arm]");
  if (!b) return;
  if (b.dataset.sample) {
    if (b.closest("#run-result") && state.inspected !== state.resultDataset) await inspectDataset(state.resultDataset);
    openSample(b.dataset.sample);
  }
  if (b.dataset.resultTab) resultTab(b.dataset.resultTab);
  if (b.dataset.artifact) await openArtifact(b.dataset.artifact);
  if (b.dataset.viewArm) {
    const {result,saved} = state.comparison;
    page("experiment");
    await inspectDataset(result.dataset); state.resultDataset=result.dataset;state.runSource=saved;state.runArm=b.dataset.viewArm;state.mappingReviewer="";renderRun(result.results[b.dataset.viewArm],saved);
  }
}));
$("#close-dialog").addEventListener("click",()=>$("#detail-dialog").close());
renderFuture();
guarded(async()=>{await refresh();const wanted=location.hash.slice(1);page($$(".page").some(p=>p.id === `page-${wanted}`) ? wanted : "experiment");})();
