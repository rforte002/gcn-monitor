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
        keywords = (
            '"São Paulo" OR "Rio de Janeiro" OR "Florianópolis" AND '
            '"enchente" OR "violência" OR "tiroteio" OR "apagão" OR '
            '"queda de energia" OR "ataque cibernético" OR "roubo de dados"'
        )

        url = (
            "https://newsapi.org/v2/everything?"
            f"q={keywords}&"
            "language=pt&"
            "sortBy=publishedAt&"
            f"apiKey={api_key}"
        )

        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])

        return jsonify(articles)
    except Exception as e:
        return jsonify({"error": f"Erro ao obter notícias: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
