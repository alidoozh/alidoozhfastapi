from fastapi import FastAPI, HTTPException
from mlp_model import MLPModel
from drl_model import DRLModel
from signal_engine import get_signals
from decision_engine import get_final_signal
from market_state import get_market_state
from volume_profile import get_volume_profile
from whale_activity import get_whale_activity
from sentiment import get_sentiment
from risk_reward import get_risk_reward
from candle_analysis import get_candle_analysis
from adaptive_weights import get_weights
from live_data import get_live_rates

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/predict/mlp")
def predict_mlp():
    return MLPModel().predict()

@app.get("/predict/drl")
def predict_drl():
    return DRLModel().predict()

@app.get("/signal/final")
def final_signal():
    return {"signal": get_final_signal()}

@app.get("/market/state")
def market():
    return get_market_state()

@app.get("/volume/profile")
def volume():
    return get_volume_profile()

@app.get("/whale/activity")
def whale():
    return get_whale_activity()

@app.get("/sentiment")
def sentiment():
    return get_sentiment()

@app.get("/risk/reward")
def risk():
    return get_risk_reward()

@app.get("/candle/analysis")
def candle():
    return get_candle_analysis()

@app.get("/adaptive/weights")
def weights():
    return get_weights()

@app.get("/live/rates")
def rates():
    return get_live_rates()
