import torch
import torch.nn as nn

class DNAMutationPredictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(10, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.fc(x)

def predict_mutation_risk(dna_sequence):
    model = DNAMutationPredictor()
    input_data = torch.randn(1, 10)
    return model(input_data).item()
