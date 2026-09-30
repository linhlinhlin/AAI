"use strict";
const $ = (s) => document.querySelector(s);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const state = {user:null, csrf:null, problems:[], history:[], current:null, attempt:null, busy:false, hints:0, report:null, mode:"login", setup:null,generation:0};
const when = (n) => new Date(n*1000).toLocaleString("vi-VN", {day:"2-digit",month:"2-digit",hour:"2-digit",minute:"2-digit"});
const labels = {pass:"Đạt",fail:"Chưa đạt",timeout:"Hết thời gian",runtime_error:"Lỗi thực thi",not_run:"Chưa chạy",queued:"Đang đợi",running:"Đang chấm",system_error:"Chấm bị gián đoạn",accepted:"Đạt tất cả test",compile_error:"Lỗi biên dịch",needs_work:"Cần kiểm tra thêm"};
function toast(message){$("#toast").textContent=message;$("#toast").hidden=false;setTimeout(()=>$("#toast").hidden=true,7000);}
async function api(path, body){
  const generation=state.generation;
  const options={credentials:"same-origin",headers:{}};
  if(body!==undefined){options.method="POST";options.headers={"Content-Type":"application/json","X-CSRF-Token":state.csrf||""};options.body=JSON.stringify(body);}
  const response=await fetch(path,options);const data=await response.json();
  if(!response.ok){if(response.status===401&&generation===state.generation)showAuth();throw new Error(data.error||"Không thể hoàn thành yêu cầu.");}return data;
}
function guarded(fn){return async(event)=>{try{await fn(event);}catch(error){toast(error.message);}};}
function showAuth(){delete document.body.dataset.role;state.generation++;state.user=null;state.csrf=null;state.history=[];state.historyStats={completed:0,attempted:0,solved:[]};state.current=null;state.attempt=null;state.report=null;state.busy=false;for(const id of ["#source","#reflection"])$(id).value="";for(const id of ["#class-report","#detail-body","#attempt-result","#all-history","#problem-history"])$(id).replaceChildren();$("#detail").close();$("#auth-view").hidden=false;$("#app-view").hidden=true;$("#account").hidden=true;}
function authMode(mode){state.mode=mode;const register=mode!=="login";document.querySelectorAll(".register-field").forEach(e=>e.hidden=!register);$("#auth-name").required=register;$("#auth-title").textContent=mode==="setup"?"Thiết lập lớp học.":register?"Bắt đầu hành trình của bạn.":"Chào bạn trở lại.";$("#auth-copy").textContent=mode==="setup"?"Tạo tài khoản giảng viên quản lý lớp học trên máy này.":register?"Tạo tài khoản để lưu code và từng lần thử.":"Đăng nhập để tiếp tục bài đang làm.";$("#auth-submit").textContent=mode==="setup"?"Tạo tài khoản giảng viên →":register?"Tạo tài khoản học viên →":"Đăng nhập →";$("#auth-toggle").textContent=register?"Đã có tài khoản? Đăng nhập":"Chưa có tài khoản? Đăng ký học viên";$("#auth-password").autocomplete=register?"new-password":"current-password";$("#auth-error").textContent="";}
function runner(value){state.runner=value;$("#runner-text").textContent=value.message;$("#runner-dot").classList.toggle("ready",value.ready);$("#submit-code").disabled=state.busy||!value.ready||state.user?.role!=="student";}
function solved(){return new Set(state.historyStats?.solved||[]);}
function renderProblems(){const done=solved();$("#solved-count").textContent=`${done.size} / ${state.problems.length}`;$("#problem-list").innerHTML=state.problems.map((p,i)=>`<button class="problem-button ${state.current?.id===p.id?"active":""}" data-problem="${esc(p.id)}"><span class="number ${done.has(p.id)?"solved":""}">${done.has(p.id)?"✓":String(i+1).padStart(2,"0")}</span><span><strong>${esc(p.title)}</strong><small>${esc(p.topic)}</small></span></button>`).join("");}
function draftKey(){return `aai-draft:${state.user.id}:${state.current.id}`;}
function saveDraft(){if(state.user&&state.current){try{localStorage.setItem(draftKey(),$("#source").value);$("#draft-status").textContent="Đã lưu bản nháp trên trình duyệt";}catch{$("#draft-status").textContent="Trình duyệt không cho lưu bản nháp";}}}
function selectProblem(id){if(state.current)saveDraft();const p=state.problems.find(x=>x.id===id);if(!p)return;state.current=p;state.attempt=null;state.hints=0;$("#problem-topic").textContent=p.topic;$("#problem-title").textContent=p.title;$("#problem-description").textContent=p.description;$("#problem-constraints").textContent=p.constraints;const example=p.tests.find(t=>t.name==="Có phần lẻ")||p.tests[0];$("#example-input").textContent=example.input;$("#example-output").textContent=example.expected;let draft;try{draft=localStorage.getItem(draftKey());}catch{}$("#source").value=draft??p.starter;$("#reflection").value="";$("#hint-content").hidden=true;$("#download-attempt").hidden=true;$("#attempt-result").innerHTML='<div class="empty-state"><span class="empty-icon">⌘</span><h3>Sẵn sàng cho một lần thử.</h3><p>Chạy code để đối chiếu kết quả với các trường hợp của bài.</p></div>';renderProblems();renderHistory();}
function setView(name){document.querySelectorAll("[data-view]").forEach(b=>b.classList.toggle("active",b.dataset.view===name));for(const view of ["practice","progress","teacher"])$("#view-"+view).hidden=view!==name;if(name==="progress")renderProgress();if(name==="teacher"){ $("#teacher-list").hidden=false;$("#class-report").hidden=true;loadClass().catch(e=>toast(e.message));}}
async function signedIn(data){document.body.dataset.role=data.user.role;state.generation++;state.user=data.user;state.csrf=data.csrf;state.history=[];state.historyStats={completed:0,attempted:0,solved:[]};state.current=null;state.attempt=null;$("#auth-view").hidden=true;$("#app-view").hidden=false;$("#account").hidden=false;$("#account-name").textContent=state.user.name;$("#teacher-tab").hidden=state.user.role!=="teacher";$("#greeting").textContent=state.user.role==="teacher"?"Phân tích bài làm":`Chào ${state.user.name}, cùng thử tiếp nhé.`;$("#role-eyebrow").textContent=state.user.role==="teacher"?"":"HỌC BẰNG CÁCH THỬ";$("#auth-password").value="";await refreshHistory();selectProblem(state.problems[0].id);runner(state.runner);setView(state.user.role==="teacher"?"teacher":"practice");const pending=state.history.find(a=>["running","queued"].includes(a.status));if(pending){selectProblem(pending.problem_id);poll(pending.id).catch(e=>toast(e.message));}}
async function refreshHistory(){const data=await api("/api/history");state.history=data.attempts;state.historyStats=data.stats;renderProblems();renderHistory();}
function statusBadge(attempt){const result=attempt.result;return `<span class="pill ${result?.verdict==="accepted"?"pass":""}">${esc(result?`${result.passed}/${result.total} · ${labels[result.verdict]}`:labels[attempt.status]||attempt.status)}</span>`;}
function renderHistory(){if(!state.current)return;const rows=state.history.filter(a=>a.problem_id===state.current.id);$("#problem-history").innerHTML=rows.map(a=>`<button class="history-item" data-attempt="${esc(a.id)}">${esc(when(a.created))} ${statusBadge(a)}</button>`).join("")||'<p class="small muted">Chưa có lần nộp nào. Bản nháp của bạn vẫn ở trên.</p>';}
function testRows(tests){return tests.map(t=>`<details class="test-row" ${t.outcome!=="pass"?"open":""}><summary><span>${esc(t.name||t.test_id)} <span class="pill ${t.outcome==="pass"?"pass":""}">${esc(labels[t.outcome]||t.outcome||"Bằng chứng")}</span></span><small>${t.elapsed_ms==null?"":`${t.elapsed_ms} ms*`}</small></summary><div class="test-evidence"><div><h4>Đầu vào</h4><pre>${esc(t.input)}</pre></div><div><h4>Mong đợi</h4><pre>${esc(t.expected)}</pre></div><div><h4>Chương trình của bạn</h4><pre>${esc(t.output||"(không có output)")}</pre></div></div>${t.focus?`<div class="test-detail">Điểm cần kiểm tra: ${esc(t.focus)}</div>`:""}${t.stderr?`<pre class="diagnostics">${esc(t.stderr)}</pre>`:""}${t.limit?`<p class="test-detail">Đã chạm giới hạn ${esc(t.limit)}.</p>`:""}</details>`).join("");}
function oavTable(oav){return `<div class="table-wrap"><table class="oav-table"><thead><tr><th>Thuộc tính</th><th>Giá trị</th></tr></thead><tbody>${Object.entries(oav||{}).map(([k,v])=>`<tr><td>${esc(k)}</td><td>${esc(v)}</td></tr>`).join("")}</tbody></table></div>`;}
function renderAttempt(attempt){state.attempt=attempt;const r=attempt.result;$("#download-attempt").hidden=!r;if(!r){$("#attempt-result").innerHTML=`<div class="notice">${esc(attempt.progress)}</div>`;return;}const f=r.feedback;$("#attempt-result").innerHTML=`<div class="feedback ${r.verdict==="accepted"?"success":""}"><h3>${esc(f.title)}</h3><p>${esc(f.message)}</p><ul>${f.next_steps.map(t=>`<li>${esc(t)}</li>`).join("")}</ul></div>${r.diagnostics?`<details ${r.verdict==="compile_error"?"open":""}><summary>Thông báo trình biên dịch</summary><pre class="diagnostics">${esc(r.diagnostics)}</pre></details>`:""}${testRows(r.tests)}${r.tests.length?'<p class="small muted">* Thời gian gồm khởi động phiên cách ly, không phải điểm đo tốc độ thuật toán.</p>':""}${r.findings?.map(finding=>`<div class="notice"><b>Giả thuyết cần kiểm tra:</b> ${esc(finding.then_vi)}<br>${esc(finding.explanation?.suggested_follow_up?.join(" ")||"")}</div>`).join("")||""}<details class="technical"><summary>Bằng chứng OAV và nguồn chạy</summary>${oavTable(r.oav)}<pre>${esc(JSON.stringify(r.provenance,null,2))}</pre></details>`;}
async function poll(id){const generation=state.generation;state.busy=true;runner(state.runner);try{for(;;){const a=await api("/api/attempt?id="+encodeURIComponent(id));if(generation!==state.generation)return;$("#run-status").textContent=a.progress;if(a.problem_id===state.current?.id)renderAttempt(a);if(!["running","queued"].includes(a.status)){await refreshHistory();return a;}await new Promise(resolve=>setTimeout(resolve,700));}}finally{if(generation===state.generation){state.busy=false;runner(state.runner);}}}
async function loadAttempt(id){const a=await api("/api/attempt?id="+encodeURIComponent(id));setView("practice");selectProblem(a.problem_id);renderAttempt(a);$("#source").value=a.source;$("#reflection").value=a.reflection;saveDraft();$("#run-status").textContent=`Đang xem lần nộp ${when(a.created)}.`;}
function renderProgress(){$("#progress-stats").innerHTML=stats([["Bài đã đạt test",`${solved().size} / ${state.problems.length}`],["Lượt đã chấm",state.historyStats.completed],["Bài đã thử",state.historyStats.attempted]]);$("#all-history").innerHTML=state.history.length?`<div class="table-wrap"><table><thead><tr><th>Bài tập</th><th>Lần thử</th><th>Kết quả</th><th>Điều bạn thay đổi</th><th></th></tr></thead><tbody>${state.history.map(a=>`<tr><td>${esc(state.problems.find(p=>p.id===a.problem_id)?.title)}</td><td>${esc(when(a.created))}</td><td>${statusBadge(a)}</td><td>${esc(a.reflection||"—")}</td><td><button class="quiet" data-attempt="${esc(a.id)}">Xem bài →</button></td></tr>`).join("")}</tbody></table></div>`:'<div class="empty-state"><h3>Hành trình sẽ được ghi lại từ lần nộp đầu tiên.</h3><p>Quay lại Luyện tập để bắt đầu.</p></div>';}
function stats(items){return items.map(([label,value])=>`<div class="stat"><span>${esc(label)}</span><strong>${esc(value)}</strong></div>`).join("");}
async function loadClass(){
  const data=await api("/api/teacher/overview");state.classData=data;
  $("#teacher-stats").innerHTML=stats([["Học viên",data.students.length],["Lượt đã chấm",data.total_attempts],["Bài cần hỗ trợ",data.problems.reduce((n,p)=>n+p.needs_work,0)]]);
  $("#class-problems").innerHTML=`<div class="table-wrap"><table class="problem-table"><thead><tr><th>Bài tập</th><th>Đã nộp</th><th>Đạt</th><th>Cần hỗ trợ</th><th><span class="sr-only">Thao tác</span></th></tr></thead><tbody>${data.problems.map(p=>{const note=data.recent_reports.find(r=>r.problem_id===p.id&&r.reviews>0);return `<tr><td><strong>${esc(p.title)}</strong></td><td>${p.learners}</td><td>${p.accepted}</td><td>${p.needs_work}</td><td class="row-actions"><button class="secondary" data-analyze="${esc(p.id)}">Mở phân tích</button>${note?`<button class="quiet" data-open-report="${esc(note.id)}">Ghi chú gần nhất</button>`:""}</td></tr>`;}).join("")}</tbody></table></div>`;
}
function teacherList(){
  $("#teacher-list").hidden=false;$("#class-report").hidden=true;
  $("#refresh-class").focus();loadClass().catch(e=>toast(e.message));
}
async function openAnalysis(problemId,k=2){
  const data=await api("/api/teacher/analyze",{problem_id:problemId,k});
  state.classData=await api("/api/teacher/overview");renderReport(data);
}
function noteDraftKey(form){return `aai-note:${state.user.id}:${state.report.id}:${form.dataset.cluster}`;}
function saveNoteDraft(form){
  try{localStorage.setItem(noteDraftKey(form),JSON.stringify(Object.fromEntries(new FormData(form))));form.querySelector(".review-status").textContent="Nháp đã lưu trên máy này";}
  catch{form.querySelector(".review-status").textContent="Chưa lưu nháp — hãy lưu ghi chú trước khi rời trang";}
}
function showSavedNote(form,entry){
  const container=form.closest('.cluster-card');
  container.querySelector('.saved-note').innerHTML=`<b>Ghi chú đã lưu:</b> ${esc(entry.label)}<p>${esc(entry.follow_up)}</p>`;
  container.querySelector('.note-editor summary').textContent='Sửa ghi chú giảng viên';
}

const reasons={fewer_than_four_eligible_rows:"Cần ít nhất 4 bài có test sai và đủ bằng chứng.",fewer_than_two_independent_groups:"Chưa đủ nhóm bài độc lập để chia tập.",fewer_than_three_training_rows:"Chưa đủ bài ở tập xây dựng cụm.",identical_training_features:"Các bài ở tập xây dựng chưa có đặc trưng khác nhau.",k_requires_more_training_rows_or_distinct_patterns:"Số bài hoặc kiểu đặc trưng khác nhau chưa đủ cho k đã chọn.",empty_evaluation_partition:"Chưa có mẫu giữ lại để kiểm tra luật."};

// Teaching hypotheses are evidence-gated local rules, not labels learned by the cluster tree.
const readableTeachingRules = {
  SUM_FORMULA: {
    conditions: ["Sử dụng sai công thức tính toán", "Kết quả không khớp đáp án ở các test được dẫn"],
    conclusion: "Chưa tính đúng tổng theo yêu cầu.",
    followUp: "Đối chiếu công thức với yêu cầu tính tổng từ 1 đến n."
  },
  SUM_INPUT: {
    conditions: ["In lại dữ liệu nhập, chưa thực hiện phép tính", "Kết quả không khớp đáp án ở các test được dẫn"],
    conclusion: "Chưa tính tổng theo yêu cầu.",
    followUp: "Bổ sung bước tính tổng trước khi in kết quả."
  },
  C_SWAP_BY_VALUE: {
    conditions: ["Hàm hoán vị nhận hai biến thường và đổi các bản sao tham số", "Trong test cần đổi chỗ hai số khác nhau, đầu ra vẫn giữ thứ tự ban đầu"],
    conclusion: "Có dấu hiệu hoán vị bản sao, chưa làm đổi biến ở hàm gọi.",
    followUp: "Vẽ biến trong main và tham số của hàm; thử truyền địa chỉ rồi đổi giá trị qua *a, *b. C truyền đối số theo giá trị, kể cả con trỏ."
  },
  C_BRANCH_ATTACHMENT: {
    conditions: ["Code có hai if liên tiếp; else gắn với if thứ hai", "Một test cần một kết luận vị trí nhưng chương trình in nhiều kết luận"],
    conclusion: "Có dấu hiệu gắn else chưa đúng, khiến hai thông báo cùng được in.",
    followUp: "Truy vết lần lượt từng if và xác định else thuộc if nào. Không phải mọi chuỗi if độc lập đều sai."
  },
  C_HARDCODED_OUTPUT: {
    conditions: ["Code in giá trị cố định, không tính đầu ra từ dữ liệu nhập", "Có ít nhất hai test được ghi nhận là không đạt"],
    conclusion: "Có dấu hiệu in hằng số, chưa tính toán theo đầu vào.",
    followUp: "Đổi input và dự đoán output trước khi chạy; chỉ ra biểu thức nào phải phụ thuộc dữ liệu nhập."
  },
  OUTPUT_PRESENTATION: {
    conditions: ["Code có lời gọi xuất dữ liệu; log ghi nhận output thực tế", "Đầu ra chỉ khác đáp án ở cách trình bày được luật kiểm tra"],
    conclusion: "Có sai khác trình bày output ở các test được dẫn.",
    followUp: "So sánh từng ký tự của đáp án và đầu ra. Các test khác vẫn có thể có lỗi logic."
  }
};
function clusterObservations(report, members, findings, labelFor) {
  const covered = new Set(findings.map(f=>f.submission_id));
  const rows = (report.submissions || []).filter(s=>members.includes(s.submission_id));
  const tests = report.problem?.tests || [];
  const frequencies = tests.map(t=>({name:t.name||t.test_id,
    failed:rows.filter(s=>s.outcomes?.[t.test_id]==='fail').length})).filter(t=>t.failed);
  const missing = rows.filter(s=>!covered.has(s.submission_id));
  return `<div class="cluster-observations"><p><b>Test trượt trong nhóm:</b> ${frequencies.map(t=>`${esc(t.name)}: ${t.failed}/${rows.length}`).join(' · ') || 'Chưa có log test trượt.'}</p>
    <details><summary>Đối chiếu đầu ra từng bài · ${rows.length} bài</summary>${rows.map(s=>{
      const logs=(s.logged_tests||[]).filter(t=>s.outcomes?.[t.test_id]==='fail');
      return `<div class="rule"><button class="member" data-evidence="${esc(s.submission_id)}">${esc(labelFor(s.submission_id))}</button><p>${covered.has(s.submission_id)?'Có luật cục bộ khớp':'Chưa xác định nguyên nhân; xem sai khác quan sát được bên dưới.'}</p>${testRows(logs.map(t=>({...t,outcome:'fail'})))}</div>`;
    }).join('')}</details>
    ${missing.length?`<p><b>${missing.length}/${rows.length} bài chưa khớp luật chẩn đoán.</b> Có bằng chứng sai kết quả, chưa đủ căn cứ kết luận nguyên nhân chung.</p>${missing.length < rows.length ? `<div class="members">${missing.map(s=>`<button class="member" data-evidence="${esc(s.submission_id)}">${esc(labelFor(s.submission_id))} · code và test</button>`).join('')}</div>` : ''}`:''}</div>`;
}
function teachingDisplayKey(ruleId) {
  return ['SUM_PREVIOUS', 'SUM_SQUARE'].includes(ruleId) ? 'SUM_FORMULA' : ruleId;
}
function teachingRulesForCluster(report, cluster, members, labelFor) {
  const findings = (report.teaching?.findings || []).filter(f => members.includes(f.submission_id));
  const groups = new Map();
  for (const finding of findings) {
    const key = teachingDisplayKey(finding.rule_id);
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(finding);
  }
  const confirmed = (report.confirmed_reference?.matches || []).filter(r=>members.includes(r.submission_id));
  const heading = '<h3>Dấu hiệu lỗi</h3>' + clusterObservations(report, members, findings, labelFor) + confirmed.map(r=>`<div class="rule"><b>${esc(r.label)}</b><p>Nguồn: AI đề xuất, người dùng đã xác nhận trên đúng code và log này; không phải đánh giá độc lập.</p><p><b>NẾU</b> ${esc(r.rule.if)} <b>VÀ</b> ${esc(r.rule.and)} <b>THÌ</b> ${esc(r.label)}.</p><p>${esc(r.reasoning)}</p><button class="member" data-evidence="${esc(r.submission_id)}">${esc(labelFor(r.submission_id))} · xem bằng chứng</button></div>`).join('');
  if (!groups.size) return `<section class="teaching-rules">${heading}<p class="small muted">${confirmed.length ? "Chưa có luật cục bộ bổ sung." : "Chưa có kết luận chẩn đoán cho các bài này. Thư viện C-Pack là dữ liệu khác, không tự áp nhãn sang bài đang xem."} <button class="quiet" type="button" data-reference-library>Xem thư viện C-Pack-IPAs</button></p></section>`;
  return `<section class="teaching-rules">${heading}<p class="small muted">Các dấu hiệu dưới đây áp dụng cho từng phần của nhóm. Phân cụm theo code/test có thể tách cùng một lỗi thành nhiều nhóm.</p>${[...groups].map(([key, matches]) => {
    const sample = matches[0], ids = [...new Set(matches.map(f => f.submission_id))];
    const wording = readableTeachingRules[key] || {conditions:sample.if_vi, conclusion:sample.then_vi, followUp:sample.suggestion};
    const assignments = {...report.train_assignments, ...report.holdout_assignments};
    const otherClusters = [...new Set((report.teaching?.findings || [])
      .filter(f=>teachingDisplayKey(f.rule_id) === key && assignments[f.submission_id] != null && assignments[f.submission_id] !== cluster)
      .map(f=>assignments[f.submission_id] + 1))].sort((a,b)=>a-b);
    const shared = otherClusters.length ? `<p class="small">Dấu hiệu này cũng có ở nhóm ${otherClusters.join(', ')}. Các nhóm được chia theo đặc trưng code/test, không chia riêng theo tên lỗi.</p>` : '';
    const outputs = [...new Set(matches.flatMap(f=>(f.tests||[]).map(t=>t.output)))];
    const specifics = key === 'C_HARDCODED_OUTPUT' ? `<p><b>Giá trị in cứng quan sát được:</b> ${outputs.map(o=>`<code>${esc(JSON.stringify(o))}</code>`).join(', ')}</p>` : '';
    return `<div class="rule teaching-rule"><b>${ids.length === members.length ? 'Khớp toàn nhóm' : 'Chỉ khớp một phần nhóm'} · ${ids.length}/${members.length} bài</b>${specifics}${shared}<ol class="rule-conditions">${wording.conditions.map((condition,i)=>`<li><b>${i ? "VÀ" : "NẾU"}</b> ${esc(condition)}</li>`).join("")}</ol><p><b>THÌ</b> ${esc(wording.conclusion)}</p><p class="small">Khớp ${ids.length}/${members.length} bài trong nhóm.${ids.length < members.length ? " Chỉ áp dụng cho các bài khớp; chưa có căn cứ gán lỗi này cho cả nhóm." : " Việc khớp luật chưa xác nhận misconception."}</p><p><b>Kiểm tra / giảng lại:</b> ${esc(wording.followUp)}</p><div class="members">${ids.map(id=>`<button class="member" type="button" data-evidence="${esc(id)}">${esc(labelFor(id))} · xem bằng chứng</button>`).join("")}</div>${matches.map(f=>`<details><summary>Code và test · ${esc(labelFor(f.submission_id))}</summary><p>${esc(f.then_vi)}</p>${(f.source||[]).map(part=>`<p class="small">Dòng ${esc(part.line_start)}–${esc(part.line_end)}</p><pre>${esc(part.code)}</pre>`).join('')}${(f.tests||[]).slice(0,2).map(test=>`<p><b>Test ${esc(test.test_id)}</b></p><p class="small">Đầu vào</p><pre>${esc(test.input)}</pre><p class="small">Đáp án cần có</p><pre>${esc(test.expected)}</pre><p class="small">Chương trình in</p><pre>${esc(test.output)}</pre>`).join('')}<p class="small muted">${esc(f.alternative)}</p></details>`).join('')}</div>`;
  }).join("")}</section>`;
}
function inducedRulesForCluster(report, cluster) {
  const rules = (report.teaching?.cluster_rules || []).filter(rule => rule.then_cluster === cluster);
  if (!rules.length) return '';
  return `<details class="induced-rules"><summary>Luật quy nạp phân biệt nhóm ${cluster+1} · ${rules.length} luật</summary><p class="small muted">${esc(report.teaching?.condition_scope_vi||"Luật giữ nguyên các trạng thái đã khai báo trong dữ liệu.")} Cây quyết định học từ các bài xây dựng cụm. Mỗi luật dưới đây dự đoán nhóm, không tự suy ra nguyên nhân hay hiểu biết của học viên. Sai khác ký tự chỉ đo hình thức output.</p>${rules.map(rule=>`<div class="rule induced-rule"><ol class="rule-conditions">${rule.if_vi.map((condition,i)=>`<li><b>${i ? "VÀ" : "NẾU"}</b> ${esc(condition)}</li>`).join("")}</ol><p><b>THÌ</b> dự đoán bài thuộc nhóm ${cluster+1}.</p><p class="small">${rule.train_support} bài dùng xây dựng luật; ${rule.holdout_support} bài dùng kiểm tra. Khớp ID nhóm ở phần kiểm tra: ${rule.holdout_precision==null?"chưa có mẫu":Math.round(rule.holdout_precision*100)+"%"}. Không phải tỷ lệ chẩn đoán đúng lỗi.</p><details><summary>Điều kiện OAV gốc</summary><pre>${esc(rule.if.join("\nAND "))}</pre></details></div>`).join("")}</details>`;
}

// Frozen ILA-2 rules from repair-grounded labels: a checked hypothesis with its held-out accuracy.
function mechanismForCluster(report, cluster) {
  const m = report.mechanism; if (!m || m.status !== "hypothesis") return "";
  const c = (m.clusters || []).find(x => x.cluster === String(cluster)); if (!c) return "";
  const held = m.held_out?.seen_problems, fresh = m.held_out?.unseen_problems;
  const pct = v => v == null ? "—" : Math.round(v * 100) + "%";
  const measured = held ? `Luật đúng ${pct(held.selective_accuracy)} số bài được trả lời ở sinh viên chưa thấy (trả lời ${pct(held.coverage)})${fresh ? `; ở bài tập mới: ${pct(fresh.selective_accuracy)}` : ""}.` : "";
  if (!c.top_category) return `<section class="rule mechanism"><b>Giả thuyết cơ chế</b><p class="small muted">Không luật nào khớp ${c.abstained}/${c.members} bài; hệ thống không đoán.</p></section>`;
  const f = c.feedback || {}, share = c.categories[c.top_category] || 0;
  return `<section class="rule mechanism"><b>Giả thuyết cơ chế · ${esc(f.name || c.top_category)}</b><p>${share}/${c.members} bài khớp luật ILA-2${c.abstained ? `; ${c.abstained} bài không khớp luật nào` : ""}. ${esc(f.hypothesis || "")}</p><p><b>Kiểm tra nhanh:</b> ${esc(f.check || "")}</p><p><b>Giảng lại:</b> ${esc(f.reteach || "")}</p><p class="small muted">${esc(measured)} ${esc(m.caveat)}</p></section>`;
}
function renderReport(data){
  state.report=data;const r=data.report,assignments={...r.train_assignments,...r.holdout_assignments};
  const names=Object.fromEntries(r.students.map(s=>[s.id,s.name]));
  const labelFor=id=>names[r.population[id]]||id.slice(0,8);
  const clusters=[...new Set(Object.values(assignments))].sort();
  const history=(state.classData?.recent_reports||[]).filter(item=>item.problem_id===r.problem.id&&item.id!==data.id);
  $("#teacher-list").hidden=true;$("#class-report").hidden=false;
  $("#class-report").innerHTML=`<section class="panel report-panel">
    <button class="quiet" type="button" data-back-class>← Bài tập</button>
    <div class="section-heading"><h1 tabindex="-1" id="analysis-title">${esc(r.problem.title)}</h1><button id="export-class-report" class="quiet">Tải JSON</button></div>
    <div class="analysis-toolbar"><span>${r.submissions.length} bài đã chấm · ${clusters.length} nhóm bài</span><div><label for="analysis-k">Số nhóm</label><select id="analysis-k"><option value="2" ${r.config?.k===2?"selected":""}>2</option><option value="3" ${r.config?.k===3?"selected":""}>3</option></select><button class="secondary" data-analyze="${esc(r.problem.id)}" data-refresh-analysis>Cập nhật phân tích</button></div></div>
    <p class="small muted">${data.reused?"Đang xem kết quả hiện tại; dữ liệu không đổi.":data.reused===false?"Đã phân tích bài nộp mới nhất.":"Đang xem bản đã lưu. Cập nhật để phân tích bài nộp mới nhất."}</p>
    ${r.status!=="ok"?`<div class="notice">${esc(reasons[r.reason]||r.reason)}</div>`:""}
    ${clusters.map(c=>{const members=Object.keys(assignments).filter(id=>assignments[id]===c),representative=r.medoids[String(c)]||members[0];return `<article class="cluster-card">
      <div class="cluster-head"><h2>Nhóm ${c+1}</h2><span class="pill">${members.length} bài · chưa xác thực</span></div>
      <div class="cluster-members"><button class="member" data-evidence="${esc(representative)}">Bài đại diện · ${esc(labelFor(representative))}</button><details><summary>Tất cả ${members.length} bài</summary><div class="members">${members.map(id=>`<button class="member" data-evidence="${esc(id)}">${esc(labelFor(id))}</button>`).join("")}</div></details></div>
      ${mechanismForCluster(r,c)}${teachingRulesForCluster(r,c,members,labelFor)}${inducedRulesForCluster(r,c)}
      <div class="saved-note"></div>
      <form class="review-form" data-cluster="${c}"><div class="span-2"><button type="button" class="secondary" data-suggest>Gợi ý giảng lại</button><div class="suggestion-preview" aria-live="polite"></div></div>
      <details class="note-editor span-2"><summary>Ghi chú giảng viên · tùy chọn</summary><div class="note-fields">
        <label>Tên nhóm lỗi<input name="label" required maxlength="200" autocomplete="off"></label>
        <label>Loại nhận định<select name="category"><option value="other_error">Cơ chế lỗi quan sát</option><option value="misconception">Giả thuyết quan niệm sai</option><option value="mixed">Nhóm hỗn hợp</option><option value="unclear">Chưa đủ bằng chứng</option></select></label>
        <label class="span-2">Căn cứ từ code và test<textarea name="rationale" required maxlength="2000" rows="3"></textarea></label>
        <label class="span-2">Nội dung giảng lại<textarea name="follow_up" required maxlength="2000" rows="3"></textarea></label>
        <div class="span-2"><button class="secondary" type="submit">Lưu ghi chú</button></div></div></details><span class="small muted review-status span-2" role="status"></span></form>
    </article>`;}).join("")}
    <details class="all-evidence"><summary>Tất cả bài trong phân tích (${r.submissions.length})</summary><div class="members">${r.submissions.map(s=>`<button class="member" data-evidence="${esc(s.submission_id)}">${esc(labelFor(s.submission_id))}</button>`).join("")}</div></details>
    <details class="report-history"><summary>Lịch sử của bài này (${history.length})</summary><p class="small">Giữ bản gần nhất và các bản có ghi chú. Bản cũ không có ghi chú được ẩn.</p><label class="history-filter"><input type="checkbox" id="reviewed-only">Chỉ có ghi chú</label><div class="history-list">${history.map(item=>`<button class="history-item" data-open-report="${esc(item.id)}" data-review-count="${item.reviews}">${esc(when(item.created))} · ${item.reviews} ghi chú</button>`).join("")||'<p class="small muted">Chưa có lịch sử cần hiển thị.</p>'}</div></details>
    <details class="technical"><summary>Phạm vi đánh giá và OAV</summary><p>Chỉ phân nhóm bài sai. Luật cây dự đoán ID nhóm; luật cục bộ gợi ý cơ chế từ code và test. Cả hai chưa xác nhận hiểu biết của học viên. Ghi chú được lưu theo đúng bản phân tích, không tự chuyển sang nhóm mới.</p><pre>${esc(JSON.stringify({split:r.split,provenance:r.provenance,features:r.features},null,2))}</pre></details>
  </section>`;
  for(const review of data.reviews||[])for(const entry of review.payload){const form=document.querySelector(`.review-form[data-cluster="${entry.cluster}"]`);if(!form)continue;for(const key of ["label","rationale","follow_up","category"])form.elements[key].value=entry[key];form.querySelector('.review-status').textContent='Đã lưu trên hệ thống';showSavedNote(form,entry);}
  for(const form of document.querySelectorAll('.review-form')){try{const draft=JSON.parse(localStorage.getItem(noteDraftKey(form)));if(draft){for(const key of ['label','rationale','follow_up','category'])if(typeof draft[key]==='string')form.elements[key].value=draft[key];form.querySelector('.review-status').textContent='Đã khôi phục nháp trên máy này';}}catch{}}
  for(const proposal of data.suggestions||[]){const form=document.querySelector(`.review-form[data-cluster="${proposal.cluster}"]`);if(form)showSuggestion(form,proposal);}
  $('#analysis-title').focus();window.scrollTo({top:0,behavior:'instant'});
}
function showSuggestion(form, proposal){
  form.suggestion=proposal;
  const value=proposal.output;
  const origin=proposal.source==="llm"?`AI · ${proposal.provider} / ${proposal.model}`:"Bộ luật cục bộ";
  const evidence=(value.evidence_samples||[]).map(alias=>proposal.sample_bindings[alias]).filter(Boolean);
  form.querySelector(".suggestion-preview").innerHTML=`<div class="notice"><b>${esc(origin)} · Bản nháp chưa duyệt</b><p>${esc(proposal.notice)}</p><p><b>Tên nhóm:</b> ${esc(value.misconception_name)}</p><p><b>Căn cứ:</b> ${esc(value.reasoning)}</p><p><b>Giảng lại:</b> ${esc(value.teaching_hint)}</p>${evidence.map(id=>`<button type="button" class="member" data-evidence="${esc(id)}">Xem bài dẫn chứng</button>`).join(" ")}${proposal.local_output&&proposal.source==="llm"?`<details><summary>Gợi ý cục bộ gốc</summary><p>${esc(proposal.local_output.misconception_name)}</p><p>${esc(proposal.local_output.reasoning)}</p><p>${esc(proposal.local_output.teaching_hint)}</p></details>`:""}${proposal.llm_error?`<p class="small muted">Mã lỗi: ${esc(proposal.llm_error.code)}${proposal.llm_error.retry_after_seconds?" · Thử lại sau 30 giây":""}</p>`:""}<p class="small muted">Điền sẽ thay nội dung các ô bên dưới; chưa lưu nhận xét giảng viên.</p><button type="button" class="secondary" data-apply-suggestion>Điền vào bản nháp</button> <button type="button" class="secondary" data-suggest data-use-llm="true">Diễn giải bằng AI</button></div>`;
}
document.addEventListener("click",guarded(async event=>{
  const button=event.target.closest("[data-suggest]");
  if(button){
    const form=button.closest(".review-form"), reportId=state.report.id, generation=state.generation;
    const useLLM=button.dataset.useLlm==="true", originalText=button.textContent;
    button.disabled=true;button.textContent=useLLM?"Đang nhờ AI diễn giải…":"Đang tạo gợi ý…";
    try{
      const proposal=await api("/api/teacher/suggest",{id:reportId,cluster:form.dataset.cluster,use_llm:useLLM});
      if(generation===state.generation&&state.report?.id===reportId&&form.isConnected)showSuggestion(form,proposal);
    }catch(error){
      if(form.isConnected)form.querySelector(".review-status").textContent=" "+error.message+" Bản nháp hiện có vẫn được giữ.";
    }finally{button.disabled=false;button.textContent=originalText;}
  }
  const apply=event.target.closest("[data-apply-suggestion]");
  if(apply){
    const form=apply.closest(".review-form"), value=form.suggestion.output;
    form.elements.label.value=value.misconception_name;
    form.elements.category.value=value.category;
    form.elements.rationale.value=value.reasoning;
    form.elements.follow_up.value=value.teaching_hint;form.querySelector(".note-editor").open=true;saveNoteDraft(form);
    form.querySelector(".review-status").textContent=" Bản nháp chưa lưu — kiểm tra rồi bấm Lưu nhận xét giảng viên.";
  }
}));
function download(value,name){const blob=new Blob([JSON.stringify(value,null,2)],{type:"application/json"});const url=URL.createObjectURL(blob);const a=document.createElement("a");a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
function showEvidence(id){const r=state.report.report,s=r.submissions.find(x=>x.submission_id===id);if(!s)return;$("#detail-title").textContent=`Bài làm · ${r.students.find(x=>x.id===s.student_id)?.name||id}`;$("#detail-body").innerHTML=`<pre class="source-view">${esc(s.source_code)}</pre><h3>Bằng chứng test</h3>${testRows(s.logged_tests.map(t=>({...t,outcome:s.outcomes[t.test_id]})))}<h3>Object: ${esc(id)} · Attribute → Value</h3>${oavTable(r.observed_oav[id])}`;$("#detail").showModal();}
$("#auth-toggle").addEventListener("click",()=>authMode(state.mode==="login"?"register":"login"));
$("#auth-form").addEventListener("submit",async event=>{event.preventDefault();$("#auth-submit").disabled=true;$("#auth-error").textContent="";try{const result=await api("/api/"+state.mode,{username:$("#auth-username").value,name:$("#auth-name").value,password:$("#auth-password").value,token:state.setup});await signedIn(result);}catch(error){$("#auth-error").textContent=error.message;}finally{$("#auth-submit").disabled=false;}});
$("#logout").addEventListener("click",guarded(async()=>{saveDraft();await api("/api/logout",{});state.history=[];state.historyStats={completed:0,attempted:0,solved:[]};state.current=null;state.attempt=null;state.report=null;state.classData=null;showAuth();authMode("login");}));
$("#source").addEventListener("input",saveDraft);
$("#source").addEventListener("keydown",event=>{if(event.key==="Tab"){event.preventDefault();const el=event.target;el.setRangeText("    ",el.selectionStart,el.selectionEnd,"end");saveDraft();}if(event.key==="Enter"&&(event.ctrlKey||event.metaKey)){event.preventDefault();$("#submit-code").click();}});
$("#reset-code").addEventListener("click",()=>{if(confirm("Thay bản nháp bằng code ban đầu? Các lần nộp đã lưu vẫn được giữ.")){$("#source").value=state.current.starter;saveDraft();}});
$("#show-hint").addEventListener("click",()=>{state.hints=Math.min(state.hints+1,state.current.hints.length);$("#hint-content").textContent=state.current.hints.slice(0,state.hints).join(" ");$("#hint-content").hidden=false;});
$("#submit-code").addEventListener("click",guarded(async()=>{saveDraft();state.busy=true;runner(state.runner);try{const queued=await api("/api/submit",{problem_id:state.current.id,source:$("#source").value,reflection:$("#reflection").value});await poll(queued.id);}finally{state.busy=false;runner(state.runner);}}));
$("#runner-refresh").addEventListener("click",guarded(async()=>runner(await api("/api/runner",{}))));
$("#download-attempt").addEventListener("click",()=>download(state.attempt,`aai-${state.attempt.id}.json`));
$("#refresh-class").addEventListener("click",guarded(loadClass));
$('#expand-detail').addEventListener('click',()=>{const expanded=$('#detail').classList.toggle('expanded');$('#expand-detail').setAttribute('aria-pressed',String(expanded));$('#expand-detail').textContent=expanded?'Thu gọn':'Mở rộng';});
$("#close-detail").addEventListener("click",()=>$("#detail").close());
document.addEventListener("click",guarded(async event=>{if(event.target.closest("[data-back-class]")){teacherList();return;}const savedReport=event.target.closest("[data-open-report]");if(savedReport)renderReport(await api("/api/teacher/report?id="+savedReport.dataset.openReport));const p=event.target.closest("[data-problem]");if(p)selectProblem(p.dataset.problem);const v=event.target.closest("[data-view]");if(v)setView(v.dataset.view);const a=event.target.closest("[data-attempt]");if(a)await loadAttempt(a.dataset.attempt);const e=event.target.closest("[data-evidence]");if(e)showEvidence(e.dataset.evidence);const analyze=event.target.closest("[data-analyze]");if(analyze){analyze.disabled=true;try{await openAnalysis(analyze.dataset.analyze,analyze.hasAttribute("data-refresh-analysis")?Number($("#analysis-k").value):2);}finally{analyze.disabled=false;}}if(event.target.closest("#export-class-report")){const current=await api("/api/teacher/report?id="+state.report.id);download(current,`aai-class-${state.report.id}.json`);}}));
document.addEventListener("submit",guarded(async event=>{if(!event.target.matches(".review-form"))return;event.preventDefault();const form=event.target;const values=Object.fromEntries(new FormData(form));const entry={...values,cluster:form.dataset.cluster,status:"confirmed"};await api("/api/teacher/review",{id:state.report.id,mappings:[entry]});form.querySelector(".review-status").textContent=" Đã lưu · nhận xét lớp học";showSavedNote(form,entry);try{localStorage.removeItem(noteDraftKey(form));}catch{}}));
document.addEventListener('input',event=>{const form=event.target.closest('.review-form');if(form)saveNoteDraft(form);});
document.addEventListener('change',event=>{if(event.target.id==='reviewed-only')for(const item of document.querySelectorAll('.report-history [data-review-count]'))item.hidden=event.target.checked&&Number(item.dataset.reviewCount)===0;});
function textSize(large){document.documentElement.dataset.textSize=large?'large':'normal';$('#text-size').setAttribute('aria-pressed',String(large));$('#text-size').textContent=large?'Chữ thường':'Chữ lớn';}
try{textSize(localStorage.getItem('aai-text-size')==='large');}catch{}
$('#text-size').addEventListener('click',()=>{const large=document.documentElement.dataset.textSize!=='large';textSize(large);try{localStorage.setItem('aai-text-size',large?'large':'normal');}catch{}});
async function boot(){const params=new URLSearchParams(location.hash.slice(1));state.setup=params.get("setup");if(state.setup){history.replaceState(null,"",location.pathname);authMode("setup");}const data=await api("/api/bootstrap");state.problems=data.problems;state.runner=data.runner;if(data.user)await signedIn(data);else showAuth();}
boot().catch(error=>toast(error.message));

async function showReferenceLibrary(){
  const data=await api('/api/teacher/reference');
  $('#detail-title').textContent=`C-Pack-IPAs · ${data.clusters.length} cụm · ${data.n_submissions} bài`;
  $('#detail-body').innerHTML='<button class="secondary" data-cpack-ai>Nhãn đã xác nhận · 150 bài</button><p>Đây là các cụm của bộ dữ liệu C-Pack-IPAs, không phải các nhóm bài luyện tập vừa xem. “Khớp 35/35” chỉ áp dụng cho 35 bài trong cụm thư viện tương ứng.</p><p>Đã có bộ tham chiếu 150 bài C-Pack được người dùng xác nhận; chưa duyệt toàn bộ 2.151 bài. Nhãn ITSP đã duyệt không áp dụng ở đây. Code và log lịch sử; gói còn thiếu đề gốc, chưa chạy lại C.</p>'+data.clusters.map(c=>`<div class="rule"><b>${esc(c.problem_id)} · ${c.n_submissions} bài</b><p class="small">${esc(c.cluster_id)}</p><p>${c.semantic_patterns.length?c.semantic_patterns.map(p=>`${esc(p.then_vi)} — khớp ${p.n_submissions}/${c.n_submissions} bài`).join('<br>'):'Chưa có chẩn đoán cục bộ khớp; cần đọc code/test.'}</p><button class="secondary" data-cpack-cluster="${esc(c.cluster_id)}">Xem dấu hiệu và bằng chứng</button></div>`).join('');
  if(!$('#detail').open)$('#detail').showModal();
}
async function showCPackCluster(id){
 const data=await api('/api/teacher/reference?cluster='+encodeURIComponent(id)),c=data.cluster;
 $('#detail-title').textContent=c.problem_id+' · '+c.n_submissions+' bài · chờ xác nhận';
 $('#detail-body').innerHTML=`<button class="quiet" data-reference-library>← Danh sách C-Pack-IPAs</button><h3>Dấu hiệu lỗi quan sát được</h3><p>Chưa gán gold. Một dấu hiệu ở vài bài không đại diện cho cả cụm.</p>${c.test_statistics.map(t=>`<p>Test ${esc(t.test_id)}: ${t.n_failed}/${t.n_cluster} bài trượt (${Math.round(t.failure_rate_cluster*100)}%); ${t.n_not_run} chưa chạy.</p>`).join('')}<h3>Mẫu code/test cục bộ</h3>${c.semantic_patterns.map(p=>`<p>${esc(p.then_vi)} · ${p.n_submissions}/${c.n_submissions} bài khớp.</p>`).join('')||'<p>Chưa có mẫu chẩn đoán khớp.</p>'}<details><summary>OAV và luật phân nhóm gốc</summary><p>Luật dự đoán ID cụm, chưa xác nhận nguyên nhân lỗi.</p><pre>${esc(JSON.stringify({features:c.prominent_features,rules:c.learned_if_then_rules},null,2))}</pre></details><h3>Bài làm (${c.members.length})</h3>${[...c.members].sort((a,b)=>Number(b.representative)-Number(a.representative)).map(m=>`<details class="rule"><summary>${esc(m.sample_id)}${m.representative?' · đại diện':''}</summary><pre>${esc(m.raw_code)}</pre>${testRows(m.logged_tests.map(t=>({...t,outcome:m.outcomes[t.test_id]})))}</details>`).join('')}`;
}
document.addEventListener('click',guarded(async e=>{if(e.target.closest('[data-reference-library]'))await showReferenceLibrary();const c=e.target.closest('[data-cpack-cluster]');if(c)await showCPackCluster(c.dataset.cpackCluster);}));

async function showCPackAI(){
 const data=await api('/api/teacher/reference?source=cpack_gold');
 $('#detail-title').textContent='C-Pack-IPAs · 150 nhận định đã được bạn xác nhận';
 $('#detail-body').innerHTML='<button class="quiet" data-reference-library>← Thư viện C-Pack</button><p>Phạm vi: 150 bài pilot, không phải toàn bộ 2.151 bài. AI đề xuất, người dùng đã xác nhận. Sáu trường hợp chưa chắc vẫn chưa có nhãn gold; không phải chấm mù độc lập. Các câu luật là diễn giải code/log.</p>'+data.records.map(r=>`<details class="rule"><summary>Bài ${r.number} · ${esc(r.problem_id)} · ${esc(r.misconception_label)}</summary><p>${esc({supported:'Có căn cứ code/log',multiple:'Nhiều lỗi cùng xuất hiện',uncertain:'Cần kiểm tra thêm'}[r.decision])}</p><h3>Dấu hiệu lỗi</h3><p><b>NẾU</b> ${esc(r.rule.if)} <b>VÀ</b> ${esc(r.rule.and)} <b>THÌ</b> gợi ý: ${esc(r.misconception_label)}.</p><p>${esc(r.reasoning)}</p><p><b>Giảng lại:</b> ${esc(r.teaching_hint)}</p><p class="small muted">${esc(r.notes)}</p><p>Dòng căn cứ: ${esc(r.source_lines.join(', '))}</p><pre>${esc(r.source_code)}</pre>${testRows(r.logged_tests.map(t=>({...t,outcome:r.outcomes[t.test_id]})))}</details>`).join('');
}
document.addEventListener('click',guarded(async e=>{if(e.target.closest('[data-cpack-ai]'))await showCPackAI();}));
