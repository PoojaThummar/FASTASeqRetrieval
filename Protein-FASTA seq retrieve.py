from Bio import Entrez, SeqIO

Entrez.email = "____@gmail.com"
with open("potein_accession_no.txt") as accession:
    accession_numbers = accession.read().splitlines()
handle = Entrez.efetch(db="protein", id=accession_numbers, rettype="fasta", retmode="text")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()

# Writing the sequences to a file
with open("output_sequences.fasta", "w") as o:
    SeqIO.write(records, o, "fasta")
