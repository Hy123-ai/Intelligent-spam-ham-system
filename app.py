from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import os
import uvicorn

app = FastAPI()

# Path Setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Static files mount
static_path = os.path.join(BASE_DIR, "static")
if not os.path.exists(static_path):
    os.makedirs(static_path)
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Load Model & Vectorizer
MODEL_PATH = os.path.join(BASE_DIR, "model", "spam_detect_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
with open(VECTORIZER_PATH, "rb") as f:
    cv = pickle.load(f)

# --- ROUTES ---

@app.get("/")
async def home(request: Request):
    # Yeh aapki main website (front.html) ko load karega
    return templates.TemplateResponse(request, "front.html")

@app.get("/classifier")
async def classifier_page(request: Request):
    # Yeh aapke prediction page (index.html) ko load karega
    return templates.TemplateResponse(request, "index.html")

@app.post("/predict")
async def predict(request: Request, message: str = Form(...)):
    data = cv.transform([message]).toarray()
    prediction = model.predict(data)[0]
    result = "Spam" if prediction == 1 else "Ham"
    
    return templates.TemplateResponse(request, "index.html", {
        "prediction": result, 
        "original_text": message
    })

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)