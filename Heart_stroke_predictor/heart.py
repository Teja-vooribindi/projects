# Importing the Libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Load and prepare the dataset
df = pd.read_csv("C:\\Users\\vijay\\Downloads\\heart_disease_data.csv")

X = df.drop(columns='target', axis=1)
Y = df['target']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the model
model = LogisticRegression(max_iter=200)
model.fit(X_train, Y_train)

# Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve form data
        input_data = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]  # Exclude the 'target' column

        # Convert input_data to DataFrame
        target_df = pd.DataFrame([input_data], columns=X.columns)

        # Prediction
        prediction = model.predict(target_df)[0]

        # Display results
        if prediction == 0:
            result = "Good News: Patient doesn't have heart disease."
        else:
            result = "Oh! Patient should visit the doctor."

        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
