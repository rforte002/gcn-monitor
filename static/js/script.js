// Inicializa o mapa
const map = L.map('map').setView([-23.5505, -46.6333], 11);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

L.marker([-23.5505, -46.6333])
  .addTo(map)
  .bindPopup('Unidade Orizon - SP');

// Atualiza o ticker com as notícias
window.onload = async function () {
    const ticker = document.getElementById('ticker-content');

    try {
        const res = await fetch('/api/news');
        const data = await res.json();
        const headlines = data.map(article => article.title).join(' 🔺 ');
        ticker.textContent = headlines || 'Nenhuma notícia disponível no momento.';
    } catch (err) {
        ticker.textContent = 'Erro ao carregar as notícias.';
    }
};


