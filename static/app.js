const API_URL = "/rankings";

let controller = null;

async function loadData() {
  const loading = document?.getElementById("loading");

  // cancel previous request
  if (controller) controller.abort();
  controller = new AbortController();

  let timeout;

  try {
    // timeout protection
    timeout = setTimeout(() => controller.abort(), 8000);

    const res = await fetch(API_URL, {
      cache: "no-store",
      signal: controller.signal
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const data = await res.json();

    if (loading) loading.style.display = "none";

    const rows = Array.isArray(data?.data) ? data.data : [];

    if (rows.length === 0) {
      if (loading) {
        loading.style.display = "block";
        loading.innerText = "No Data Available";
      }
      return;
    }

    const leaderEl = document?.getElementById("leader");
    if (leaderEl) {
      const leader = rows[0];
      leaderEl.innerHTML = `
        <h3>${leader.Country ?? "-"}</h3>
        <p>Score: ${leader.Score ?? "-"}</p>
        <p>${leader.Tier ?? "-"}</p>
      `;
    }

    const top10 = document?.getElementById("top10");
    if (top10) {
      top10.innerHTML = "";

      rows.slice(0, 10).forEach(r => {
        const li = document.createElement("li");
        li.textContent = `${r.Rank ?? "-"} . ${r.Country ?? "-"} (${r.Score ?? "-"})`;
        top10.appendChild(li);
      });
    }

    const table = document?.getElementById("table");
    if (table) {
      table.innerHTML = "";

      rows.forEach(r => {
        const tr = document.createElement("tr");

        tr.innerHTML = `
          <td>${r.Rank ?? "-"}</td>
          <td>${r.Country ?? "-"}</td>
          <td>${r.QSSI_scaled ?? "-"}</td>
          <td>${r.QSSI_adj ?? "-"}</td>
          <td>${r.Score ?? "-"}</td>
          <td>${r.Tier ?? "-"}</td>
        `;

        table.appendChild(tr);
      });
    }

  } catch (err) {
    console.error("Frontend error:", err);

    if (err.name === "AbortError") return;

    if (loading) {
      loading.style.display = "block";
      loading.innerText = "⚠️ Failed to load data";
      loading.style.color = "red";
    }

  } finally {
    if (timeout) clearTimeout(timeout);
    controller = null;
  }
}

document.addEventListener("DOMContentLoaded", loadData);
