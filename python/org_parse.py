from Bio import Entrez, SeqIO

# Trying my current strategy with another organism, seeing if that makes any difference or not, if not try different programming.
Entrez.email = 'graham.n.taggart.dut@gmail.com'

def search_and_fetch_org_sequence(organism):
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
    print(sequence_record.seq[0:50] + '...')

search_and_fetch_org_sequence('ecoli')

def seq_analysis():
    pass