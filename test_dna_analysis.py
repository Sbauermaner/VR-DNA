from dna_analysis import analyze_mutations

def test_dna_analysis():
    dna_sequence = "ATCGTACGATCG"
    target_sequence = "TACG"
    result = analyze_mutations(dna_sequence, target_sequence)
    assert len(result) > 1, "Мутации не найдены!"
    print("Тест анализа ДНК успешно пройден!")

test_dna_analysis()
