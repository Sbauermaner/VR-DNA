import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

def dna_to_music(dna_sequence):
    """Конвертация ДНК-последовательности в звуковые волны"""
    mapping = {'A': 440, 'T': 494, 'C': 523, 'G': 587}  # Частоты нот
    frequencies = [mapping[base] for base in dna_sequence if base in mapping]

    # Создание звуковой волны
    sample_rate = 44100
    duration = 0.5
    time = np.linspace(0, duration, int(sample_rate * duration))
    wave = np.sin(2 * np.pi * np.array(frequencies)[:, None] * time).sum(axis=0)

    plt.plot(time[:1000], wave[:1000])
    plt.title("Музыкальная волна ДНК")
    plt.xlabel("Время (сек)")
    plt.ylabel("Амплитуда")
    plt.show()

    return wave

# Пример использования
dna_sequence = "ATCGATCG"
waveform = dna_to_music(dna_sequence)
