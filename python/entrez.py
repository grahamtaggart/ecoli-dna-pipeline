import argparse
from typing import str, Dict, List, Any

print(result)

def ezget():
    parser = argparse.ArgumentParser(
        prog="Use of Biopython's 'Entrez' class to retrieve data from commandline",
        description="This program takes as input your email, organism, and datatype",
        epilog=("Databases include ['pubmed', 'protein', 'nucleotide', 'nuccore', 'nucgss', 'nucest',
        'structure', 'genome', 'books', 'cancerchromosomes', 'cdd', 'gap',
        'domains', 'gene', 'genomeprj', 'gensat', 'geo', 'gds', 'homologene',
        'journals', 'mesh', 'ncbisearch', 'nlmcatalog', 'omia', 'omim', 'pmc',
        'popset', 'probe', 'proteinclusters', 'pcassay', 'pccompound',
        'pcsubstance', 'snp', 'taxonomy', 'toolkit', 'unigene', 'unists'""))
    
    parser.add_argument('email address')
    parser.add_argument('organism')
    parser.add_argument('datatype')
    parser.add_argument('-o','--output')
    parser.add_argument('-d','--data')
