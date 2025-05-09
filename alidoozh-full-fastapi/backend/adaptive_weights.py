import json

def get_weights():
    try:
        with open("models/weights.json") as f:
            return json.load(f)
    except:
        return {"mlp": 0.6, "drl": 0.4}
