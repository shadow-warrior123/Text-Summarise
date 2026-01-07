from fastapi import FastAPI, Request, Form
import uvicorn
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from text_summarizer.pipeline.prediction import PredictionPipeline

app = FastAPI(title="Scribe AI Summarizer")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict_route(text: str):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return summary
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
