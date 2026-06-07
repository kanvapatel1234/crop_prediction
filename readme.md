# 🌱 Crop Recommendation System

An AI-powered Crop Recommendation System that predicts the most suitable crop based on soil nutrients and environmental conditions using Machine Learning.

## 📌 Project Overview

This project helps farmers and agricultural enthusiasts identify the best crop to cultivate based on input parameters such as:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH Value
* Rainfall

The system uses a trained Machine Learning model and provides crop recommendations through a user-friendly web interface.

---

## 🚀 Features

* Predicts the most suitable crop
* Displays prediction confidence score
* Shows second-best crop recommendation
* FastAPI backend for efficient API handling
* Responsive frontend using HTML, CSS, and JavaScript
* Real-time predictions
* Easy deployment on cloud platforms

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Scikit-Learn
* Pandas
* NumPy
* Joblib

### Backend

* FastAPI
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### Deployment

* Render

---



---

## 📊 Machine Learning Model Performance

| Model         | Accuracy |
| ------------- | -------- |
| Random Forest | 99.55%   |
| XGBoost       | 99.32%   |
| SVM           | 98.41%   |
| KNN           | 97.95%   |
| Decision Tree | 97.95%   |

### Selected Model

✅ Random Forest Classifier

Performance Metrics:

* Accuracy: 99.55%
* Precision: 99.57%
* Recall: 99.55%
* F1 Score: 99.55%

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/crop-recommendation-system.git
cd crop-recommendation-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🌾 Input Parameters

| Feature     | Description           |
| ----------- | --------------------- |
| N           | Nitrogen Content      |
| P           | Phosphorus Content    |
| K           | Potassium Content     |
| Temperature | Temperature in °C     |
| Humidity    | Relative Humidity (%) |
| pH          | Soil pH               |
| Rainfall    | Rainfall (mm)         |

---

## 📈 Prediction Output

The API returns:

```json
{
  "best_crop": "rice",
  "best_crop_probability": 98.7,
  "second_crop": "maize",
  "second_crop_probability": 1.2
}
```

---

## 🎯 Future Improvements

* Weather API Integration
* Fertilizer Recommendation System
* Disease Detection Module
* Mobile Application
* Multi-language Support
* Yield Prediction System

---

## 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is developed for educational and research purposes.

---

## 👨‍💻 Author

Kanva

BMS College of Engineering

Machine Learning & Full Stack Development Enthusiast
