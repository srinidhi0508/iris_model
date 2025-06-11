# iris_model
A simple Machine Learning model (Iris flower classifier using scikit-learn) and deploy it using Streamlit (for a web app)
# 🌸 Iris Flower Prediction - ML Project

This is a simple Machine Learning project to classify iris flowers into three species (*setosa*, *versicolor*, *virginica*) using the Random Forest Classifier. The model is trained on the famous Iris dataset and deployed using Streamlit.

## 📊 Dataset

- Dataset: **Iris** from `sklearn.datasets`
- Features:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- Target: Flower species

---

## ⚙️ Model

- Algorithm: `RandomForestClassifier` from `sklearn.ensemble`
- Accuracy: ~95% (can vary slightly on different runs)

---

## 🖥️ Deployment

- **Local**: `streamlit run app.py`
- **Online**: Deployed via **Streamlit Cloud** (link below)

---

## 🧪 Files Included

- `model.py` → Trains and saves the model as `iris_model.pkl`
- `app.py` or `add.py` → Streamlit UI for prediction
- `iris_model.pkl` → Saved model
- `requirements.txt` → List of packages for deployment

---

## 🚀 Try it Live

[🌐 Deployed App on Streamlit Cloud]()

---

## 📦 Installation

```bash
pip install -r requirements.txt
streamlit run app.py

