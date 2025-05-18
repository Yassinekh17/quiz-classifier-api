from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}}, supports_credentials=True)


# Load model
model = joblib.load('model/model.pkl')  
scaler = joblib.load('model/scaler.pkl')
@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200  # for preflight

    data = request.get_json()
    features = data.get('features')
    if features is None:
        return jsonify({'error': 'No features provided'}), 400
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)
    return jsonify({'prediction': int(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)
