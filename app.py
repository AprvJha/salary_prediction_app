from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load trained pipelines (preprocessing + model)
model_files = {
    "Decision Tree": "models/decision_tree.pkl",
    "Random Forest": "models/random_forest.pkl",
    "Linear Regression": "models/linear_regression.pkl"
}

models = {}
for name, path in model_files.items():
    if os.path.exists(path):
        models[name] = joblib.load(path)
    else:
        print(f"Warning: {path} not found!")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Collect user input
            exp = int(request.form["experience"])
            edu = request.form["education"]
            job = request.form["jobtitle"]
            age = int(request.form["age"])
            selected_model = request.form["model"]

            # Create DataFrame from input
            user_input = pd.DataFrame({
                "Experience": [exp],
                "Education": [edu],
                "JobTitle": [job],
                "Age": [age]
            })

            # Predict using selected model
            pipeline = models[selected_model]
            prediction = pipeline.predict(user_input)[0]

        except Exception as e:
            prediction = f"Error: {str(e)}"

    # Possible options for dropdowns
    educations = ["High School", "Bachelor", "Master", "PhD"]
    job_titles = ["Analyst", "Software Engineer", "Data Scientist", "Manager"]
    model_names = list(models.keys())

    return render_template(
        "index.html",
        prediction=prediction,
        educations=educations,
        job_titles=job_titles,
        model_names=model_names
    )

if __name__ == "__main__":
    app.run(debug=True)
