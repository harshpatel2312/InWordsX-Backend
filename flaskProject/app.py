from flask import Flask, render_template
import requests

app = Flask(__name__)

# Fetching data from "/newsModel" endpoint
def fetch_news_model():
    try:
        response = requests.get('http://127.0.0.1:5000/newsModel')
        return response.json() if response.status_code == 200 else {}
    except requests.exceptions.RequestException as e:
        print(f"Fetching request failed: {e}")
        return {}

@app.route('/')
def home():  # put application's code here
    news_model = fetch_news_model()
    return render_template("home.html", news_model = news_model)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
