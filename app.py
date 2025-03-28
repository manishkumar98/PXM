# backend/app.py
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/submit-data', methods=['POST'])
def submit_data():
    data = request.get_json()

    # Perform data analysis (simplified)
    product_name = data['product_name']
    sales = data['sales']
    reviews = data['reviews']
    sentiment = analyze_sentiment(reviews)  # Your sentiment analysis function

    result = {
        "product_name": product_name,
        "sales": sales,
        "sentiment": sentiment
    }

    return jsonify(result)

def analyze_sentiment(reviews):
    # Simplified sentiment analysis, you should use a real NLP library
    return 0.7

if __name__ == '__main__':
    app.run(debug=True)
