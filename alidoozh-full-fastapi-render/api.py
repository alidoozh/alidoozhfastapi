from fastapi import FastAPI
from live_data import get_live_rates

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/live/rates")
def live_rates():
    return get_live_rates()
