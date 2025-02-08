from dna_analysis import analyze_mutations

def test_dna_analysis():
    dna_sequence = "ATCGTACGATCG"
    target_sequence = "TACG"
    result = analyze_mutations(dna_sequence, target_sequence)
    assert result == [4], f"Ожидалось [4], получено {result}"
    print("Тест успешно пройден!")

test_dna_analysis()
