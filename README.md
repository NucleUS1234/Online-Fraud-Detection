

# Fraud Detection Web Application

This project is a **Fraud Detection Web Application** that allows users to input details of a financial transaction (like transaction type, amount, old balance, and new balance) and get a prediction on whether the transaction is fraudulent or not. The app is powered by a **pre-trained Decision Tree Classifier**.

## Features

- User-friendly form to input transaction details.
- Flask web server to handle form submissions and process predictions.
- Pre-trained machine learning model (Decision Tree) to predict fraud based on transaction features.
- Clean and simple UI with a styled form for ease of use.
- The prediction result is displayed directly on the same page after submission.

## Technologies Used

- **Flask**: Web framework to handle routing and HTTP requests.
- **HTML/CSS**: Frontend for the form and result display.
- **Joblib**: For loading the pre-trained machine learning model.
- **scikit-learn**: Used for training the Decision Tree model.
- **Python**: Core programming language for the backend and model integration.

## Project Structure

```
fraud_detection/
│
├── templates/
│   └── index.html          # The HTML form and result page
├── fraud_detection_model.pkl # Pre-trained machine learning model (Decision Tree)
└── app.py                  # Flask app that runs the server and handles prediction logic
```

## Getting Started

### Prerequisites

You’ll need the following dependencies to run the project:

- Python 3.x
- Flask
- Joblib
- scikit-learn

You can install the required Python packages using:

```
pip install Flask joblib scikit-learn
```

### Running the Application

1. **Clone this repository** to your local machine:

```
git clone https://github.com/yourusername/fraud-detection-webapp.git
```

2. **Navigate to the project folder**:

```
cd fraud_detection
```

3. **Run the Flask app**:

```
python app.py
```

4. **Access the app** by opening your browser and navigating to `http://127.0.0.1:5000/`.

### Usage

- On the homepage, enter the required transaction details in the form:
  - Transaction Type (1: CASH_OUT, 2: PAYMENT, 3: CASH_IN, 4: TRANSFER, 5: DEBIT)
  - Amount (e.g., 9000.60)
  - Old Balance (e.g., 9000.60)
  - New Balance (e.g., 0.00)
- After submitting the form, the app will display whether the transaction is **Fraudulent** or **Not Fraudulent**.

### Example Input

| Field           | Example Value |
|-----------------|---------------|
| Transaction Type| 4 (TRANSFER)  |
| Amount          | 9000.60       |
| Old Balance     | 9000.60       |
| New Balance     | 0.00          |

### Example Output

- **Prediction**: No Fraud

## Model Information

The fraud detection is powered by a **Decision Tree Classifier** trained on a dataset of financial transactions. The model evaluates transactions based on the following features:

- Transaction Type: CASH_OUT, PAYMENT, CASH_IN, TRANSFER, DEBIT
- Transaction Amount
- Old Balance of the origin account
- New Balance after the transaction

The model was trained using **scikit-learn** and saved using **joblib** for easy integration into the Flask web app.

## Future Improvements

- Implement additional machine learning models like Random Forest or XGBoost to improve accuracy.
- Add more transaction features to the dataset (e.g., destination balance).
- Incorporate error handling and validation for user inputs.
- Expand the UI for a more intuitive user experience.
- Add user authentication and transaction logs for tracking predictions.



## Acknowledgements

- **scikit-learn** for the machine learning framework.
- **Flask** for providing an easy-to-use web framework.
- **Joblib** for model serialization and deserialization.

