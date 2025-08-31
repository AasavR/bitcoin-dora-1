from fastapi import FastAPI, Request
import requests, os

app = FastAPI()
CORTENSOR_URL = os.getenv("CORTENSOR_URL")
CORTENSOR_KEY = os.getenv("CORTENSOR_KEY")

@app.post("/inference/{model}")
async def inference(model: str, request: Request):
    payload = await request.json()
    headers = {"Authorization": f"Bearer {CORTENSOR_KEY}"}
    r = requests.post(f"{CORTENSOR_URL}/{model}", json=payload, headers=headers)
    return r.json()
