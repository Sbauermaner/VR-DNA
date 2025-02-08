import numpy as np
import matplotlib.pyplot as plt

def biorhythm_sync(frequency, phase_shift=0):
    """Генерация синусоидальной волны для биоритмов"""
    sample_rate = 44100
    duration = 5  # 5 секунд
    time = np.linspace(0, duration, int(sample_rate * duration))
    
    wave = np.sin(2 * np.pi * frequency * time + phase_shift)
    plt.plot(time[:1000], wave[:1000])
    plt.title(f"Биоритмическая волна ({frequency} Гц)")
    plt.xlabel("Время (сек)")
    plt.ylabel("Амплитуда")
    plt.show()

def therapeutic_frequencies():
    """Выбор терапевтической частоты и ее звуковая генерация"""
    healing_frequencies = {
        "Delta (Сон)": 1.5,
        "Theta (Медитация)": 7.83,
        "Alpha (Расслабление)": 10,
        "Beta (Концентрация)": 16,
        "Gamma (Осознанность)": 40
    }
    
    for name, freq in healing_frequencies.items():
        biorhythm_sync(freq)
        print(f"Генерация {name} - {freq} Гц")

# Пример использования
therapeutic_frequencies()
