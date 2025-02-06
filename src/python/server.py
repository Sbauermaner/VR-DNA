from flask import Flask, request, jsonify
import torch
from dna_mutation_ai import DNAMutationPredictor

app = Flask(__name__)
model = DNAMutationPredictor()

@app.route('/analyze_stretch', methods=['POST'])
def analyze_stretch():
    if not request.is_json:
        return jsonify({"error": "Invalid data format"}), 400
    try:
        stretch_data = request.get_json()["stretch_values"]
        stretch_tensor = torch.tensor(stretch_data, dtype=torch.float32)
        risk_factor = model(stretch_tensor).item()
        return jsonify({"mutation_risk": risk_factor})
    except KeyError:
        return jsonify({"error": "Missing 'stretch_values'"}), 400

if __name__ == "__main__":
    app.run(port=5000)
