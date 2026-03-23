# ♻️ WasteWise — AI Waste Classification System

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> AI-powered waste classification system — upload a waste image and instantly know if it is **Recyclable**, **Organic**, or **Hazardous**!

---

## 🌍 Why This Project?

Improper waste disposal causes major environmental pollution. WasteWise solves this by letting anyone upload a photo of waste and instantly get the category + disposal tip.

---

## ✨ Features

- ♻️ Classifies waste as **Recyclable / Organic / Hazardous**
- 📊 Confidence score for each prediction
- 💡 Disposal tip for each category
- 📂 History dashboard to track past classifications
- ⚡ FastAPI backend — fast and lightweight

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| ML Model | TensorFlow, MobileNetV2 (Transfer Learning) |
| Backend API | FastAPI, Uvicorn |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render.com |

---

## 📁 Project Structure
```
waste-classifier/
├── model/
│   ├── preprocess.py
│   ├── train.py
│   ├── model_cnn.h5
│   └── class_indices.pkl
├── api/
│   ├── main.py
│   └── predict.py
├── frontend/
│   └── index.html
├── run.bat
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Madhu-T18/waste-classifier.git
cd waste-classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the API
```bash
cd api
uvicorn main:app --reload
```

### 4. Open frontend
Open `frontend/index.html` in browser

> Windows users — just double click `run.bat`! 🎉

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/predict` | Upload image → get category |
| GET | `/categories` | List all categories |

### Sample Response
```json
{
  "category": "Recyclable",
  "confidence": 92.4,
  "disposal_tip": "Clean and place in blue recycling bin.",
  "raw_class": "plastic"
}
```

---

## 📊 Waste Categories

| Category | Examples | Bin |
|---|---|---|
| ♻️ Recyclable | Plastic, Paper, Glass, Metal | 🔵 Blue bin |
| 🌿 Organic | Food scraps, Leaves, Peels | 🟢 Green bin |
| ⚠️ Hazardous | Batteries, Chemicals, E-waste | 🔴 Hazardous facility |

---

## 🧠 Model Details

| Detail | Info |
|---|---|
| Base Model | MobileNetV2 (ImageNet pretrained) |
| Approach | Transfer Learning |
| Input Size | 224 x 224 px |
| Classes | Recyclable, Organic, Hazardous |
| Accuracy | ~66% |
| Optimizer | Adam |

---

## 🙋‍♀️ Author

**Madhu T**
- 🎓 AI/ML Student — Sri Shakthi Institute of Engineering and Technology
- 💼 [LinkedIn](https://www.linkedin.com/in/madhu-t-b6b106331)
- 🐙 [GitHub](https://github.com/Madhu-T18)

---

## 📄 License

MIT License

---

⭐ If you found this useful, please star this repo!

> Built with 💚 for a cleaner environment
