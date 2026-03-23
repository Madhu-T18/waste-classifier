import os
import shutil
import uuid
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from predict import predict_image
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Waste Classification API",
    description="Upload a waste image and get its category: Recyclable, Organic, or Hazardous.",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

@app.get("/")
def health_check():
    return {"status": "running", "message": "Waste Classification API is live!"}

@app.get("/categories")
def get_categories():
    return {
        "categories": [
            {
                "name": "Recyclable",
                "examples": ["cardboard", "glass", "metal", "paper", "plastic"],
                "bin_color": "Blue bin"
            },
            {
                "name": "Organic",
                "examples": ["food scraps", "leaves", "fruit peels"],
                "bin_color": "Green bin"
            },
            {
                "name": "Hazardous",
                "examples": ["batteries", "chemicals", "general trash"],
                "bin_color": "Hazardous waste facility"
            }
        ]
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type '{ext}'. Only JPG and PNG are allowed."
        )

    temp_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}{ext}")
    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = predict_image(temp_path)
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)