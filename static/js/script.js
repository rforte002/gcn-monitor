window.onload = async function () {
  const ticker = document.getElementById('ticker-content');

  try {
    const res = await fetch('/api/news');
    const data = await res.json();
    const headlines = data.map(article => article.title).join(' ⚠️ ');
    ticker.textContent = headlines || 'Nenhuma notícia disponível no momento.';
  } catch (err) {
    ticker.textContent = 'Erro ao carregar as notícias.';
  }
};

