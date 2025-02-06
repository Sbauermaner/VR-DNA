from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

@app.route('/analyze_dna', methods=['POST'])
def analyze_dna():
    data = request.get_json()
    dna_sequence = data.get("dna_sequence", "")
    risk = round(torch.rand(1).item(), 2)
    return jsonify({"sequence": dna_sequence, "mutation_risk": risk})

if __name__ == "__main__":
    app.run(port=5000)
