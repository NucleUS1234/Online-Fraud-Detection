Fraud Detection System
This project aims to develop a machine learning model that can detect fraudulent transactions using financial transaction data. The dataset includes various features such as transaction type, amount, origin account balance, and destination account balance, which are used to train the model.

Table of Contents
Project Overview
Dataset
Exploratory Data Analysis
Feature Engineering
Model Training
Results
Installation
Usage
Contributing
License
Project Overview
The goal of this project is to predict fraudulent transactions using a Decision Tree Classifier. We preprocess the dataset, explore the data, check correlations between features, and train a machine learning model to classify transactions as "Fraud" or "No Fraud".

Dataset
The dataset used in this project contains the following columns:

step: Time step of the transaction
type: Type of transaction (e.g., CASH_OUT, PAYMENT, etc.)
amount: Amount of the transaction
nameOrig: Customer ID of the origin account
oldbalanceOrg: Initial balance of the origin account
newbalanceOrig: New balance of the origin account after the transaction
nameDest: Customer ID of the destination account
oldbalanceDest: Initial balance of the destination account
newbalanceDest: New balance of the destination account after the transaction
isFraud: Indicates if the transaction is fraudulent (1) or not (0)
isFlaggedFraud: Indicates if the transaction is flagged as potentially fraudulent (1) or not (0)
Exploratory Data Analysis
We performed the following steps to explore the dataset:

Null Values Check: Ensured there are no missing values in the dataset.
Transaction Type Distribution: Visualized the distribution of transaction types using a pie chart.
Correlation Analysis: Checked correlations between features and the target variable (isFraud).
Feature Engineering
Encoded the type feature into numerical values.
Mapped the isFraud target variable to "Fraud" and "No Fraud" labels for better interpretability.
Model Training
We trained a Decision Tree Classifier using the following steps:

Data Splitting: Split the dataset into training and testing sets (80% training, 20% testing).
Model Training: Trained the model on the training data.
Model Evaluation: Achieved an accuracy score of 99.97% on the test set.
Results
The model is able to predict fraudulent transactions with high accuracy. For example, it correctly identified a transaction with the following features as fraudulent:

type: Transfer (encoded as 4)
amount: 9000.60
oldbalanceOrg: 9000.60
newbalanceOrig: 0.0
The model predicted this transaction as "Fraud".
