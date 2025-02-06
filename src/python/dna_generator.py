import random

def generate_dna(length=10):
    return ''.join(random.choice('ATCG') for _ in range(length))

print("Generated DNA:", generate_dna(15))
