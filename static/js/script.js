const map = L.map('map').setView([-23.5505, -46.6333], 11);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

L.marker([-23.55, -46.63]).addTo(map)
  .bindPopup('Unidade Orizon - SP');

fetch('/api/news')
  .then(res => res.json())
  .then(data => {
    const newsDiv = document.getElementById('news');
    const ticker = document.getElementById('ticker-content');
    let tickerText = '';

    const keywords = [
      'trânsito', 'engarrafamento', 'acidente', 'alagamento', 'enxurrada',
      'deslizamento', 'desabamento', 'incêndio', 'explosão', 'chuva',
      'tempestade', 'queda de energia', 'violência', 'tiroteio', 'roubo'
    ];

    data.forEach(article => {
      const title = article.title || '';
      const description = article.description || '';

      const div = document.createElement('div');
      div.innerHTML = `<p><strong>${title}</strong><br>${description}</p>`;
      newsDiv.appendChild(div);

      const texto = (title + ' ' + description).toLowerCase();
      const isRelevant = keywords.some(k => texto.includes(k));

      if (isRelevant) {
        tickerText += `🚨 ${title} • `;
      }
    });

    ticker.innerText = tickerText || '✅ Nenhum evento crítico detectado no momento.';
  });