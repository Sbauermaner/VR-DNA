from Bio import Entrez, SeqIO

Entrez.email = "user@example.com"
handle = Entrez.efetch(db="nucleotide", id="NM_001301717", rettype="fasta")
record = SeqIO.read(handle, "fasta")
print(record.seq)
