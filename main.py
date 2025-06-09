import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/news")
def get_news():
    api_key = os.environ.get("GNEWS_API_KEY")
    if not api_key:
        return jsonify({"error": "Chave da API não configurada"}), 500

    try:
        # Palavras-chave relacionadas a continuidade
        keywords = "catástrofe OR enchente OR violência OR tiroteio OR sequestro OR vazamento de dados OR ciberataque"
        # Áreas geográficas de interesse
        cities = ["São Paulo", "Rio de Janeiro", "Florianópolis"]
        results = []

        for city in cities:
            query = f"{keywords} {city}"
            url = (
                f"https://gnews.io/api/v4/search?q={query}"
                f"&lang=pt&country=br&max=5&apikey={api_key}"
            )
            response = requests.get(url)
            data = response.json()

            articles = data.get("articles", [])
            results.extend(articles)

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": f"Erro ao obter notícias: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
