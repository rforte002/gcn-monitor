import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/news")
def get_news():
    api_key = os.environ.get("NEWS_API_KEY")
    if not api_key:
        return jsonify({"error": "Chave da API não configurada"}), 500

    try:
        # Termos críticos para continuidade de negócio nas 3 cidades
        keywords = (
            "São Paulo OR Rio de Janeiro OR Florianópolis "
            "AND (enchente OR violência OR apagão OR tiroteio OR "
            "roubo de dados OR ataque hacker OR crise)"
        )

        # Monta a URL com encoding apropriado
        url = (
            "https://newsapi.org/v2/everything?"
            f"q={requests.utils.quote(keywords)}&"
            "language=pt&"
            "sortBy=publishedAt&"
            f"apiKey={api_key}"
        )

        response = requests.get(url)
        response.raise_for_status()  # Lança erro se a resposta for 4xx ou 5xx

        data = response.json()

        articles = data.get("articles", [])
        if not isinstance(articles, list):
            return jsonify([])

        return jsonify(articles)
    except Exception as e:
        return jsonify({"error": f"Erro ao obter notícias: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
