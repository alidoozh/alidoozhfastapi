from mlp_model import predict_mlp
from drl_model import predict_drl
from risk_reward import get_risk_reward

def get_signals():
    mlp = predict_mlp()
    drl = predict_drl()
    rr = get_risk_reward()
    return {"mlp": mlp, "drl": drl, "risk_reward": rr}
