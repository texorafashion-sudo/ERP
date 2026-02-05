// Upcoming Jobs Alert & Job Status Manager
// This script handles all app behavior: form input, filtering, sorting, dashboard stats,
// localStorage persistence, status updates, and optional dark mode.

const STORAGE_KEY = "jobsManager.jobs";
const THEME_KEY = "jobsManager.theme";

const state = {
  jobs: [],
  filters: {
    search: "",
    status: "All",
    priority: "All",
  },
};

const elements = {
  form: document.getElementById("jobForm"),
  activeJobs: document.getElementById("activeJobs"),
  completedJobsList: document.getElementById("completedJobsList"),
  template: document.getElementById("jobCardTemplate"),
  notificationBanner: document.getElementById("notificationBanner"),
  darkModeToggle: document.getElementById("darkModeToggle"),

  searchInput: document.getElementById("searchInput"),
  statusFilter: document.getElementById("statusFilter"),
  priorityFilter: document.getElementById("priorityFilter"),

  totalJobs: document.getElementById("totalJobs"),
  pendingJobs: document.getElementById("pendingJobs"),
  inProgressJobs: document.getElementById("inProgressJobs"),
  completedJobs: document.getElementById("completedJobs"),
  completionText: document.getElementById("completionText"),
  progressBar: document.getElementById("progressBar"),
};

function init() {
  loadJobs();
  loadTheme();
  bindEvents();
  render();
}

function bindEvents() {
  elements.form.addEventListener("submit", handleAddJob);
  elements.searchInput.addEventListener("input", (event) => {
    state.filters.search = event.target.value.trim().toLowerCase();
    render();
  });

  elements.statusFilter.addEventListener("change", (event) => {
    state.filters.status = event.target.value;
    render();
  });

  elements.priorityFilter.addEventListener("change", (event) => {
    state.filters.priority = event.target.value;
    render();
  });

  elements.darkModeToggle.addEventListener("click", toggleDarkMode);
}

function handleAddJob(event) {
  event.preventDefault();

  const formData = new FormData(elements.form);
  const job = {
    id: crypto.randomUUID(),
    jobName: formData.get("jobName").trim(),
    clientName: formData.get("clientName").trim(),
    jobType: formData.get("jobType").trim(),
    startDate: formData.get("startDate"),
    dueDate: formData.get("dueDate"),
    priority: formData.get("priority"),
    status: formData.get("status"),
    notes: formData.get("notes").trim(),
  };

  // Lightweight validation to keep beginner-friendly behavior obvious.
  if (!job.jobName || !job.clientName || !job.jobType || !job.startDate || !job.dueDate) {
    alert("Please fill in all required fields.");
    return;
  }

  if (new Date(job.dueDate) < new Date(job.startDate)) {
    alert("Due date cannot be before start date.");
    return;
  }

  state.jobs.push(job);
  saveJobs();
  elements.form.reset();
  render();
}

function loadJobs() {
  try {
    const parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    state.jobs = Array.isArray(parsed) ? parsed : [];
  } catch (error) {
    state.jobs = [];
    console.error("Could not load jobs from localStorage", error);
  }
}

function saveJobs() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.jobs));
}

function getSortedJobs(jobs) {
  return [...jobs].sort((a, b) => new Date(a.dueDate) - new Date(b.dueDate));
}

function getFilteredJobs() {
  return state.jobs.filter((job) => {
    const matchesSearch =
      !state.filters.search ||
      job.jobName.toLowerCase().includes(state.filters.search) ||
      job.clientName.toLowerCase().includes(state.filters.search);

    const matchesStatus = state.filters.status === "All" || job.status === state.filters.status;
    const matchesPriority = state.filters.priority === "All" || job.priority === state.filters.priority;

    return matchesSearch && matchesStatus && matchesPriority;
  });
}

function render() {
  const filtered = getFilteredJobs();
  const sorted = getSortedJobs(filtered);

  const activeJobs = sorted.filter((job) => job.status !== "Completed");
  const completedJobs = sorted.filter((job) => job.status === "Completed");

  renderJobs(activeJobs, elements.activeJobs);
  renderJobs(completedJobs, elements.completedJobsList);
  renderStats();
  renderNotificationBanner();
}

function renderJobs(jobs, container) {
  container.innerHTML = "";

  if (jobs.length === 0) {
    container.innerHTML = '<p class="muted">No jobs match your current view.</p>';
    return;
  }

  jobs.forEach((job) => {
    const fragment = elements.template.content.cloneNode(true);
    const card = fragment.querySelector(".job-card");

    fragment.querySelector(".job-title").textContent = job.jobName;
    fragment.querySelector(".job-client").textContent = `Client: ${job.clientName}`;
    fragment.querySelector(".job-type").textContent = job.jobType;
    fragment.querySelector(".job-start").textContent = formatDate(job.startDate);
    fragment.querySelector(".job-due").textContent = formatDate(job.dueDate);
    fragment.querySelector(".job-notes").textContent = job.notes || "No notes added.";

    const statusSelect = fragment.querySelector(".status-select");
    statusSelect.value = job.status;
    statusSelect.addEventListener("change", (event) => {
      updateJobStatus(job.id, event.target.value, card);
    });

    const deleteButton = fragment.querySelector(".delete-btn");
    deleteButton.addEventListener("click", () => {
      deleteJob(job.id);
    });

    const badges = fragment.querySelector(".badges");
    badges.appendChild(createBadge(`Priority: ${job.priority}`, `priority-${job.priority.toLowerCase()}`));
    badges.appendChild(createBadge(job.status, statusToClass(job.status)));

    const dueInfo = getDueLabel(job.dueDate, job.status);
    badges.appendChild(createBadge(dueInfo.label, dueInfo.className));

    container.appendChild(fragment);
  });
}

function createBadge(text, className) {
  const badge = document.createElement("span");
  badge.className = `badge ${className}`;
  badge.textContent = text;
  return badge;
}

function updateJobStatus(id, status, cardElement) {
  const job = state.jobs.find((item) => item.id === id);
  if (!job) return;

  job.status = status;
  saveJobs();

  if (cardElement) {
    cardElement.classList.add("status-change");
    setTimeout(() => cardElement.classList.remove("status-change"), 450);
  }

  render();
}

function deleteJob(id) {
  state.jobs = state.jobs.filter((job) => job.id !== id);
  saveJobs();
  render();
}

function renderStats() {
  const total = state.jobs.length;
  const pending = state.jobs.filter((job) => job.status === "Pending").length;
  const inProgress = state.jobs.filter((job) => job.status === "In Progress").length;
  const completed = state.jobs.filter((job) => job.status === "Completed").length;
  const completedPercent = total === 0 ? 0 : Math.round((completed / total) * 100);

  elements.totalJobs.textContent = String(total);
  elements.pendingJobs.textContent = String(pending);
  elements.inProgressJobs.textContent = String(inProgress);
  elements.completedJobs.textContent = String(completed);

  elements.completionText.textContent = `${completed} of ${total} jobs completed (${completedPercent}%)`;
  elements.progressBar.style.width = `${completedPercent}%`;

  const progressTrack = elements.progressBar.parentElement;
  progressTrack.setAttribute("aria-valuenow", String(completedPercent));
}

function renderNotificationBanner() {
  const upcomingCount = state.jobs.filter((job) => {
    const dueStatus = classifyDueDate(job.dueDate);
    return job.status !== "Completed" && (dueStatus === "today" || dueStatus === "tomorrow" || dueStatus === "within7");
  }).length;

  if (upcomingCount > 0) {
    elements.notificationBanner.classList.remove("hidden");
    elements.notificationBanner.textContent = `🔔 ${upcomingCount} upcoming job${
      upcomingCount > 1 ? "s are" : " is"
    } due in the next 7 days.`;
  } else {
    elements.notificationBanner.classList.add("hidden");
    elements.notificationBanner.textContent = "";
  }
}

function classifyDueDate(dueDate) {
  const oneDay = 24 * 60 * 60 * 1000;
  const today = startOfDay(new Date());
  const due = startOfDay(new Date(dueDate));
  const diffDays = Math.round((due - today) / oneDay);

  if (diffDays < 0) return "overdue";
  if (diffDays === 0) return "today";
  if (diffDays === 1) return "tomorrow";
  if (diffDays <= 7) return "within7";
  return "later";
}

function getDueLabel(dueDate, status) {
  if (status === "Completed") {
    return { label: "Completed", className: "completed" };
  }

  const dueClass = classifyDueDate(dueDate);
  switch (dueClass) {
    case "overdue":
      return { label: "Overdue", className: "overdue" };
    case "today":
      return { label: "Due Today", className: "due-soon" };
    case "tomorrow":
      return { label: "Due Tomorrow", className: "due-soon" };
    case "within7":
      return { label: "Due within 7 days", className: "normal" };
    default:
      return { label: "Upcoming", className: "normal" };
  }
}

function statusToClass(status) {
  if (status === "Completed") return "completed";
  if (status === "In Progress") return "in-progress";
  return "normal";
}

function formatDate(value) {
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? "-" : date.toLocaleDateString();
}

function startOfDay(date) {
  const copy = new Date(date);
  copy.setHours(0, 0, 0, 0);
  return copy;
}

function loadTheme() {
  const savedTheme = localStorage.getItem(THEME_KEY);
  if (savedTheme === "dark") {
    document.body.classList.add("dark");
    elements.darkModeToggle.textContent = "☀️ Light Mode";
  }
}

function toggleDarkMode() {
  const isDark = document.body.classList.toggle("dark");
  localStorage.setItem(THEME_KEY, isDark ? "dark" : "light");
  elements.darkModeToggle.textContent = isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
}

init();
