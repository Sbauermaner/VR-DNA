from scipy.io import wavfile

# После генерации wave:
wavfile.write("dna_music.wav", sample_rate, (wave * 32767).astype(np.int16))
print("Аудиофайл сохранен как dna_music.wav")
