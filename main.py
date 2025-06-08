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

    url = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        return jsonify(data.get("articles", []))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
