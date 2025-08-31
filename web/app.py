from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import requests, os

app = FastAPI()
API_URL = os.getenv("API_URL")

@app.get("/", response_class=HTMLResponse)
def form():
    return '''<form action="/gen" method="post">
                <input name="prompt">
                <button type="submit">Generate</button>
              </form>'''

@app.post("/gen")
def gen(prompt: str = Form(...)):
    r = requests.post(f"{API_URL}/inference/textgen", json={"inputs": prompt})
    return r.json()
