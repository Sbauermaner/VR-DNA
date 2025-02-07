# VR-DNA 🎧🧬  
🚀 Open-source VR platform for DNA visualization, mutation analysis, and AI research.

## 🔬 Features  
✅ **3D visualization** of DNA in VR  
✅ **AI-driven mutation analysis**  
✅ **Spectral analysis of the iris and retina**  
✅ **Real-time DNA stretching (Hoberman effect)**  
✅ **REST API for AI and VR interaction**  
✅ **Unity XR support (Oculus, Vive, SteamVR)**  

## 🚀 Installation  
### 1️⃣ Установка Python и зависимостей  
```bash
pip install -r requirements.txt

# VR-DNA: Интеграция с NCBI Gene и dbSNP

## 🔬 Источники данных:
1. **NCBI Gene** – [https://www.ncbi.nlm.nih.gov/gene/](https://www.ncbi.nlm.nih.gov/gene/)
2. **dbSNP** – [https://www.ncbi.nlm.nih.gov/snp/](https://www.ncbi.nlm.nih.gov/snp/)

## 🛠️ Интеграция:
- Данные о генах и мутациях загружаются через `ncbi_api.py`.
- AI-анализ ДНК использует известные SNP-маркеры (`dna_analysis.py`).
- В VR отображается информация о генах (`NCBIGeneVisualizer.cs`).

⚠️ **Важно:** Все данные получены из открытых источников и соблюдают лицензии NCBI.
