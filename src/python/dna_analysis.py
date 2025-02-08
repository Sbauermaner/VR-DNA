def analyze_mutations(dna_sequence, target_sequence):
    try:
        hits = nt_search(str(dna_sequence), str(target_sequence))
        return hits[1:]  # Исключаем первый элемент (шаблон)
    except Exception as e:
        return f"Ошибка анализа ДНК: {e}"
