import streamlit as st
import pickle
import pandas as pd

# Load model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Iris Flower Prediction")

# Input features
sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5)
petal_length = st.slider("Petal Length", 1.0, 7.0)
petal_width = st.slider("Petal Width", 0.1, 2.5)

# Make prediction
if st.button("Predict"):
    features = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                            columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
    prediction = model.predict(features)[0]
    classes = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"Predicted Iris Type: {classes[prediction]}")
