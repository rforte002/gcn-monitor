import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map")
def mapa_unidades():
    return render_template("map.html")

@app.route("/api/news")
def get_news():
    api_key = os.environ.get("GNEWS_API_KEY")
    if not api_key:
        return jsonify({"error": "Chave da API não configurada"}), 500

    try:
        # Palavras-chave relacionadas à continuidade de negócios
        keywords = (
            "catástrofe OR enchente OR violência OR tiroteio OR "
            "sequestro OR vazamento de dados OR ciberataque OR crise OR acidente"
        )
        # Cidades de interesse
        cities = ["São Paulo", "Rio de Janeiro", "Florianópolis"]
        results = []

        for city in cities:
            query = f"{keywords} {city}"
            url = (
                f"https://gnews.io/api/v4/search?q={requests.utils.quote(query)}"
                f"&lang=pt&country=br&max=5&apikey={api_key}"
            )
            response = requests.get(url)
            data = response.json()

            if data.get("status") != "ok" and "articles" not in data:
                continue  # Ignora se resposta não for válida

            articles = data.get("articles", [])
            results.extend(articles)

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": f"Erro ao obter notícias: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
