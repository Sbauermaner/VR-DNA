import requests

def test_dna_analysis():
    response = requests.post("http://localhost:5000/analyze_dna", json={"dna_sequence": "AGCT"})
    assert response.status_code == 200
    assert "mutation_risk" in response.json()
