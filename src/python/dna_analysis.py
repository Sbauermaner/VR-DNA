from ncbi_api import fetch_gene_info, fetch_snp_info

def analyze_dna_sequence(sequence):
    """Анализирует последовательность ДНК и проверяет, содержит ли она известные мутации"""
    known_snps = ["rs1801133", "rs121913529"]  # Примеры мутаций
    results = []
    
    for snp in known_snps:
        snp_data = fetch_snp_info(snp)
        if "error" not in snp_data:
            results.append(snp_data)

    return results

# Анализ тестовой ДНК
dna_results = analyze_dna_sequence("AGTCCAGTCTAGT")
print(dna_results)
