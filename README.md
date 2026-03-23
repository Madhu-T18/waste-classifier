♻️ WasteWise — AI Waste Classification System
An AI-powered waste classification system that detects whether waste is Recyclable, Organic, or Hazardous from an image — built with MobileNetV2 Transfer Learning and served via a FastAPI backend with a full dashboard frontend.

🌍 Why This Project?
Improper waste disposal is one of the leading causes of environmental pollution. Most people don't know which bin to use for different types of waste. WasteWise solves this by letting anyone upload a photo of waste and instantly get:
✅ The waste category (Recyclable / Organic / Hazardous)
✅ Confidence score of the prediction
✅ Disposal tip — exactly where and how to dispose it
✅ History dashboard to track past classifications

🖥️ Demo Screenshots
<img width="1888" height="923" alt="Screenshot (727)" src="https://github.com/user-attachments/assets/404149a6-7983-41b5-90f0-84d245ce2833" />
<img width="1847" height="879" alt="Screenshot (728)" src="https://github.com/user-attachments/assets/7e601d5b-ad59-494d-84bd-fa56989f3b0e" />

🛠️ Tech Stack
LayerTechnologyML ModelTensorFlow, MobileNetV2 (Transfer Learning)Backend APIFastAPI, UvicornFrontendHTML, CSS, JavaScriptImage ProcessingPillow, NumPyModel SavingKeras (.h5)DeploymentRender.com

📁 Project Structure
waste-classifier/
├── model/
│   ├── preprocess.py        # Image loading & feature extraction
│   ├── train.py             # Model training script (MobileNetV2)
│   ├── model_cnn.h5         # Trained model file
│   └── class_indices.pkl    # Class label mapping
├── api/
│   ├── main.py              # FastAPI app with endpoints
│   └── predict.py           # Prediction logic
├── frontend/
│   └── index.html           # Full dashboard UI
├── run.bat                  # One-click run (Windows)
├── requirements.txt         # Python dependencies
└── README.md

🚀 Getting Started
Prerequisites

Python 3.10+
pip

1. Clone the repository
bashgit clone https://github.com/Madhu-T18/waste-classifier.git
cd waste-classifier
2. Install dependencies
bashpip install -r requirements.txt
3. Train the model (optional — pretrained model included)
bashcd model
python train.py
4. Start the API
bashcd api
uvicorn main:app --reload
5. Open the frontend
Open frontend/index.html in your browser
Or on Windows — just double click run.bat! 🎉

🌐 API Endpoints
MethodEndpointDescriptionGET/Health checkPOST/predictUpload image → get waste categoryGET/categoriesList all waste categories & tips
Sample Request
bashcurl -X POST "http://127.0.0.1:8000/predict" \
  -H "accept: application/json" \
  -F "file=@waste_image.jpg"
Sample Response
json{
  "category": "Recyclable",
  "confidence": 92.4,
  "disposal_tip": "Clean the item and place it in the blue recycling bin.",
  "raw_class": "plastic"
}

🧠 Model Details
DetailInfoBase ModelMobileNetV2 (pretrained on ImageNet)ApproachTransfer Learning + Fine TuningInput Size224 x 224 pxOutput ClassesRecyclable, Organic, HazardousTraining DatasetCustom waste dataset (1638 images)Accuracy~66% (improving with more data)OptimizerAdamLoss FunctionCategorical Crossentropy

📊 Waste Categories
CategoryExamplesBin♻️ RecyclablePlastic, Paper, Glass, Metal🔵 Blue bin🌿 OrganicFood scraps, Leaves, Peels🟢 Green bin⚠️ HazardousBatteries, Chemicals, E-waste🔴 Hazardous facility

🔧 requirements.txt
fastapi
uvicorn
tensorflow
pillow
numpy
joblib
scikit-learn
scikit-image
python-multipart

🚀 Deployment (Render.com)
This API is deployed on Render.com (free tier).
Live API: Add your Render URL here after deployment

🙋‍♀️ Author
Madhu T

🎓 AI/ML Student — Sri Shakthi Institute of Engineering and Technology, Coimbatore
💼 LinkedIn
🐙 GitHub


📄 License
This project is licensed under the MIT License.

🌟 Show Your Support
If you found this project useful, please ⭐ star this repository — it helps a lot!

Built with 💚 for a cleaner environment
