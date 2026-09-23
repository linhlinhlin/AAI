"use strict";
const mappingStatus = {unreviewed:"Chưa gắn nhãn",draft:"Nhãn nháp",confirmed:"Giảng viên đã duyệt",ignored:"Đã bỏ qua"};
const mappingCategory = {misconception:"Quan niệm sai lầm",other_error:"Lỗi khác / trình bày",mixed:"Nhóm hỗn hợp"};
function candidateOverview(r) {
  const total=r.teacher?.total_submissions || 0;
  return `<h4>Máy gợi ý — chưa được xác nhận</h4><p class="caption">Dùng để ưu tiên đọc bài. Đây là số bài khớp mẫu, không phải tỷ lệ hiểu sai đã xác nhận; một bài có thể khớp nhiều mẫu.</p>${(r.teaching?.summaries || []).map(s=>`<article class="teacher-bar candidate-bar"><b>${esc(s.explanation?.title || s.then_vi)}</b><p>${s.n_submissions}/${total} bài khớp (${total ? number(Math.round(s.n_submissions/total*1000)/10) : 0}%) · ${s.category === "presentation_issue" ? "sai khác trình bày" : "giả thuyết cơ chế"}</p><progress max="${total || 1}" value="${s.n_submissions}" aria-label="Số bài khớp mẫu ${esc(s.explanation?.title || s.then_vi)}"></progress></article>`).join("") || '<p class="caption">Chưa có mẫu phù hợp hoặc thiếu log.</p>'}`;
}
function oavTable(conditions) {
  return table(["Đối tượng (Object)","Thuộc tính (Attribute)","Quan hệ","Giá trị (Value)"],conditions.map(c=>`<tr><td>${esc(c.object)}</td><td>${esc(featureLabel(c.attribute))}</td><td>${esc(c.operator)}</td><td>${esc(label(c.value))}</td></tr>`));
}
function proposalSource(source) {return ({llm:"AI đề xuất — chờ duyệt",llm_cache:"AI đề xuất — dùng kết quả đã lưu",local_rules:"Bộ luật cục bộ — chưa phải LLM",none:"Chưa có đề xuất"})[source] || source;}
function teacherDashboard(r) {
  const d=r.teacher;if(!d) return '<p>Chạy lại phân tích để tạo dashboard.</p>';
  const overview=d.overview || [];
  return `<h3>Bức tranh lỗi theo nhóm bài làm</h3><p>Phạm vi: bài ${esc(r.provenance?.dataset?.problem_id)} · ${d.total_submissions} bài làm. ${d.total_students == null ? "Thiếu mã sinh viên: biểu đồ tính theo bài làm." : `${d.total_students} mã sinh viên khác nhau.`}</p>${/synthetic/i.test(r.provenance?.dataset?.dataset_name || "") ? '<p class="result-notice">Dữ liệu tổng hợp để minh họa; không phải kết quả một lớp thực tế.</p>' : ""}<p class="caption">Nhãn chờ duyệt là đề xuất, không phải kết luận đã kiểm chứng. Tỷ lệ là kích thước nhóm / toàn bộ bài trong bộ dữ liệu; không phải xác suất nhãn đúng.</p>${overview.map(item=>`<button class="teacher-bar overview-bar ${item.status === "ignored" ? "ignored" : ""}" data-review-cluster="${esc(item.cluster)}"><span class="status-pill">${esc(item.status === "draft" ? proposalSource(item.source) : mappingStatus[item.status])}</span><h4>${esc(item.status === "ignored" ? "Nhóm đã bỏ qua" : item.label)}</h4><p>Nhóm ${esc(item.cluster)} · ${item.count}/${d.total_submissions} bài · ${number(Math.round(item.percent*10)/10)}%</p><progress max="100" value="${item.percent}" aria-label="Nhóm ${esc(item.cluster)}: ${item.count} bài"></progress><span>Xem và duyệt →</span></button>`).join("") || '<p>Chưa đủ dữ liệu tạo cụm. Xem phần luật để kiểm tra những bằng chứng đã có.</p>'}<p class="caption">${d.excluded_submissions} bài ngoài phân cụm, vẫn thuộc mẫu số. Nhóm bỏ qua không bị xóa khỏi dữ liệu hoặc mẫu số.</p><div class="actions"><button class="primary" data-result-tab="mapping">Duyệt & chỉnh sửa →</button><button class="secondary" data-result-tab="rules">Xem luật giải thích</button></div><details><summary>Tiến độ duyệt: ${d.confirmed_submissions} bài trong nhóm đã duyệt · ${d.ignored_submissions || 0} bài đã bỏ qua</summary><p>${d.unmapped_submissions} bài chưa có nhãn xác nhận (bao gồm ngoài cụm và đã bỏ qua).</p>${d.bars.map(bar=>`<p>${esc(bar.label)} — ${bar.submissions} bài (${number(Math.round(bar.submission_percent*10)/10)}%). ${bar.students == null ? "" : `${bar.students}/${d.total_students} mã sinh viên có ít nhất một bài trong nhóm. Một người có thể thuộc nhiều loại lỗi.`}</p>`).join("")}</details><h4>Gợi ý giảng lại từ nhãn đã duyệt</h4>${(d.mappings || []).filter(m=>m.status === "confirmed").map(m=>`<p><b>${esc(m.label)}:</b> ${esc(m.follow_up)}</p>`).join("") || '<p class="caption">Mở một nhóm để xem gợi ý và duyệt nội dung phù hợp.</p>'}<details><summary>Các mẫu chuyên môn phát hiện trong bài</summary>${candidateOverview(r)}</details><details><summary>Chỉ báo kỹ thuật dành cho nhà nghiên cứu</summary><p>Silhouette: ${number(r.silhouette_train)} · Fidelity: ${number(r.explanation?.holdout_fidelity)}.</p>${technicalDetails(r)}</details>`;
}
function mappingPanel(r) {
  const assignments={...r.train_assignments,...r.holdout_assignments};
  const groups=[...new Set(Object.values(assignments))].sort((a,b)=>a-b);
  if(!groups.length) return '<p>Chưa có cụm để duyệt; xem bằng chứng ở tab luật.</p>';
  const previous=Object.fromEntries((r.teacher?.mappings || []).map(m=>[m.cluster,m]));
  return `<h3>Duyệt & chỉnh sửa đề xuất</h3>${state.llm?.configured ? `<p class="caption">LLM đã cấu hình: ${esc(state.llm.provider)} · ${esc(state.llm.model)}. Nguồn thực tế của mỗi đề xuất ghi trên thẻ bên dưới.</p>` : '<p class="result-notice">Chưa cấu hình LLM: đang dùng bộ luật cục bộ. Xem docs/ai_cluster_labeling.md để kết nối API và chạy lại phân tích.</p>'}<p>Đọc tên lỗi, lý giải và gợi ý giảng dạy; kiểm tra bằng chứng trước khi duyệt. Nhóm chưa có cơ chế chung có thể bỏ qua.</p><label for="mapping-reviewer">Người duyệt · chỉ cần nhập một lần</label><input id="mapping-reviewer" maxlength="120" value="${esc(state.mappingReviewer || localStorage.getItem("mapping-reviewer") || "")}">${groups.map(cluster=>{
    const m=previous[cluster] || {status:"unreviewed",category:"mixed",label:"Chưa có đề xuất",rationale:"Chạy lại phân tích để tạo đề xuất tự động.",follow_up:"Kiểm tra bài đại diện và log."};
    const proposal=r.ai_labeling?.proposals.find(p=>p.cluster === String(cluster));
    const members=Object.keys(assignments).filter(id=>assignments[id] === cluster);
    return `<article class="panel spaced mapping-card" data-cluster="${cluster}" id="review-cluster-${cluster}"><p class="caption">Nhóm ${cluster} · ${members.length} bài · ${esc(mappingStatus[m.status])}</p><span class="status-pill">${esc(m.status === "confirmed" || m.status === "ignored" ? mappingStatus[m.status] : proposalSource(proposal?.source || "none"))}</span><h4>${esc(m.label)}</h4><p><b>Phân loại:</b> ${esc(proposal?.output.misconception_type || mappingCategory[m.category])}</p><p><b>Lý giải:</b> ${esc(m.rationale)}</p><p><b>Gợi ý giảng dạy:</b> ${esc(m.follow_up)}</p><p class="caption">${esc(proposal?.notice || "")}</p><div class="actions"><button class="primary run-button" data-review-action="confirmed">✓ Duyệt nhãn này</button><button class="secondary" data-edit-label>✎ Chỉnh sửa</button><button class="secondary run-button" data-review-action="ignored">Bỏ qua cụm này</button></div><details class="label-editor"><summary>Chỉnh sửa nội dung đề xuất</summary><label>Tên lỗi<input data-field="label" maxlength="200" value="${esc(m.label)}"></label><label>Loại nhóm<select data-field="category">${Object.entries(mappingCategory).map(([key,value])=>`<option value="${key}" ${m.category===key?"selected":""}>${value}</option>`).join("")}</select></label><input type="hidden" data-field="status" value="${m.status}"><label>Lý giải / căn cứ<textarea data-field="rationale" maxlength="2000" rows="3">${esc(m.rationale)}</textarea></label><label>Gợi ý giảng dạy<textarea data-field="follow_up" maxlength="2000" rows="3">${esc(m.follow_up)}</textarea></label><div class="actions"><button class="primary run-button" data-review-action="confirmed">Lưu chỉnh sửa & duyệt</button><button class="secondary run-button" data-review-action="draft">Lưu nháp</button></div></details><details><summary>Xem ${members.length} bài và bằng chứng dùng để đề xuất</summary><div class="cluster-members">${members.map(id=>`<button class="member" data-sample="${esc(id)}">${esc(id)}</button>`).join("")}</div>${proposal ? `<p class="caption">${proposal.input.samples.length}/${members.length} bài được đưa vào mẫu đại diện; không phải toàn bộ cụm. Các định danh sample trong phản hồi ánh xạ về bài thật tại dữ liệu kỹ thuật.</p>${technicalDetails({input:proposal.input,output:proposal.output,sample_bindings:proposal.sample_bindings,provider:proposal.provider,model:proposal.model})}` : ""}</details></article>`;
  }).join("")}<p class="caption">Duyệt hoặc bỏ qua được lưu thành bản mới cho đúng lượt chạy; không sửa annotation chấm mù.</p>`;
}
function readableCondition(c,r) {
  const neg=c.operator === "≠";
  if(c.attribute.startsWith("test:")) {
    const id=c.attribute.slice(5), input=r.test_context?.[id];
    return `${neg ? "Bài làm không có trạng thái" : "Bài làm có trạng thái"} <b>${esc(label(c.value))}</b> ở [Ca kiểm thử ${esc(id)}${input ? `: đầu vào ${esc(input)}` : ""}]`;
  }
  if(c.attribute.startsWith("ast:")) return `Cấu trúc mã: [${esc(featureLabel(c.attribute))}] ${neg ? "khác" : "="} [${esc(label(c.value))}]`;
  return `[${esc(c.object)}] — [${esc(c.attribute)}] ${esc(c.operator)} [${esc(label(c.value))}]`;
}
function teacherRules(r) {
  const rules=r.teacher?.rules || [];
  return `<h3>Luật OAV → tên lỗi</h3><p>Các điều kiện trong mỗi bảng kết hợp bằng VÀ. Tên lỗi lấy từ đề xuất hoặc nhãn đã duyệt; luật chỉ kế thừa phạm vi của nhóm, chưa xác thực từng bài.</p>${rules.map(rule=>`<article class="rule"><p>${rule.conditions.map((c,i)=>`<b>${i ? "VÀ" : "NẾU"}</b> ${readableCondition(c,r)}`).join("<br>")}</p><details><summary>Xem biểu diễn OAV đầy đủ</summary><div class="table-wrap">${oavTable(rule.conditions)}</div></details><p><b>THÌ — ${esc(rule.category ? mappingCategory[rule.category] : "Tên lỗi")}:</b> ${esc(rule.conclusion)}</p><p class="caption">${esc(mappingStatus[rule.status])}. ${rule.status === "draft" ? "Chưa dùng nhãn này để thống kê lỗi đã xác nhận." : ""}</p>${rule.follow_up ? `<p><b>Kiểm tra / giảng lại:</b> ${esc(rule.follow_up)}</p>` : ""}<details><summary>Thông tin kiểm tra mô hình</summary><p>Nhóm nguồn ${rule.cluster}; độ khớp với nhãn cụm trên tập giữ lại: ${number(rule.technical.holdout_precision)}. Không phải độ chính xác nhận diện misconception.</p></details></article>`).join("") || '<p>Chưa có luật phân cụm cho lượt này.</p>'}`;
}
async function restoreTeacherRun(id) {
  const payload=JSON.parse((await api(`/api/artifact?id=${encodeURIComponent(id)}`)).text);
  let report;
  if(payload.kind === "mapping") {
    report=payload.report;state.runSource=payload.source;state.runArm=payload.arm;state.mappingReviewer=payload.reviewer;
  } else if(payload.kind === "run" || payload.kind === "compare") {
    state.runArm=payload.kind === "run" ? "run" : "C";report=payload.results[state.runArm];state.runSource=id;state.mappingReviewer="";
  } else throw new Error("File này là log thao tác, không phải kết quả phân tích hoặc gắn nhãn.");
  await inspectDataset(payload.dataset);state.resultDataset=payload.dataset;renderRun(report,id);page("experiment");
}
document.addEventListener("click",guarded(async event=>{
  const review=event.target.closest("[data-review-cluster]");
  if(review){resultTab("mapping");document.getElementById(`review-cluster-${review.dataset.reviewCluster}`)?.scrollIntoView({block:"start"});}
  const edit=event.target.closest("[data-edit-label]");
  if(edit){const panel=edit.closest(".mapping-card").querySelector(".label-editor");panel.open=true;panel.querySelector("input").focus();}
  const action=event.target.closest("[data-review-action]");
  if(action){
    const reviewer=$("#mapping-reviewer").value.trim();
    if(!reviewer) {$("#mapping-reviewer").focus();throw new Error("Nhập tên người duyệt một lần trước khi lưu.");}
    const card=action.closest(".mapping-card");const status=card.querySelector('[data-field="status"]');const previous=status.value;status.value=action.dataset.reviewAction;
    const mappings=$$(".mapping-card").map(card=>Object.fromEntries([["cluster",card.dataset.cluster],...[...card.querySelectorAll("[data-field]")].map(el=>[el.dataset.field,el.value.trim()])]));
    try {await job({action:"mapping",source:state.runSource,arm:state.runArm,mappings,reviewer},(result,saved)=>{state.mappingReviewer=reviewer;localStorage.setItem("mapping-reviewer",reviewer);renderRun(result.report,saved);resultTab("mapping");});}
    catch(e){status.value=previous;throw e;}
  }
  const restore=event.target.closest("[data-open-run]");if(restore) await restoreTeacherRun(restore.dataset.openRun);
}));
