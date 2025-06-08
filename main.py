import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/news")
def get_news():
    return jsonify([{"title": "Teste de resposta OK"}])

    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()

        # Verifica se 'articles' existe e é uma lista
        articles = data.get("articles", [])
        if not isinstance(articles, list):
            return jsonify([])

        return jsonify(articles)
    except Exception as e:
        return jsonify({"error": f"Erro ao obter notícias: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
