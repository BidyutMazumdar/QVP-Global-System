fetch("/qssi/rankings")
  .then(res => {
    if (!res.ok) {
      throw new Error("API error");
    }
    return res.json();
  })
  .then(data => {

    const rows = data && data.data ? data.data : [];

    if (!rows || rows.length === 0) {
      document.body.innerHTML = "<h2>No Data Available</h2>";
      return;
    }

    const leader = rows[0];
    document.getElementById("leader").innerHTML =
      `<h3>${leader.Country}</h3>
       <p>Score: ${leader.Score}</p>
       <p>${leader.Tier}</p>`;

    const top10 = document.getElementById("top10");
    if (top10) top10.innerHTML = "";  // 🔒 FIX

    rows.slice(0,10).forEach(r => {
      const li = document.createElement("li");
      li.textContent = `${r.Rank}. ${r.Country} (${r.Score})`;
      top10.appendChild(li);
    });

    const table = document.getElementById("table");
    if (!table) return;

    table.innerHTML = "";

    rows.forEach(r => {
      const tr = document.createElement("tr");

      tr.innerHTML = `
        <td>${r.Rank}</td>
        <td>${r.Country}</td>
        <td>${r.QSSI_scaled ?? "-"}</td>
        <td>${r.QSSI_adj ?? "-"}</td>
        <td>${r.Score ?? "-"}</td>
        <td class="${(r.Tier || "").replace(' ', '')}">${r.Tier || "-"}</td>
      `;

      table.appendChild(tr);
    });

  })
  .catch(err => {
    console.error(err);
    document.body.innerHTML = "<h2>Error loading data</h2>";
  });
