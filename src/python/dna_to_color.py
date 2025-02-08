import colorsys

def generate_color_from_dna(dna_sequence):
    """Создание цвета на основе ДНК-последовательности"""
    mapping = {'A': 0.1, 'T': 0.3, 'C': 0.6, 'G': 0.9}
    hue = sum(mapping[base] for base in dna_sequence if base in mapping) / len(dna_sequence)
    
    # Конвертация в RGB
    rgb_color = colorsys.hsv_to_rgb(hue, 1, 1)
    rgb_color = tuple(int(c * 255) for c in rgb_color)

    return rgb_color

# Пример
dna_sequence = "ATCGATCG"
print("RGB Цвет из ДНК:", generate_color_from_dna(dna_sequence))
