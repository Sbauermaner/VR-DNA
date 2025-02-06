import numpy as np
import matplotlib.pyplot as plt

def spectral_analysis(melanin_level):
    wavelengths = np.arange(380, 750, 10)
    reflectance = 1 - (melanin_level * np.exp(-0.001 * (wavelengths - 500) ** 2))

    plt.plot(wavelengths, reflectance)
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Reflectance")
    plt.title("Iris Spectral Analysis")
    plt.show()

spectral_analysis(melanin_level=0.3)
