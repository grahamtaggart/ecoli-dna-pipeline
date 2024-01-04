from Bio import Entrez, SeqIO
from io import StringIO
Entrez.email = 'graham.n.taggart.dut@gmail.com'
# Einfo to find out WHAT I can actually query


# Search for e.coli lacY gene and find id's (GenBank Accession Numbers)
handle = Entrez.esearch(db='nucleotide', retmax=10, term='Escherichia coli[Orgn] AND lacY[Gene]')
record = Entrez.read(handle)
id_list = record['IdList']
# Efetch 
handle1 = Entrez.efetch(db='nucleotide', id=id_list[0], rettype='gb', retmode='text')
res = handle1.read()
record1 = SeqIO.read(StringIO(res), 'gb')

print(type(record1))
