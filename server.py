from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/analyze_dna', methods=['POST'])
def analyze_dna():
    dna_sequence = request.json["dna_sequence"]
    mutation_risk = round(random.uniform(0, 1), 2)
    return jsonify({"sequence": dna_sequence, "mutation_risk": mutation_risk})

if __name__ == "__main__":
    app.run(port=5000)
