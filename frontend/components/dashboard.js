const toggle = document.getElementById("themeToggle");
const body = document.body;

const storedTheme = localStorage.getItem("theme");
if (storedTheme === "dark") {
  body.classList.add("dark");
  toggle.textContent = "Light Mode";
}

toggle.addEventListener("click", () => {
  body.classList.toggle("dark");
  const isDark = body.classList.contains("dark");
  toggle.textContent = isDark ? "Light Mode" : "Dark Mode";
  localStorage.setItem("theme", isDark ? "dark" : "light");
});

const ctx = document.getElementById("productionChart");
if (ctx) {
  new Chart(ctx, {
    type: "line",
    data: {
      labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
      datasets: [
        {
          label: "Planned",
          data: [120, 130, 125, 140, 150, 160],
          borderColor: "#2563eb",
          backgroundColor: "rgba(37, 99, 235, 0.15)",
          tension: 0.35,
          fill: true,
        },
        {
          label: "Actual",
          data: [110, 128, 120, 134, 148, 155],
          borderColor: "#22c55e",
          backgroundColor: "rgba(34, 197, 94, 0.15)",
          tension: 0.35,
          fill: true,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
        },
      },
      scales: {
        y: {
          ticks: {
            callback: (value) => `${value} units`,
          },
        },
      },
    },
  });
}
