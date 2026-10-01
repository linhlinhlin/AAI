// AAI Lab client. Plain DOM with no build step; server text is only ever inserted as text.

const main = document.getElementById('main');
const sheet = document.getElementById('sheet');
const toastBox = document.getElementById('toast');
const announcer = document.getElementById('announce');
const SVG_NS = 'http://www.w3.org/2000/svg';

const VIEWS = {
  lop: {title: 'Lớp học', render: (param, token) => viewCohort('class', param, token)},
  'chay-thu': {title: 'Chạy thử', render: viewTrial},
  'c-pack': {title: 'Dữ liệu C-Pack', render: (param, token) => viewCohort('cpack', param, token)},
  'nghien-cuu': {title: 'Nghiên cứu', render: viewStudy},
};
const SOURCE_LABEL = {
  exercise_rule: 'Luật viết tay cho bài này',
  c_rule: 'Luật viết tay cho mọi bài C',
  cpack_rule: 'Luật ILA-2 học từ C-Pack',
};
const OUTCOME = {
  pass: {text: 'đạt', tone: 'pass', icon: 'check'},
  fail: {text: 'sai', tone: 'fail', icon: 'cross'},
  timeout: {text: 'quá thời gian', tone: 'warn', icon: 'clock'},
  runtime_error: {text: 'lỗi khi chạy', tone: 'warn', icon: 'alert'},
  not_run: {text: 'chưa chạy', tone: 'warn', icon: 'alert'},
};
const ICONS = {
  check: ['M4.5 10.5 8.5 14.5 15.5 6'],
  cross: ['M6 6l8 8M14 6l-8 8'],
  clock: ['M10 3.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Z', 'M10 6.5V10l2.5 1.5'],
  alert: ['M10 3.5 17 16H3Z', 'M10 8.5v3', 'M10 13.8v.2'],
  minus: ['M5.5 10h9'],
  close: ['M5.5 5.5l9 9M14.5 5.5l-9 9'],
  chevron: ['M8 5.5 12.5 10 8 14.5'],
  play: ['M7 5.2v9.6L14.6 10Z'],
  reset: ['M4.5 10a5.5 5.5 0 1 0 1.7-4', 'M4.5 3.8v3h3'],
  external: ['M8.5 5.5H5.5v9h9v-3', 'M11 4.5h4.5V9', 'M15.5 4.5 9.5 10.5'],
};

const state = {
  k: {class: 'auto', cpack: 'auto'},
  problem: {class: null, cpack: null, trial: null},
  selected: new Map(),
  cache: new Map(),
  runner: null,
  lastRoute: null,
};
let renderToken = 0;
let lastTrigger = null;

// ---------- small utilities ----------

function h(tag, props, ...children) {
  const el = document.createElement(tag);
  for (const child of children.flat(Infinity)) {
    if (child != null && child !== false) el.append(child instanceof Node ? child : String(child));
  }
  for (const [key, value] of Object.entries(props || {})) {
    if (value == null || value === false) continue;
    if (key === 'text') el.textContent = value;
    else if (key === 'vars') for (const [name, v] of Object.entries(value)) el.style.setProperty(name, v);
    else if (key.startsWith('on')) el.addEventListener(key.slice(2), value);
    else if (key === 'value') el.value = value;
    else el.setAttribute(key, value === true ? '' : value);
  }
  return el;
}

function icon(name, className) {
  const el = document.createElementNS(SVG_NS, 'svg');
  if (className) el.setAttribute('class', className);
  el.setAttribute('viewBox', '0 0 20 20');
  el.setAttribute('aria-hidden', 'true');
  for (const d of ICONS[name]) {
    const path = document.createElementNS(SVG_NS, 'path');
    path.setAttribute('d', d);
    el.append(path);
  }
  return el;
}

const decimal = (value, digits = 2) => value.toFixed(digits).replace('.', ',').replace(/^-/, '−');
const percent = (share) => `${Math.round(share * 100)}%`;
const quoted = (name) => `“${name}”`;
const count = (value) => value.toLocaleString('vi-VN');

const storage = {
  get(key) { try { return localStorage.getItem(`aai-lab:${key}`); } catch { return null; } },
  set(key, value) { try { localStorage.setItem(`aai-lab:${key}`, value); } catch { /* storage is optional */ } },
  remove(key) { try { localStorage.removeItem(`aai-lab:${key}`); } catch { /* storage is optional */ } },
};

async function api(path, body) {
  const init = body === undefined ? {headers: {Accept: 'application/json'}} : {
    method: 'POST',
    headers: {'Content-Type': 'application/json', 'X-AAI-Lab': '1'},
    body: JSON.stringify(body),
  };
  let response;
  try {
    response = await fetch(path, init);
  } catch {
    throw new Error('Không kết nối được AAI Lab. Kiểm tra cửa sổ đang chạy app rồi thử lại.');
  }
  let data = null;
  try { data = await response.json(); } catch { /* not JSON */ }
  if (!response.ok) throw new Error(data?.error || `Máy chủ trả về lỗi ${response.status}.`);
  return data;
}

function cached(key, load) {
  if (!state.cache.has(key)) {
    state.cache.set(key, load().catch((error) => { state.cache.delete(key); throw error; }));
  }
  return state.cache.get(key);
}

function forget(prefix) {
  for (const key of [...state.cache.keys()]) if (key.startsWith(prefix)) state.cache.delete(key);
}

function announce(text) {
  announcer.textContent = '';
  requestAnimationFrame(() => { announcer.textContent = text; });
}

const reducedMotion = () => matchMedia('(prefers-reduced-motion: reduce)').matches;

let toastTimer;
function toast(message, action, sticky = false) {
  clearTimeout(toastTimer);
  const parts = [h('span', {text: message})];
  if (action?.href) parts.push(h('a', {href: action.href, text: action.label, onclick: hideToast}));
  if (action?.run) parts.push(h('button', {type: 'button', text: action.label, onclick: () => { hideToast(); action.run(); }}));
  if (action || sticky) parts.push(h('button', {type: 'button', class: 'icon-btn', 'aria-label': 'Đóng thông báo', onclick: hideToast}, icon('close')));
  toastBox.replaceChildren(...parts);
  if (!action && !sticky) toastTimer = setTimeout(hideToast, 4000);
}
function hideToast() {
  clearTimeout(toastTimer);
  toastBox.replaceChildren();
}

function tag(text, tone, iconName) {
  return h('span', {class: tone ? `tag tag-${tone}` : 'tag'}, iconName && icon(iconName), text);
}

function statusIcon(outcome) {
  const meta = OUTCOME[outcome] || OUTCOME.not_run;
  return h('span', {class: 'status-icon', 'data-tone': meta.tone, 'aria-hidden': 'true'}, icon(meta.icon));
}

// ---------- C highlighting ----------

const C_TOKENS = new RegExp([
  String.raw`(\/\*[\s\S]*?\*\/|\/\/[^\n]*)`,
  String.raw`("(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*')`,
  String.raw`(^[ \t]*#[^\n]*)`,
  String.raw`(\b(?:0[xX][\da-fA-F]+|\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)[uUlLfF]*\b)`,
  String.raw`(\b(?:int|long|short|char|float|double|void|unsigned|signed|const|static|struct|union|enum|typedef|size_t|bool|FILE)\b)`,
  String.raw`(\b(?:if|else|for|while|do|return|break|continue|switch|case|default|sizeof|goto)\b)`,
].join('|'), 'gm');
const TOKEN_CLASS = ['c', 's', 'p', 'n', 't', 'k'];

function escapeHtml(text) {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function highlight(code) {
  let out = '';
  let last = 0;
  for (const match of code.matchAll(C_TOKENS)) {
    const kind = TOKEN_CLASS[match.slice(1).findIndex((group) => group !== undefined)];
    out += escapeHtml(code.slice(last, match.index));
    out += `<span class="tok-${kind}">${escapeHtml(match[0])}</span>`;
    last = match.index + match[0].length;
  }
  return out + escapeHtml(code.slice(last));
}

function lineNumbers(code) {
  return Array.from({length: code.split('\n').length}, (_, i) => i + 1).join('\n');
}

function codeView(code) {
  const source = code.replace(/\n$/, '');
  const pre = h('pre', {tabindex: '0', 'aria-label': 'Mã nguồn'});
  const inner = h('code');
  inner.innerHTML = highlight(source);
  pre.append(inner);
  return h('div', {class: 'code-view'}, h('div', {class: 'gutter', 'aria-hidden': 'true', text: lineNumbers(source)}), pre);
}

// ---------- routing ----------

function parseHash() {
  const [route, param] = location.hash.replace(/^#\/?/, '').split('/');
  return {route: VIEWS[route] ? route : 'lop', param: param ? decodeURIComponent(param) : null};
}

function setHash(route, param) {
  const hash = `#/${route}${param ? `/${encodeURIComponent(param)}` : ''}`;
  if (location.hash !== hash) history.replaceState(null, '', hash);
}

async function render() {
  const {route, param} = parseHash();
  const token = ++renderToken;
  const changed = state.lastRoute !== null && state.lastRoute !== route;
  state.lastRoute = route;
  for (const link of document.querySelectorAll('.nav a')) {
    if (link.dataset.route === route) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  }
  document.title = `${VIEWS[route].title} · AAI Lab`;
  if (changed) hideToast();
  try {
    await VIEWS[route].render(param, token);
  } catch (error) {
    if (token === renderToken) show(token, page(errorNotice(error, render)));
  }
  if (changed && token === renderToken) {
    const heading = main.querySelector('h1');
    heading?.setAttribute('tabindex', '-1');
    heading?.focus();
  }
}

function show(token, ...nodes) {
  if (token !== renderToken) return false;
  main.replaceChildren(...nodes);
  return true;
}

function page(...children) {
  return h('div', {class: 'page'}, ...children);
}

function loadingLine(text) {
  return h('p', {class: 'loading', role: 'status'}, h('span', {class: 'spinner', 'aria-hidden': 'true'}), text);
}

function whileLoading(token, text, target) {
  const timer = setTimeout(() => {
    if (target) target.replaceChildren(loadingLine(text));
    else show(token, page(loadingLine(text)));
  }, 160);
  return () => clearTimeout(timer);
}

function errorNotice(error, retry) {
  return h('div', {class: 'notice notice-error', role: 'alert'},
    h('h2', {text: 'Chưa tải được nội dung'}),
    h('p', {text: error.message}),
    retry && h('div', null, h('button', {type: 'button', class: 'btn', text: 'Thử lại', onclick: retry})));
}

// ---------- runner status ----------

async function refreshRunner() {
  const box = document.getElementById('runner');
  try {
    const status = await api('/api/state');
    state.runner = status.runner;
    box.dataset.state = status.runner.ready ? 'ready' : 'down';
    box.querySelector('.runner-text').textContent = status.runner.ready ? 'Docker sẵn sàng' : 'Docker chưa sẵn sàng';
    box.title = status.runner.message;
  } catch {
    box.dataset.state = 'down';
    box.querySelector('.runner-text').textContent = 'Mất kết nối máy chủ';
  }
  return state.runner;
}

// ---------- cohort views: class and C-Pack ----------

const COHORT_TEXT = {
  class: {
    route: 'lop', title: 'Lớp học', people: 'học viên',
    lede: 'Bài sai mới nhất của mỗi học viên được gom theo cách chúng trượt test, để dạy lại theo từng nhóm lỗi.',
  },
  cpack: {
    route: 'c-pack', title: 'Dữ liệu C-Pack', people: 'sinh viên',
    lede: 'Cùng cách phân tích trên bài thật của C-Pack-IPAs. Nhãn kiểm chứng từ bản sửa của sinh viên chỉ dùng để đối chiếu, không dùng để gom nhóm.',
  },
};

async function viewCohort(source, param, token) {
  const text = COHORT_TEXT[source];
  const done = whileLoading(token, source === 'cpack' ? 'Đang đọc dữ liệu C-Pack (lần đầu mất vài giây)' : 'Đang tải lớp học');
  let listing;
  try {
    listing = await cached(`problems:${source}`, () => api(`/api/problems?source=${source}`));
  } finally {
    done();
  }
  if (token !== renderToken) return;
  const heading = h('div', null, h('h1', {text: text.title}), h('p', {class: 'lede', text: text.lede}));
  if (!listing.available) {
    show(token, page(h('header', {class: 'page-head'}, heading), unavailable(listing)));
    return;
  }
  const problems = listing.problems;
  const valid = (id) => id && problems.some((p) => p.id === id);
  const fallback = (problems.find((p) => p.failing > 0) || problems[0])?.id;
  let problemId = [param, state.problem[source], storage.get(`problem:${source}`)].find(valid) || fallback;
  const body = h('div', {class: 'cohort'});

  const problemSelect = h('select', {id: `${source}-problem`, onchange: (event) => {
    problemId = event.target.value;
    remember();
    load();
  }}, problems.map((p) => h('option', {value: p.id,
    text: p.failing ? `${p.title} — ${p.failing} bài sai` : `${p.title} — chưa có bài sai`})));
  problemSelect.value = problemId;
  const kSelect = h('select', {id: `${source}-k`, onchange: (event) => {
    state.k[source] = event.target.value;
    load();
  }}, h('option', {value: 'auto', text: 'Tự động'}), [2, 3, 4, 5, 6].map((k) => h('option', {value: String(k), text: `${k} nhóm`})));
  kSelect.value = state.k[source];

  const remember = () => {
    state.problem[source] = problemId;
    storage.set(`problem:${source}`, problemId);
    setHash(text.route, problemId);
  };
  const load = () => loadCohort(source, problemId, body, token);
  remember();
  show(token, page(
    h('header', {class: 'page-head'}, heading,
      h('div', {class: 'controls'},
        h('label', {class: 'field field-wide', for: problemSelect.id}, h('span', {text: 'Bài tập'}), problemSelect),
        h('label', {class: 'field', for: kSelect.id}, h('span', {text: 'Số nhóm'}), kSelect))),
    body));
  await load();
}

function unavailable(listing) {
  return h('div', {class: 'notice'},
    h('h2', {text: listing.reason}),
    h('p', {class: 'muted', text: 'Chạy ba lệnh sau trong thư mục misconceptions-prototype, rồi tải lại trang. Lần đầu có thể mất khoảng một giờ vì phải chạy lại toàn bộ bài trong Docker.'}),
    h('pre', {text: listing.steps.join('\n')}));
}

async function loadCohort(source, problemId, body, token) {
  const k = state.k[source];
  const done = whileLoading(token, 'Đang phân tích bài sai', body);
  let report;
  try {
    report = await cached(`analysis:${source}:${problemId}:${k}`,
      () => api(`/api/analysis?source=${source}&problem=${encodeURIComponent(problemId)}&k=${k}`));
  } catch (error) {
    done();
    if (token === renderToken) body.replaceChildren(errorNotice(error, () => loadCohort(source, problemId, body, token)));
    return;
  } finally {
    done();
  }
  if (token !== renderToken || state.problem[source] !== problemId || state.k[source] !== k) return;
  body.replaceChildren(...cohortContent(source, report));
}

function cohortContent(source, report) {
  const text = COHORT_TEXT[source];
  const stats = report.stats;
  if (report.status === 'empty') {
    const nobody = !stats.students;
    return [h('div', {class: 'notice empty-state'},
      h('h2', {text: nobody ? 'Chưa có bài nộp cho bài này' : `Cả ${stats.students} ${text.people} đều đã đạt`}),
      h('p', {class: 'muted', text: nobody
        ? 'Chạy một bài trong Chạy thử rồi thêm vào lớp để bắt đầu phân tích.'
        : 'Không có bài sai nên không có nhóm lỗi để phân tích.'}),
      source === 'class' && h('a', {class: 'btn', href: `#/chay-thu/${encodeURIComponent(report.problem.id)}`, text: 'Mở Chạy thử'}))];
  }
  const summary = h('p', {class: 'summary'},
    h('span', null, h('strong', {class: 'num', text: `${report.n_failing} bài sai`}),
      ` trên ${count(stats.students)} ${text.people} · ${report.k} nhóm lỗi`,
      source === 'cpack' ? ` · ${stats.labelled} bài có nhãn kiểm chứng` : ''));
  const key = `${source}:${report.problem.id}`;
  const exists = (index) => report.groups.some((g) => g.index === index);
  let selected = exists(state.selected.get(key)) ? state.selected.get(key) : report.groups[0].index;
  const panel = h('section', {class: 'panel card', id: 'group-panel', role: 'tabpanel', tabindex: '0'});
  const tabs = h('div', {class: 'groups-list', role: 'tablist', 'aria-orientation': 'vertical', 'aria-label': 'Nhóm lỗi'});

  const select = (index, fromPointer) => {
    selected = index;
    state.selected.set(key, index);
    for (const tab of tabs.children) {
      const on = Number(tab.dataset.index) === index;
      tab.setAttribute('aria-selected', String(on));
      tab.tabIndex = on ? 0 : -1;
    }
    const group = report.groups.find((g) => g.index === index);
    panel.setAttribute('aria-labelledby', `group-tab-${index}`);
    panel.replaceChildren(...groupPanel(source, report, group, () => refreshTab(group)));
    if (fromPointer && matchMedia('(max-width: 900px)').matches) {
      panel.scrollIntoView({block: 'start', behavior: reducedMotion() ? 'auto' : 'smooth'});
    }
  };
  const refreshTab = (group) => {
    const tab = tabs.querySelector(`[data-index="${group.index}"]`);
    tab?.replaceChildren(...groupTabContent(report, group));
  };
  for (const group of report.groups) {
    tabs.append(h('button', {type: 'button', role: 'tab', class: 'group-tab', id: `group-tab-${group.index}`,
      'data-index': String(group.index), 'aria-controls': 'group-panel',
      onclick: (event) => select(group.index, event.detail > 0)}, groupTabContent(report, group)));
  }
  tabs.addEventListener('keydown', (event) => {
    const list = [...tabs.children];
    const current = list.indexOf(document.activeElement);
    const next = {ArrowDown: current + 1, ArrowRight: current + 1, ArrowUp: current - 1, ArrowLeft: current - 1,
      Home: 0, End: list.length - 1}[event.key];
    if (current < 0 || next === undefined) return;
    event.preventDefault();
    const target = list[(next + list.length) % list.length];
    target.focus();
    select(Number(target.dataset.index), false);
  });
  select(selected, false);
  const several = report.groups.length > 1;
  return [summary, h('div', {class: 'workspace'},
    h('div', {class: 'groups'}, tabs,
      several && h('div', {class: 'strip-legend', 'aria-hidden': 'true'},
        h('p', {text: 'Mỗi ô là một test, theo thứ tự của đề:'}),
        h('span', null, h('span', {class: 'cell', 'data-level': '0'}), 'cả nhóm đạt'),
        h('span', null, h('span', {class: 'cell', 'data-level': '1'}), 'một số trượt'),
        h('span', null, h('span', {class: 'cell', 'data-level': '2'}), 'đa số trượt')),
      h('p', {class: 'method', text: methodLine(report)})),
    panel)];
}

function methodLine(report) {
  if (report.n_failing < 4 || report.k === 1 && report.silhouette == null && report.groups.length === 1) {
    return 'Cần ít nhất 4 bài sai với cách trượt khác nhau để chia nhóm.';
  }
  const how = report.silhouette == null ? 'do bạn chọn' : `chọn theo silhouette ${decimal(report.silhouette)}`;
  return `Gom bằng K-means trên kết quả test và cách output lệch; k = ${report.k}, ${how}.`;
}

function signature(group) {
  return h('span', {class: 'strip', 'aria-hidden': 'true'}, group.tests.map((row) => {
    const share = row.failing / row.size;
    return h('span', {class: 'cell', 'data-level': share >= 0.6 ? '2' : share > 0 ? '1' : '0'});
  }));
}

function groupTabContent(report, group) {
  const review = group.review?.status;
  return [
    h('span', {class: 'group-top'}, h('b', {text: `Nhóm ${group.index}`}),
      h('span', {class: 'num', text: `${group.size}/${report.n_failing} bài`})),
    h('span', {class: 'group-title', text: group.title}),
    report.groups.length > 1 && signature(group),
    h('span', {class: 'group-tags'},
      !group.hypothesis && (group.mixed ? tag(`Trộn ${group.mixed.length} giả thuyết`, 'warn') : tag('Chưa có giả thuyết')),
      review === 'confirmed' && tag('Đã xác nhận', 'pass', 'check'),
      review === 'rejected' && tag('Không chung lỗi', 'fail', 'cross')),
  ];
}

function groupPanel(source, report, group, onReviewSaved) {
  const hypothesis = group.hypothesis;
  const head = h('header', {class: 'panel-head'},
    h('div', {class: 'panel-top'},
      h('p', {class: 'panel-meta num', text: `Nhóm ${group.index} · ${group.size}/${report.n_failing} bài sai`}),
      verdictControl(source, report, group, onReviewSaved)),
    h('h2', {text: group.title}),
    hypothesis && h('p', {class: 'hypothesis-line'},
      tag(SOURCE_LABEL[hypothesis.source], 'accent'),
      h('span', {class: 'num', text: `khớp ${hypothesis.matched}/${hypothesis.size} bài`
        + (hypothesis.source === 'cpack_rule' ? '' : ` · loại lỗi: ${hypothesis.family}`)})),
    hypothesis?.statement && h('p', {class: 'statement', text: hypothesis.statement}));
  const teaching = hypothesis
    ? teachingCards(hypothesis)
    : group.mixed
      ? h('div', {class: 'no-hypothesis'},
        h('p', {text: `Các bài trong nhóm khớp ${group.mixed.length} luật khác nhau, không luật nào khớp quá nửa nhóm: cùng cách trượt test nhưng chưa chắc cùng một lỗi. Nên xem và dạy riêng từng trường hợp.`}),
        h('ul', {class: 'observations'}, group.mixed.map((item) => h('li', null,
          h('span', {text: item.title}), h('span', {class: 'count', text: `${item.count} bài`})))))
      : h('p', {class: 'no-hypothesis', text: 'Chưa có luật nào khớp quá nửa nhóm. Mở bài tiêu biểu để tự nhận định lỗi chung.'});
  const evidence = h('div', {class: 'evidence'},
    h('section', {class: 'block'}, h('h3', {text: 'Tỷ lệ trượt từng test'}), testBars(report, group)),
    (group.observations.length || group.rule) && h('div', {class: 'block-stack'},
      group.observations.length > 0 && h('section', {class: 'block'},
        h('h3', {text: 'Output lệch thế nào'}),
        h('ul', {class: 'observations'}, group.observations.map((o) => h('li', null,
          h('span', {text: o.text}), h('span', {class: 'count', text: `${o.count}/${o.size}`}))))),
      group.rule && ruleBlock(group.rule)),
    group.verified && verifiedBlock(group));
  return [head, teaching, evidence, membersBlock(source, report, group), noteBlock(source, report, group, onReviewSaved)];
}

function teachingCards(hypothesis) {
  return h('div', {class: 'teach'},
    h('section', {class: 'teach-card'}, h('h3', {text: 'Câu hỏi kiểm tra'}), h('p', {text: hypothesis.question})),
    h('section', {class: 'teach-card'}, h('h3', {text: 'Hoạt động dạy lại'}), h('p', {text: hypothesis.activity})));
}

function testBars(report, group) {
  const others = report.groups.filter((g) => g !== group);
  const otherSize = others.reduce((n, g) => n + g.size, 0);
  const list = h('ol', {class: 'test-bars'}, group.tests.map((row, i) => {
    const share = row.failing / row.size;
    const rest = otherSize ? others.reduce((n, g) => n + g.tests[i].failing, 0) / otherSize : null;
    const outcome = row.outcome && row.outcome !== 'fail' ? ` (${OUTCOME[row.outcome]?.text})` : '';
    const spoken = `${row.failing} trên ${row.size} bài trượt${outcome}` + (rest == null ? '' : `; các nhóm khác ${percent(rest)}`);
    return h('li', {class: 'test-bar', 'data-clear': String(row.failing === 0), title: `${row.name}: ${spoken}`},
      h('span', {class: 'name', text: row.name}),
      h('span', {class: 'track', 'aria-hidden': 'true'},
        h('span', {class: 'fill', vars: {'--w': percent(share)}}),
        rest != null && h('span', {class: 'mark', vars: {'--m': percent(rest)}})),
      h('span', {class: 'count', 'aria-hidden': 'true', text: row.failing ? `${row.failing}/${row.size}` : 'đạt'}),
      h('span', {class: 'sr-only', text: spoken}));
  }));
  return [list, otherSize > 0 && h('p', {class: 'legend', 'aria-hidden': 'true'},
    h('span', {class: 'legend-bar'}), 'nhóm này', h('span', {class: 'legend-mark'}), 'các nhóm khác')];
}

function ruleBlock(rule) {
  const lines = rule.conditions.flatMap((condition, i) => [
    h('span', {class: 'kw', text: i === 0 ? 'NẾU' : 'VÀ'}), h('span', {text: condition})]);
  return h('section', {class: 'block'},
    h('h3', {text: 'Luật NẾU–THÌ cho nhóm'}),
    h('div', {class: 'rule'}, lines, h('span', {class: 'kw', text: 'THÌ'}), h('span', {text: 'bài thuộc nhóm này'})),
    h('p', {class: 'rule-stats num', text: `Đúng với ${rule.support}/${rule.matched} bài khớp luật · bao ${rule.support}/${rule.size} bài của nhóm`}));
}

function verifiedBlock(group) {
  const verified = group.verified;
  return h('section', {class: 'block'},
    h('h3', {text: 'Nhãn kiểm chứng'}),
    h('p', {class: 'muted small', text: `${verified.labelled}/${group.size} bài có nhãn từ bản sửa của chính sinh viên`}),
    h('ul', {class: 'observations'}, Object.entries(verified.counts).map(([code, n]) => h('li', null,
      h('span', {text: verified.names[code] || code}), h('span', {class: 'count', text: String(n)})))));
}

const MEMBER_LIMIT = 12;

function membersBlock(source, report, group) {
  const names = group.verified?.names || {};
  const hypothesis = group.hypothesis;
  // A member's own rule is worth showing only when it disagrees with the group's hypothesis.
  const differs = (own) => own && (!hypothesis || (hypothesis.source === 'cpack_rule'
    ? own.category !== hypothesis.category : own.title !== hypothesis.title));
  const weight = (member) => (member.id === group.representative ? 0 : member.label ? 1 : differs(member.own) ? 2 : 3);
  const ordered = group.members.map((member, i) => [weight(member), i, member])
    .sort((a, b) => a[0] - b[0] || a[1] - b[1]).map(([, , member]) => member);
  const item = (member) => {
    const representative = member.id === group.representative;
    return h('li', null, h('button', {type: 'button', class: 'member', onclick: (event) => openSubmission(
      source, report.problem.id, member.id, {group, representative}, event.currentTarget)},
    h('span', {class: 'member-top'},
      h('span', {class: 'member-name', text: member.author || member.id}),
      h('span', {class: 'member-score', text: `${member.passed}/${member.total} test`})),
    h('span', {class: 'member-tags'},
      representative && tag('Tiêu biểu', 'accent'),
      differs(member.own) && tag(`Luật: ${member.own.title}`),
      member.label && tag(`Nhãn: ${names[member.label] || member.label}`))));
  };
  const list = h('ul', {class: 'members'}, ordered.slice(0, MEMBER_LIMIT).map(item));
  const more = ordered.length > MEMBER_LIMIT && h('button', {type: 'button', class: 'btn btn-quiet more-members',
    text: `Xem cả ${ordered.length} bài`, onclick: () => {
      list.append(...ordered.slice(MEMBER_LIMIT).map(item));
      more.remove();
      list.children[MEMBER_LIMIT]?.querySelector('button')?.focus();
    }});
  return h('section', {class: 'block'}, h('h3', {text: `Bài trong nhóm (${group.size})`}), list, more);
}

async function saveReview(source, report, group, change, onSaved) {
  const current = group.review || {status: 'open', note: ''};
  const next = {status: change.status ?? current.status, note: change.note ?? current.note ?? ''};
  try {
    group.review = await api('/api/review', {source, problem: report.problem.id, group: group.key, ...next});
    onSaved();
    toast(change.note === undefined ? `Đã lưu đánh giá nhóm ${group.index}.` : `Đã lưu ghi chú nhóm ${group.index}.`);
    return true;
  } catch (error) {
    toast(`Chưa lưu được: ${error.message}`, null, true);
    return false;
  }
}

function verdictControl(source, report, group, onSaved) {
  const name = `review-${group.index}`;
  const current = group.review?.status || 'open';
  const options = [['open', 'Chưa xem', null], ['confirmed', 'Đúng', 'check'], ['rejected', 'Không', 'cross']];
  const control = h('div', {class: 'verdict-control', role: 'radiogroup', 'aria-labelledby': `${name}-label`},
    h('span', {class: 'label', id: `${name}-label`, text: 'Cùng một lỗi?'}),
    h('div', {class: 'segmented'}, options.flatMap(([value, label, iconName]) => [
      h('input', {type: 'radio', name, id: `${name}-${value}`, value, checked: current === value,
        onchange: async () => {
          if (!await saveReview(source, report, group, {status: value}, onSaved)) {
            const back = control.querySelector(`input[value="${group.review?.status || 'open'}"]`);
            if (back) back.checked = true;
          }
        }}),
      h('label', {for: `${name}-${value}`}, iconName && icon(iconName), label)])));
  return control;
}

function noteBlock(source, report, group, onSaved) {
  const id = `note-${group.index}`;
  const existing = group.review?.note || '';
  const textarea = h('textarea', {id, maxlength: '2000', rows: '3', value: existing,
    placeholder: 'Ví dụ: chữa bài tiêu biểu trên bảng trong 10 phút'});
  const save = h('button', {type: 'submit', class: 'btn', text: 'Lưu ghi chú'});
  const form = h('form', {class: 'note-form', onsubmit: async (event) => {
    event.preventDefault();
    save.disabled = true;
    save.setAttribute('aria-busy', 'true');
    await saveReview(source, report, group, {note: textarea.value}, onSaved);
    save.disabled = false;
    save.removeAttribute('aria-busy');
  }},
  h('label', {class: 'sr-only', for: id, text: 'Ghi chú cho buổi dạy'}), textarea,
  h('div', {class: 'review-actions'}, save));
  return h('details', {class: 'note', open: Boolean(existing)},
    h('summary', null, icon('chevron', 'chev'), 'Ghi chú cho buổi dạy',
      existing && h('span', {class: 'muted small', text: '· đã có'})),
    form);
}

// ---------- submission sheet ----------

async function openSubmission(source, problemId, id, context, trigger) {
  lastTrigger = trigger;
  // The header stays in place while the body loads, so focus on the close button is never lost.
  const title = h('h2', {id: 'sheet-title', text: 'Bài nộp'});
  const score = h('p', {class: 'muted small num'});
  const close = h('button', {type: 'button', class: 'icon-btn', 'aria-label': 'Đóng', onclick: () => sheet.close()},
    icon('close'));
  let body = h('div', {class: 'sheet-body'}, loadingLine('Đang tải bài'));
  const where = `Nhóm ${context.group.index}${context.representative ? ' · bài tiêu biểu' : ''}`;
  sheet.replaceChildren(h('header', {class: 'sheet-head'},
    h('div', null, h('p', {class: 'panel-meta', text: where}), title, score), close), body);
  if (!sheet.open) sheet.showModal();
  close.focus();
  document.documentElement.style.setProperty('overflow', 'hidden');
  let next;
  try {
    const data = await api(`/api/submission?source=${source}&problem=${encodeURIComponent(problemId)}&id=${encodeURIComponent(id)}`);
    title.textContent = data.author || data.id;
    score.textContent = `${data.passed}/${data.total} test đạt`;
    next = sheetBody(data);
  } catch (error) {
    next = h('div', {class: 'sheet-body'}, errorNotice(error));
  }
  if (sheet.open && body.isConnected) {
    body.replaceWith(next);
    body = next;
  }
}

function sheetBody(data) {
  const failing = data.tests.filter((t) => t.outcome !== 'pass');
  const passing = data.tests.filter((t) => t.outcome === 'pass');
  const hypothesis = data.hypothesis;
  return h('div', {class: 'sheet-body'},
    (hypothesis || data.label_name) && h('div', {class: 'sheet-note'},
      hypothesis && h('p', null, h('b', {text: 'Giả thuyết cho bài này: '}), hypothesis.title),
      hypothesis && h('p', {class: 'muted small', text: SOURCE_LABEL[hypothesis.source]}),
      data.label_name && h('p', null, h('b', {text: 'Nhãn kiểm chứng: '}), data.label_name)),
    h('section', {class: 'block'}, h('h3', {text: 'Mã nguồn'}), codeView(data.code)),
    h('section', {class: 'block'},
      h('h3', {text: `Test không đạt (${failing.length})`}),
      h('div', {class: 'test-cases'}, failing.map(testCase)),
      passing.length > 0 && h('p', {class: 'passed-line', text: `Đạt: ${passing.map((t) => quoted(t.name)).join(', ')}`})));
}

function ioBox(label, text) {
  const empty = !text;
  return h('div', null, h('span', {class: 'label', text: label}),
    h('pre', {class: empty ? 'empty' : null, text: empty ? 'không in gì' : text.replace(/\n$/, '')}));
}

function testCase(test) {
  const meta = OUTCOME[test.outcome] || OUTCOME.not_run;
  return h('article', {class: 'case'},
    h('div', {class: 'case-head'}, statusIcon(test.outcome), h('strong', {text: test.name}),
      test.outcome !== 'fail' && h('span', {class: 'row-outcome', text: meta.text})),
    h('div', {class: 'io'}, ioBox('Input', test.input), ioBox('Cần in', test.expected), ioBox('Đã in', test.output)),
    test.observations.length > 0 && h('div', {class: 'case-notes'}, test.observations.map((o) => tag(o))));
}

sheet.addEventListener('click', (event) => { if (event.target === sheet) sheet.close(); });
sheet.addEventListener('close', () => {
  document.documentElement.style.removeProperty('overflow');
  if (lastTrigger?.isConnected) lastTrigger.focus();
});

// ---------- trial ----------

async function viewTrial(param, token) {
  const done = whileLoading(token, 'Đang tải bài tập');
  let listing;
  let problem;
  let runner;
  try {
    [listing, runner] = await Promise.all([cached('problems:class', () => api('/api/problems?source=class')), refreshRunner()]);
    const valid = (id) => id && listing.problems.some((p) => p.id === id);
    state.problem.trial = [param, state.problem.trial, storage.get('problem:trial')].find(valid) || listing.problems[0].id;
    problem = await cached(`problem:${state.problem.trial}`, () => api(`/api/problem?id=${state.problem.trial}`));
  } finally {
    done();
  }
  if (token !== renderToken) return;
  storage.set('problem:trial', problem.id);
  setHash('chay-thu', problem.id);

  const select = h('select', {id: 'trial-problem', onchange: (event) => {
    state.problem.trial = event.target.value;
    setHash('chay-thu', event.target.value);
    render();
  }}, listing.problems.map((p) => h('option', {value: p.id, text: p.title})));
  select.value = problem.id;
  const results = h('div', {class: 'results'});
  const draftKey = `draft:${problem.id}`;
  const editor = createEditor(storage.get(draftKey) ?? problem.starter, (code) => {
    if (code === problem.starter) storage.remove(draftKey);
    else storage.set(draftKey, code);
  }, () => run());
  const runButton = h('button', {type: 'button', class: 'btn btn-primary', onclick: () => run()},
    icon('play'), 'Chạy thử', h('kbd', {text: 'Ctrl ↵'}));
  const resetButton = h('button', {type: 'button', class: 'btn btn-quiet', onclick: () => {
    const previous = editor.value();
    if (previous === problem.starter) return;
    editor.set(problem.starter);
    toast('Đã đặt lại mã mẫu.', {label: 'Hoàn tác', run: () => editor.set(previous)});
  }}, icon('reset'), 'Mã mẫu');

  let running = false;
  async function run() {
    if (running) return;
    running = true;
    runButton.disabled = true;
    runButton.setAttribute('aria-busy', 'true');
    runButton.firstChild.replaceWith(h('span', {class: 'spinner', 'aria-hidden': 'true'}));
    results.replaceChildren(h('div', {class: 'card'}, loadingLine('Đang biên dịch và chạy 6 test trong Docker')));
    try {
      const result = await api('/api/run', {problem: problem.id, code: editor.value()});
      if (token !== renderToken) return;
      results.replaceChildren(...runResult(problem, result));
      announce(result.verdict === 'compile_error' ? 'Lỗi biên dịch.' : `Đã chạy xong: ${result.passed}/${result.total} test đạt.`);
    } catch (error) {
      if (token === renderToken) results.replaceChildren(errorNotice(error, () => run()));
      refreshRunner();
    } finally {
      running = false;
      runButton.disabled = false;
      runButton.removeAttribute('aria-busy');
      runButton.firstChild.replaceWith(icon('play'));
    }
  }

  results.replaceChildren(h('div', {class: 'card empty-state'},
    h('h2', {text: 'Chưa chạy'}),
    h('p', {class: 'muted', text: 'Kết quả từng test, giả thuyết lỗi và nút thêm bài vào lớp sẽ hiện ở đây.'})));
  show(token, page(
    h('header', {class: 'page-head'},
      h('div', null, h('h1', {text: 'Chạy thử'}),
        h('p', {class: 'lede', text: 'Chạy một bài C trong Docker cách ly, xem nó trượt test nào và có thể do lỗi gì, rồi thêm vào lớp để phân nhóm.'})),
      h('div', {class: 'controls'}, h('label', {class: 'field field-wide', for: select.id}, h('span', {text: 'Bài tập'}), select))),
    runner && !runner.ready && h('div', {class: 'notice notice-error', role: 'status'},
      h('h2', {text: 'Chưa chạy được code'}),
      h('p', {text: runner.message}),
      h('pre', {text: 'python scripts/setup_learning.py'})),
    h('div', {class: 'trial'},
      h('div', {class: 'trial-main'},
        problemCard(problem),
        h('section', {class: 'card editor-card', 'aria-label': 'Soạn mã'},
          h('div', {class: 'editor-bar'}, h('span', {class: 'file', text: 'main.c'}),
            h('div', {class: 'editor-actions'}, resetButton, runButton)),
          editor.element,
          h('p', {class: 'editor-hint', id: 'editor-hint', text: 'Tab thụt lề · Esc rồi Tab để rời ô soạn · Ctrl+Enter để chạy'}))),
      results)));
  editor.refresh();
}

function problemCard(problem) {
  return h('section', {class: 'card problem'},
    h('p', {class: 'panel-meta', text: problem.topic}),
    h('h2', {text: problem.title}),
    h('p', {text: problem.description}),
    h('p', {class: 'muted', text: problem.constraints}),
    h('div', {class: 'examples'}, problem.examples.map((example) => h('div', {class: 'example'},
      h('span', {class: 'muted', text: 'Input'}), h('pre', {text: example.input.replace(/\n$/, '')}),
      h('span', {class: 'muted', text: 'Cần in'}), h('pre', {text: example.expected.replace(/\n$/, '')})))));
}

function runResult(problem, result) {
  if (result.verdict === 'compile_error') {
    return [h('section', {class: 'card verdict', 'data-tone': 'warn'},
      h('span', {class: 'verdict-icon', 'aria-hidden': 'true'}, icon('alert')),
      h('h2', {text: 'Lỗi biên dịch'}),
      h('pre', {class: 'diagnostics', text: result.diagnostics || 'Trình biên dịch không trả về thông báo.'}),
      h('p', {class: 'muted small', text: 'Sửa lỗi theo dòng được chỉ ra rồi chạy lại.'}))];
  }
  const allPass = result.passed === result.total;
  const firstFail = result.tests.findIndex((t) => t.outcome !== 'pass');
  const rows = result.tests.map((test, i) => {
    const meta = OUTCOME[test.outcome] || OUTCOME.not_run;
    if (test.outcome === 'pass') {
      return h('li', {class: 'result-row'}, h('div', {class: 'row-line'}, statusIcon('pass'),
        h('span', {text: test.name}), h('span', {class: 'row-outcome', text: meta.text})));
    }
    return h('li', {class: 'result-row'}, h('details', {open: i === firstFail},
      h('summary', null, statusIcon(test.outcome), h('span', {text: test.name}),
        h('span', {class: 'row-outcome', text: meta.text}), icon('chevron', 'chev')),
      h('div', {class: 'result-body'},
        h('div', {class: 'io'}, ioBox('Input', test.input), ioBox('Cần in', test.expected), ioBox('Đã in', test.output)),
        test.observations.length > 0 && h('div', {class: 'case-notes'}, test.observations.map((o) => tag(o))))));
  });
  const hypothesis = result.hypothesis;
  return [
    h('section', {class: 'card verdict', 'data-tone': allPass ? 'pass' : 'fail'},
      h('span', {class: 'verdict-icon', 'aria-hidden': 'true'}, icon(allPass ? 'check' : 'cross')),
      h('h2', {class: 'num', text: allPass ? `Đạt cả ${result.total} test` : `${result.passed}/${result.total} test đạt`})),
    h('section', {class: 'card', 'aria-label': 'Kết quả từng test'}, h('ul', {class: 'result-list'}, rows)),
    !allPass && (hypothesis ? h('section', {class: 'card hypothesis-card'},
      h('p', {class: 'hypothesis-line'}, tag(SOURCE_LABEL[hypothesis.source], 'accent'),
        hypothesis.source !== 'cpack_rule' && h('span', {text: `loại lỗi: ${hypothesis.family}`})),
      h('h3', {text: hypothesis.title}),
      hypothesis.statement && h('p', {class: 'statement', text: hypothesis.statement}),
      teachingCards(hypothesis))
      : h('p', {class: 'card no-hypothesis', text: 'Chưa có luật nào khớp bài này; nhóm lỗi sẽ rõ hơn khi phân tích cùng cả lớp.'})),
    result.run_id && addForm(problem, result.run_id),
  ];
}

function addForm(problem, runId) {
  const input = h('input', {type: 'text', id: 'add-author', maxlength: '60', autocomplete: 'off',
    placeholder: 'Ví dụ: Nguyễn An'});
  const error = h('p', {class: 'small', id: 'add-error', role: 'alert'});
  const submit = h('button', {type: 'submit', class: 'btn', text: 'Thêm vào lớp'});
  const form = h('form', {class: 'card add-form', onsubmit: async (event) => {
    event.preventDefault();
    const author = input.value.trim();
    if (!author) {
      error.textContent = 'Nhập tên hiển thị để thêm bài vào lớp.';
      input.setAttribute('aria-invalid', 'true');
      input.setAttribute('aria-describedby', error.id);
      input.focus();
      return;
    }
    submit.disabled = true;
    submit.setAttribute('aria-busy', 'true');
    try {
      await api('/api/class/add', {run_id: runId, author});
      forget('problems:class');
      forget(`analysis:class:${problem.id}:`);
      const link = `#/lop/${encodeURIComponent(problem.id)}`;
      form.replaceChildren(h('p', null, `Đã thêm bài của ${author} vào lớp. `, h('a', {href: link, text: 'Xem nhóm lỗi của bài này'})));
      toast(`Đã thêm bài của ${author} vào lớp.`, {label: 'Xem nhóm lỗi', href: link});
    } catch (failure) {
      error.textContent = failure.message;
      submit.disabled = false;
      submit.removeAttribute('aria-busy');
    }
  }},
  h('h3', {class: 'section-title', text: 'Thêm vào lớp'}),
  h('p', {class: 'muted small', text: 'Bài này sẽ là bài mới nhất của tên bạn nhập và được tính khi phân tích Lớp học.'}),
  h('label', {class: 'label', for: input.id, text: 'Tên hiển thị'}),
  h('div', {class: 'add-row'}, input, submit), error);
  input.addEventListener('input', () => {
    input.removeAttribute('aria-invalid');
    error.textContent = '';
  });
  return form;
}

function createEditor(initial, onChange, onRun) {
  const gutter = h('div', {class: 'gutter', 'aria-hidden': 'true'});
  const code = h('code');
  const layer = h('pre', {class: 'editor-highlight', 'aria-hidden': 'true'}, code);
  const input = h('textarea', {class: 'editor-input', spellcheck: 'false', autocapitalize: 'off', autocomplete: 'off',
    autocorrect: 'off', wrap: 'off', 'aria-label': 'Mã nguồn C', 'aria-describedby': 'editor-hint', value: initial});
  let leaving = false;
  let lines = 0;

  const scroll = () => {
    layer.scrollTop = input.scrollTop;
    layer.scrollLeft = input.scrollLeft;
    gutter.scrollTop = input.scrollTop;
  };
  const refresh = () => {
    code.innerHTML = `${highlight(input.value)}\n`;
    const next = input.value.split('\n').length;
    if (next !== lines) {
      lines = next;
      gutter.textContent = `${lineNumbers(input.value)}\n`;
    }
    scroll();
  };
  const insert = (text) => {
    input.focus();
    if (!document.execCommand('insertText', false, text)) {
      input.setRangeText(text, input.selectionStart, input.selectionEnd, 'end');
      input.dispatchEvent(new Event('input'));
    }
  };
  input.addEventListener('input', () => { refresh(); onChange(input.value); });
  input.addEventListener('scroll', scroll);
  input.addEventListener('keydown', (event) => {
    if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
      event.preventDefault();
      onRun();
      return;
    }
    if (event.key === 'Escape') {
      leaving = true;
      return;
    }
    if (event.key === 'Tab' && !leaving && !event.ctrlKey && !event.altKey && !event.metaKey) {
      event.preventDefault();
      const start = input.value.lastIndexOf('\n', input.selectionStart - 1) + 1;
      if (!event.shiftKey) {
        insert('    ');
      } else {
        const spaces = /^ {1,4}/.exec(input.value.slice(start))?.[0].length || 0;
        if (spaces) {
          const caret = input.selectionStart;
          input.setSelectionRange(start, start + spaces);
          insert('');
          input.setSelectionRange(Math.max(start, caret - spaces), Math.max(start, caret - spaces));
        }
      }
      return;
    }
    leaving = false;
    if (event.key === 'Enter' && !event.shiftKey && !event.altKey && input.selectionStart === input.selectionEnd) {
      event.preventDefault();
      const before = input.value.slice(0, input.selectionStart);
      const indent = /^[ \t]*/.exec(before.slice(before.lastIndexOf('\n') + 1))[0];
      insert(`\n${indent}${/\{\s*$/.test(before) ? '    ' : ''}`);
    }
  });
  input.addEventListener('blur', () => { leaving = false; });
  return {
    element: h('div', {class: 'editor'}, gutter, h('div', {class: 'editor-area'}, layer, input)),
    value: () => input.value,
    set: (text) => {
      input.value = text;
      refresh();
      onChange(text);
    },
    refresh,
  };
}

// ---------- study ----------

async function viewStudy(_param, token) {
  const done = whileLoading(token, 'Đang tải kết quả nghiên cứu');
  let data;
  try {
    data = await cached('study', () => api('/api/study'));
  } finally {
    done();
  }
  if (token !== renderToken) return;
  const papers = [['en', 'Bài báo tiếng Anh (PDF)'], ['vi', 'Bản tiếng Việt (PDF)']].filter(([lang]) => data.papers[lang]);
  const bounds = [data.ari.real, data.ari.injected].flatMap((ari) => ari.rows.flatMap((row) => [row.low, row.high]));
  const domain = [Math.floor(Math.min(0, ...bounds) * 5) / 5, Math.ceil(Math.max(...bounds) * 5) / 5];
  const topRules = data.rules.slice(0, 6);
  const moreRules = data.rules.slice(6);
  show(token, h('div', {class: 'page study'},
    h('header', {class: 'study-head'},
      h('p', {class: 'eyebrow', text: 'Câu hỏi nghiên cứu'}),
      h('h1', {text: data.question}),
      h('p', {class: 'answer', text: data.answer}),
      h('p', {class: 'collision'}, 'Trong các cặp bài có cùng chữ ký test, ',
        h('strong', {class: 'num', text: `${Math.round(data.collisions.real)}%`}), ' ở dữ liệu thật và ',
        h('strong', {class: 'num', text: `${Math.round(data.collisions.injected)}%`}), ' ở dữ liệu tiêm lỗi thực ra khác cơ chế lỗi.'),
      papers.length > 0 && h('div', {class: 'papers'}, papers.map(([lang, label]) =>
        h('a', {class: 'btn', href: `/paper/${lang}.pdf`, target: '_blank', rel: 'noopener'}, label, icon('external'))))),
    h('section', {class: 'tiles', 'aria-label': 'Dữ liệu'}, data.data.map((tile) => h('div', {class: 'card tile'},
      h('span', {class: 'tile-value', text: count(tile.value)}),
      h('span', {class: 'tile-label', text: tile.label}),
      h('span', {class: 'tile-detail', text: tile.detail})))),
    h('section', {class: 'study-section'},
      h('h2', {text: 'Giả thuyết và kết quả'}),
      h('p', {class: 'lede', text: 'Trung bình trên các nhóm bài của tập kiểm tra niêm phong, kèm khoảng tin cậy bootstrap 95%. Ủng hộ khi cả khoảng nằm về phía giả thuyết.'}),
      hypothesisList(data.hypotheses)),
    h('section', {class: 'study-section'},
      h('h2', {text: 'Độ khớp cụm với cơ chế lỗi'}),
      h('p', {class: 'lede', text: 'ARI giữa cụm K-means và nhãn cơ chế; 0 là ngẫu nhiên, 1 là khớp hoàn toàn. Đường ngang là khoảng tin cậy 95%.'}),
      h('div', {class: 'charts'},
        dotPlot('Dữ liệu thật', data.ari.real, domain),
        dotPlot('Dữ liệu tiêm lỗi', data.ari.injected, domain))),
    h('section', {class: 'study-section'},
      h('h2', {text: 'Luật NẾU–THÌ học được (ILA-2)'}),
      h('p', {class: 'lede', text: `Học trên bản sửa của sinh viên ở tập huấn luyện; ${data.rules.length} luật, sắp theo số bài đúng.`}),
      rulesTable(topRules),
      moreRules.length > 0 && h('details', {class: 'more'}, h('summary', null, `Xem thêm ${moreRules.length} luật`), rulesTable(moreRules)),
      h('div', {class: 'metrics'},
        h('h3', {class: 'section-title', text: 'Macro-F1 của luật trên sinh viên ở tập kiểm tra'}),
        h('dl', null, [
          ['Dữ liệu thật', data.rule_quality.real_seen],
          ['Tiêm lỗi', data.rule_quality.injected_seen],
          ['Tiêm lỗi, bài chưa gặp khi học luật', data.rule_quality.injected_unseen],
          ['Tiêm lỗi, luật chỉ dùng kết quả test', data.rule_quality.injected_outcome_only],
        ].map(([label, value]) => h('div', {class: 'card metric'},
          h('dt', {text: label}), h('dd', {class: 'num', text: decimal(value)})))))),
    h('section', {class: 'study-section'},
      h('h2', {text: 'Giới hạn'}),
      h('ul', {class: 'limits'}, data.limits.map((limit) => h('li', {text: limit}))))));
}

function resultBox(label, result) {
  return h('dl', {class: 'hyp-result'}, h('dt', {text: label}), result
    ? h('dd', null,
      h('span', {class: 'hyp-mean num', text: decimal(result.mean)}),
      h('span', {class: 'ci', text: `${decimal(result.low)} – ${decimal(result.high)}`}),
      result.supported ? tag('Ủng hộ', 'pass', 'check') : tag('Chưa ủng hộ', null, 'minus'))
    : h('dd', {class: 'muted'}, h('span', {'aria-hidden': 'true', text: '—'}), h('span', {class: 'sr-only', text: 'không đo'})));
}

function hypothesisList(hypotheses) {
  return h('div', {class: 'card hyp-card'},
    h('div', {class: 'hyp hyp-head', 'aria-hidden': 'true'},
      h('span', {text: 'Giả thuyết'}), h('span', {text: 'Dữ liệu thật'}), h('span', {text: 'Tiêm lỗi'})),
    h('ol', {class: 'hyp-list'}, hypotheses.map((item) => h('li', {class: 'hyp'},
      h('div', {class: 'hyp-text'},
        h('span', {class: 'hyp-id', text: item.id}),
        h('p', {class: 'hyp-statement', text: item.statement}),
        h('p', {class: 'muted small', text: `Đo bằng: ${lowerFirst(item.measure)}`})),
      resultBox('Dữ liệu thật', item.real),
      resultBox('Tiêm lỗi', item.injected)))));
}

const lowerFirst = (text) => text.charAt(0).toLowerCase() + text.slice(1);

function rulesTable(rules) {
  return h('div', {class: 'table-wrap'}, h('table', null,
    h('thead', null, h('tr', null, ['NẾU', 'THÌ loại lỗi', 'Đúng / khớp'].map((label) => h('th', {scope: 'col', text: label})))),
    h('tbody', null, rules.map((rule) => h('tr', null,
      h('td', {text: rule.if.join(' và ')}),
      h('td', {text: rule.then}),
      h('td', {class: 'num', text: `${rule.support}/${rule.matched}`}))))));
}

function dotPlot(title, ari, [min, max]) {
  const x = (value) => `${((value - min) / (max - min)) * 100}%`;
  const ticks = [];
  for (let i = Math.round(min * 5); i <= Math.round(max * 5); i += 1) ticks.push(i / 5);
  return h('figure', {class: 'card chart'},
    h('figcaption', null, h('h3', {text: title}), h('p', {class: 'chart-note', text: `${ari.cohorts} nhóm bài`})),
    h('div', {class: 'dotplot'},
      ari.rows.map((row) => h('div', {class: row.proposed ? 'dp-row proposed' : 'dp-row',
        title: `${row.name}: ${decimal(row.mean)} (95%: ${decimal(row.low)} – ${decimal(row.high)})`},
      h('span', {class: 'dp-label', text: row.name}),
      h('span', {class: 'dp-track', 'aria-hidden': 'true'},
        h('span', {class: 'dp-zero', vars: {'--x': x(0)}}),
        h('span', {class: 'dp-ci', vars: {'--a': x(row.low), '--b': x(row.high)}}),
        h('span', {class: 'dp-dot', vars: {'--x': x(row.mean)}})),
      h('span', {class: 'dp-value num', text: decimal(row.mean)}),
      h('span', {class: 'sr-only', text: `, khoảng tin cậy ${decimal(row.low)} đến ${decimal(row.high)}`}))),
      h('div', {class: 'dp-row dp-axis', 'aria-hidden': 'true'}, h('span'),
        h('span', {class: 'dp-ticks'}, ticks.map((t) => h('span', {vars: {'--x': x(t)}, text: decimal(t, 1)}))),
        h('span'))));
}

// ---------- start ----------

window.addEventListener('hashchange', render);
refreshRunner();
render();
