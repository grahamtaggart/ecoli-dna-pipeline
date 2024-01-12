from Bio import Entrez, SeqIO
from collections import Counter
# Trying my current strategy with another organism, seeing if that makes any difference or not, if not try different programming.
Entrez.email = 'graham.n.taggart.dut@gmail.com'

def search_and_fetch_org(organism):
    # Step 1: Search the nucleotide database for HIV fasta files
    search_term = str(organism)
    handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=1)
    record_id = Entrez.read(handle)["IdList"][0]
    handle.close()

    # Step 2: Efetch a single record
    handle = Entrez.efetch(db="nucleotide", id=record_id, rettype="fasta", retmode="text")
    sequence_record = SeqIO.read(handle, "fasta")
    handle.close()

    # Step 3: Print the sequence or perform analysis
    print("Record ID:", record_id)
    print("Sequence Description:", sequence_record.description)
    print("Sequence:")
    print(sequence_record.seq[0:50] + '...' + sequence_record.seq[-50:])
    print('Sequence Length:', len(sequence_record.seq))
    return sequence_record

# search_and_fetch_org('ecoli')

def seq_analysis_gc(function):
   nucleotide_counts = Counter(function.seq)
   g_count = nucleotide_counts.get('G', 0)
   c_count = nucleotide_counts.get('C', 0)
   total_count = g_count + c_count
    # 1 Calculate the percentage of G and C
   if total_count > 0:
        gc_percentage = (total_count / len(function.seq)) * 100
        print(f"G/C Percentage: {gc_percentage:.2f}%")
    

seq_analysis_gc(search_and_fetch_org('ecoli'))