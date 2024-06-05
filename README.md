# Retrieval of FASTA sequence
This Biopython script simplifies the retrieval of protein or nucleotide sequences using accession numbers. Here’s how it works:
# Setup:
1. Install Biopython using the following command:<br />
    pip install biopython <br />
2. Replace ____@gmail.com with your actual email address in the script.
# Usage:
Create a text file (protein_accession_no.txt) containing accession numbers (one per line).<br />
Run the script.<br />
It fetches the corresponding fasta sequences from the NCBI protein database.<br />
The sequences are saved in an output file (output_sequences.fasta).
# Benefits:
Researchers can efficiently retrieve multiple fasta sequences without manual searching<br />
Ideal for projects requiring analysis of more than one protein or gene sequence<br />
I developed this tool during my in silico vaccine design research for malaria, where I needed to analyze over 10 protein fasta files and cross-reference them with blast results.
# Author
Pooja Thummar
