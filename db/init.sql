CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    pregnancies INT,
    glucose FLOAT,
    blood_pressure FLOAT,
    skin_thickness FLOAT,
    insulin FLOAT,
    bmi FLOAT,
    dpf FLOAT,
    age INT,
    prediction_result VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
