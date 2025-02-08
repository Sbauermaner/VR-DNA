import requests

# NCBI Gene API URL
NCBI_GENE_API = "https://api.ncbi.nlm.nih.gov/datasets/v1/gene/"
NCBI_DBSNP_API = "https://api.ncbi.nlm.nih.gov/snp/"

def fetch_gene_info(gene_id):
    """Получает информацию о гене из NCBI Gene"""
    response = requests.get(f"{NCBI_GENE_API}{gene_id}")
    if response.status_code == 200:
        return response.json()
    return {"error": "Ген не найден"}

def fetch_snp_info(snp_id):
    """Получает данные о мутации из dbSNP"""
    response = requests.get(f"{NCBI_DBSNP_API}{snp_id}")
    if response.status_code == 200:
        return response.json()
    return {"error": "SNP не найден"}

# Тестовый вызов
gene_data = fetch_gene_info("7157")  # TP53 (Tumor suppressor gene)
snp_data = fetch_snp_info("rs1801133")  # SNP, связанный с болезнью

print(gene_data)
print(snp_data)
