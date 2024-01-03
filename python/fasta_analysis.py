#! C:\Users\graha\ecoli-dna-pipeline-1\venv\Scripts\python.exe
# fasta_analysis is used for visualization, GWAS, 
from Bio import SeqIO

seq_record = SeqIO.read("python/e.coli_testing/2642090372_1.fasta","fasta")
print(seq_record)


