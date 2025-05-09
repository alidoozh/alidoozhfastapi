from signal_engine import get_signals

def get_final_signal():
    s = get_signals()
    if s["mlp"] == s["drl"]:
        return s["mlp"]
    return "hold"
