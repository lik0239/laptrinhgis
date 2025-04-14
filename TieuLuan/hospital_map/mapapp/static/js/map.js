document.addEventListener("DOMContentLoaded", function () {
    const mapDiv = document.getElementById("map");
    if (!mapDiv) return;
  
    const map = L.map("map").setView([10.7769, 106.7009], 12);
  
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "© OpenStreetMap contributors"
    }).addTo(map);
  
    fetch("/api/hospitals/")
      .then(res => res.json())
      .then(data => {
        data.forEach(h => {
          L.marker([h.lat, h.lng])
            .addTo(map)
            .bindPopup(`<strong>${h.name}</strong>`);
        });
      });
  });
  