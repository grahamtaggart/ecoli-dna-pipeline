#! /usr/bin/bash python

from Bio import Entrez, SeqIO
from io import StringIO
#

Entrez.email = 'graham.n.taggart.dut@gmail.com'

handle1 = Entrez.esearch(db='nucleotide', retmax='40', term='lacY[Gene Name] AND "Escherichia coli"[Organism]')
record1 = Entrez.read(handle1)
print(record1['IdList'])
id_list = record1['IdList']
handle = Entrez.efetch(db='nucleotide', id=id_list, rettype='gb')
recs = handle.read()
list(SeqIO.parse(StringIO(recs), 'gb'))
handle.close()
print(recs)
for rec in recs:
    if rec.name == '949083':
        break
print(rec.name)
print(rec.description)
print(rec.seq)


