from flask import Flask, render_template, request
import numpy as np
import joblib

# Create a Flask instance
app = Flask(__name__)

# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

# Route for the home page (index)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        transaction_type = int(request.form['type'])
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        
        # Create a feature array for the model to predict on
        features = np.array([[transaction_type, amount, oldbalanceOrg, newbalanceOrig]])
        
        # Make a prediction using the loaded model
        prediction = model.predict(features)

        # Return the prediction result to the user
        result = "Fraud" if prediction[0] == "Fraud" else "No Fraud"

        # Render the result page (or you can render the same index page with the result)
        return render_template('index.html', prediction_text=f'Transaction is: {result}')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
