# Salary Prediction App

A Flask web application that predicts salaries based on user input (Education, Job Title, Experience, Age, Location, Gender). 
The app uses trained machine learning models, including Decision Tree, Random Forest, and Neural Network.  

---

## Features

- Predict salary based on user-provided details  
- Handles different job titles, education levels, and locations  
- Compare predictions from multiple ML models  
- Visualizations (optional in Jupyter notebook)  

---

## Requirements

- Python 3.11+  
- Flask  
- pandas  
- numpy  
- scikit-learn  
- joblib  

---

## Setup Instructions

## Create a virtual environment (optional but recommended)

python -m venv venv

## Activate the virtual environment

Windows:

venv\Scripts\activate


Linux / macOS:

source venv/bin/activate


## Install dependencies

pip install -r requirements.txt


## Run the Flask app

python app.py


## Open your browser
Go to http://127.0.0.1:5000 to use the app.


## Notes
1. If you don’t have the .pkl models, you can train them using the provided Jupyter notebook or Python script.
2. Ensure your Python and library versions match the ones used in development (Python 3.11+, numpy < 2).

