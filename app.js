const $ = (selector) => document.querySelector(selector);

const complexityLabels = {
  constant: "O(1)",
  logarithmic: "O(log n)",
  linear: "O(n)",
  linearithmic: "O(n log n)",
  quadratic: "O(n²)",
};

async function loadTopics() {
  const data = await fetch("/api/topics").then(r => r.json());
  $("#topicGrid").innerHTML = data.map(item => `
    <article class="card topic-card" tabindex="0">
      <div class="topic-top">
        <span class="topic-icon">${item.icon}</span>
        <span class="topic-level">${item.level.toUpperCase()}</span>
      </div>
      <h3>${item.title}</h3>
      <p>${item.description}</p>
      <div class="topic-details">
        <p><strong>Why it matters:</strong> ${item.why}</p>
        <ul>${item.topics.map(t => `<li>${t}</li>`).join("")}</ul>
      </div>
    </article>
  `).join("");

  document.querySelectorAll(".topic-card").forEach(card => {
    const toggle = () => card.classList.toggle("open");
    card.addEventListener("click", toggle);
    card.addEventListener("keydown", e => { if (e.key === "Enter") toggle(); });
  });
}

async function updateComplexity() {
  const kind = $("#complexityKind").value;
  const n = $("#nRange").value;
  $("#nValue").textContent = n;

  const data = await fetch(`/api/complexity?kind=${kind}&n=${n}`).then(r => r.json());
  $("#complexityResult").textContent = `${complexityLabels[kind]} → ${data.operations.toLocaleString()} ops`;

  const max = Math.max(...data.series.map(x => x.operations));
  $("#growthBars").innerHTML = data.series.map(point => {
    const height = Math.max(4, Math.round((point.operations / max) * 190));
    return `<div class="bar-col">
      <div class="bar" style="height:${height}px" title="${point.operations} operations"></div>
      n=${point.n}
    </div>`;
  }).join("");
}

async function traceRecursion() {
  const value = $("#factorialInput").value;
  const response = await fetch(`/api/recursion/factorial?value=${value}`);
  const data = await response.json();
  if (!response.ok) {
    $("#stackOutput").innerHTML = `<div class="stack-row">${data.error}</div>`;
    return;
  }

  $("#stackOutput").innerHTML = data.events.map(event => {
    const indent = event.depth * 18;
    return `<div class="stack-row ${event.type}" style="margin-left:${indent}px">
      ${event.type.toUpperCase()} · ${event.label}
    </div>`;
  }).join("");
}

async function runReferenceDemo() {
  const data = await fetch("/api/reference-demo").then(r => r.json());
  $("#referenceOutput").textContent =
`original = ${JSON.stringify(data.original)}
alias    = ${JSON.stringify(data.alias)}
copied   = ${JSON.stringify(data.copied)}

original is alias  → ${data.same_object_original_alias}
original is copied → ${data.same_object_original_copy}

${data.explanation}`;
}

let builtinData = [];
async function loadBuiltins() {
  builtinData = await fetch("/api/builtins").then(r => r.json());
  renderBuiltins("");
}
function renderBuiltins(filter) {
  const q = filter.toLowerCase().trim();
  const rows = builtinData.filter(x => JSON.stringify(x).toLowerCase().includes(q));
  $("#builtinRows").innerHTML = rows.map(row => `
    <tr><td>${row.structure}</td><td>${row.operation}</td><td>${row.average}</td><td>${row.note}</td></tr>
  `).join("");
}

async function runTwoPointer() {
  const values = $("#pairValues").value.split(",").map(x => x.trim()).filter(Boolean);
  const target = $("#pairTarget").value;
  const response = await fetch("/api/two-pointer", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({values, target})
  });
  const data = await response.json();
  if (!response.ok) {
    $("#pairOutput").innerHTML = `<div class="step-item">${data.error}</div>`;
    return;
  }

  const steps = data.steps.map((s, i) =>
    `<div class="step-item ${s.sum == target ? "success" : ""}">
      Step ${i + 1}: left=${s.a}, right=${s.b} → sum=${s.sum}
    </div>`
  ).join("");
  const result = data.found
    ? `<div class="step-item success">✓ Found pair [${data.pair.join(", ")}]</div>`
    : `<div class="step-item">No pair found.</div>`;
  $("#pairOutput").innerHTML = steps + result;
}

async function submitQuiz(event) {
  event.preventDefault();
  const form = new FormData(event.currentTarget);
  const answers = Object.fromEntries(form.entries());
  const data = await fetch("/api/quiz/check", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({answers})
  }).then(r => r.json());

  $("#scoreDisplay").textContent = `${data.score} / ${data.total}`;
  const messages = [
    "Start with the roadmap and revisit each lab.",
    "Good start — strengthen the core mental models.",
    "You have momentum. Review the weak spots.",
    "Solid foundation. Keep practicing edge cases.",
    "Very strong prerequisite readiness.",
    "Foundation unlocked — ready to move deeper into DSA."
  ];
  $("#scoreMessage").textContent = messages[data.score];
  localStorage.setItem("dsaPrereqScore", String(data.score));
}

function restoreState() {
  const theme = localStorage.getItem("dsaTheme");
  if (theme === "light") document.body.classList.add("light");
  const score = localStorage.getItem("dsaPrereqScore");
  if (score !== null) {
    $("#scoreDisplay").textContent = `${score} / 5`;
    $("#scoreMessage").textContent = "Saved from your previous visit.";
  }
}

$("#themeToggle").addEventListener("click", () => {
  document.body.classList.toggle("light");
  localStorage.setItem("dsaTheme", document.body.classList.contains("light") ? "light" : "dark");
});
$("#complexityKind").addEventListener("change", updateComplexity);
$("#nRange").addEventListener("input", updateComplexity);
$("#runRecursion").addEventListener("click", traceRecursion);
$("#runReference").addEventListener("click", runReferenceDemo);
$("#builtinSearch").addEventListener("input", e => renderBuiltins(e.target.value));
$("#runPair").addEventListener("click", runTwoPointer);
$("#quizForm").addEventListener("submit", submitQuiz);

restoreState();
loadTopics();
loadBuiltins();
updateComplexity();
traceRecursion();
