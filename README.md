# 📊 Quiz Classifier App
This is a simple machine learning API built with Flask to classify quiz outcomes based on user input features. It is designed to integrate seamlessly with a frontend built using Angular and other backend services like Spring Boot.

# 🚀 Features
Predicts quiz results using a pre-trained ML model

Exposes a REST API endpoint (/predict) for integration

Built using Flask, scikit-learn, joblib, and pandas

Supports cross-origin requests via flask-cors

# 🛠️ Requirements
Ensure Python 3.7+ is installed.

# 📦 Installation
Clone the repository:

```git clone https://github.com/your-username/quiz-classifier-app.git```
```cd quiz-classifier-app```
Install dependencies:

You can install the required Python packages using the following commands:

```pip install flask flask-cors```
```pip install flask flask-cors joblib```
```pip install numpy```
```pip install flask joblib scikit-learn pandas```

Alternatively, install everything in one go using:

```pip install -r requirements.txt```

# ✅ You can create a requirements.txt file with the following content:


flask
flask-cors
joblib
numpy
scikit-learn
pandas

# ▶️ Running the App
Once dependencies are installed, start the Flask server:

```python app.py```

The API will be running at:
http://localhost:5000/predict

# 📤 API Endpoint
POST /predict
Request Body (JSON):

{
  "feature1": value,
  "feature2": value,
  ...
}
Response (JSON):
{
  "prediction": "Success" | "Failure"
}
# 📂 Project Structure
```
quiz-classifier-app/
│
├── app.py               # Flask server and API endpoint
├── model.pkl            # Pre-trained machine learning model (exported via joblib)
└── README.md            # This file

```

# 👨‍💻 Author
Built by Yassine Khiari.
Part of the Khotwa E-learning platform ecosystem.

