import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
df = pd.read_csv("diabetes.csv")  # Adjust the file name if needed
print(df.head())

# Separate features and target
X = df.drop(columns=["Outcome"])
y = df["Outcome"]

# Normalize the feature data
X = (X - X.mean()) / X.std()

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model
with open("diabetes_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as 'diabetes_model.pkl'")
