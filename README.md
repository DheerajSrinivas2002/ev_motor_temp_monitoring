**EV Motor PM Temperature Predictor**
A machine learning model that predicts the permanent magnet temperature of an electric motor in real time using indirect sensor readings.

**Why this matters:**
Permanent magnet temperature is critical in EV motors — if magnets overheat, they lose their magnetism permanently and irreversibly. Direct measurement is difficult in production vehicles, so this model predicts it from sensors that are already available: coolant temperature, motor speed, ambient temperature, and current readings.

**What I built**
Explored and cleaned a real 1.3 million row motor sensor dataset
Dataset sourced from kagge. link:https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature
Engineered time series features (lag, rolling average, delta)
Trained a Random Forest regression model achieving MAE of 0.67°C
Deployed as an interactive Streamlit web app with live predictions. Still ironing out the kinks on the slider range and how it affects the final output

Tech stack
Python, Pandas, Scikit-learn, Matplotlib, Streamlit, Joblib
