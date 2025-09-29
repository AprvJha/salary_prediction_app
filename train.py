import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
import os

# Load your dataset
df = pd.read_excel("salary_prediction_data.xlsx")

# Preprocess
X = df.drop("Salary", axis=1)
y = df["Salary"]

# Dummy encoding
X = pd.get_dummies(X, drop_first=True)

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train models
dt = DecisionTreeRegressor().fit(X_train, y_train)
rf = RandomForestRegressor().fit(X_train, y_train)
mlp = MLPRegressor(max_iter=1000).fit(X_train, y_train)

# Save models
os.makedirs("models", exist_ok=True)
joblib.dump(dt, "models/decision_tree.pkl")
joblib.dump(rf, "models/random_forest.pkl")
joblib.dump(mlp, "models/neural_net.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Models retrained and saved!")
