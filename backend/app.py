from flask import Flask, jsonify, request
import joblib
import numpy as np
import psycopg2

app = Flask(__name__)

# Load the ML model
model = joblib.load("diabetes_model.pkl")

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="microservices_db",
        user="postgres",
        password="password"
    )
    return conn

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        # Convert data into a NumPy array
        # Add placeholders for missing features (e.g., Gender and Smoking Status as 0)
        input_features = np.array(data["features"] + [0.0, 0.0]).reshape(1, -1)

        # Predict diabetes
        prediction = model.predict(input_features)[0]
        result = "Diabetic" if prediction == 1 else "Non-Diabetic"

        # Save to database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO predictions (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age, prediction_result)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (*data["features"], result)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
