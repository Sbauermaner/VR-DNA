import pytest
from src.python.eye_color_ai import predict_eye_color

def test_eye_color_prediction():
    assert predict_eye_color("AGTCAGTCA") in ["Blue", "Brown", "Green"]
