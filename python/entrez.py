#! C:\Users\graha\ecoli-dna-pipeline-1\venv\Scripts\python.exe
import os
import argparse
from typing import Dict, List, Any
from Bio import Entrez

# This CLI script takes in your email, the organism of interest, the database, and what data to select all from your terminal!
# This script assumes that you want genome information (Fasta, FastaQ, assembly sequences), but be careful, multicellular organisms can have GB's of data.

# Base EFetch link, builds into others https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi

def search_for_organism(email, organism):
    Entrez.email = email
    search_org = f"{organism} [ORGN]"
    handle = Entrez.esearch(db='nuccore', term=search_org)
    record = Entrez.read(handle)

    if record['IdList']:
        accession_num = record['IdList'][0]
        return accession_num
    else:
        print(f"No records found for the organism: {organism}")
        return None

def download_genomic_data(accession_num, data_amount, output_dir, data_type):
    if accession_num:
        data_amount = min(int(data_amount), 1)  # Limit to 1 sequence for demonstration purposes

        try:
            handle = Entrez.efetch(db='nuccore', id=accession_num, rettype=data_type, retmax=data_amount)
            data = handle.read()

            os.makedirs(output_dir, exist_ok=True)

            output_filename = f"{output_dir}/{accession_num}_{data_amount}.{data_type}"
            with open(output_filename, 'w') as output_file:
                output_file.write(data)

            print(f"Genomic data downloaded successfully. Saved to: {output_filename}")

        except Exception as e:
            print(f"An error occurred during data download: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Use of Biopython's 'Entrez' class to retrieve genomic data from command line",
        description="This program takes as input your email, organism, and datatype. Assumes you're retrieving genomic data.",
        epilog=("Databases include ['pubmed', 'protein', 'nucleotide', 'nuccore', 'nucgss', 'nucest',"
                "'structure', 'genome', 'books', 'cancerchromosomes', 'cdd', 'gap',"
                "'domains', 'gene', 'genomeprj', 'gensat', 'geo', 'gds', 'homologene',"
                "'journals', 'mesh', 'ncbisearch', 'nlmcatalog', 'omia', 'omim', 'pmc',"
                "'popset', 'probe', 'proteinclusters', 'pcassay', 'pccompound',"
                "'pcsubstance', 'snp', 'taxonomy', 'toolkit', 'unigene', 'unists'"))

    parser.add_argument('--email', required=True, help='Your email address (required by NCBI)')
    parser.add_argument('--organism', required=True, help='Organism name to download data from')
    parser.add_argument('--data-amount', default=1, help='Number of sequences to download (default: 1)')
    parser.add_argument('--output-dir', default='output', help='Output directory for downloaded data (default: output)')
    parser.add_argument('--data-type', default='fasta', choices=['fasta', 'gb'], help='Data type to download (fasta or gb, default: fasta)')

    args = parser.parse_args()

    accession_num = search_for_organism(args.email, args.organism)
    download_genomic_data(accession_num, args.data_amount, args.output_dir, args.data_type)

    