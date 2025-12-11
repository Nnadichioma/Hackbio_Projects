"""
# Script Name: team_leucine_info.py
# Author: Chioma Nnadi
# Purpose:
   # This script stores information about team members (Team Leucine) and performs basic bioinformatics analysis on their favorite gene sequences.
    #Analyses include:
       # - Validating DNA sequences
       # - Computing GC content
        #- Translating DNA to protein
# GitHub: https://github.com/Nnadichioma
# LinkedIn: https://www.linkedin.com/in/NnadiChioma/
"""

# Team Leucine info
team_leucine_info = [
    {
        "Name": "Chioma Nnadi",
        "Slack": "Chioma",
        "Country": "Nigeria",
        "Hobby": "Writing",
        "Affiliation": "None",
        "Gene": "BRCA1",
        "Sequence": "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC"
    },

    {
        "Name": "Kashish Arora",
        "Slack": "Kashish",
        "Country": "India",
        "Hobby": "Reading",
        "Affiliation": "University of Glasgow",
        "Gene": "CDKN1A",
        "Sequence": "GAACATGTCCCAACATGTTG"
    },

    {
        "Name": "Keola Merl Joanes",
        "Slack": "Keola",
        "Country": "India",
        "Hobby": "Reading",
        "Affiliation": "PCCAS",
        "Gene": "HBB gene",
        "Sequence": "GGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA"
    },

    {
        "Name": "Lavinia Dorothea F Joseph",
        "Slack": "Lavinia",
        "Country": "Antigua & Barbuda",
        "Hobby": "Sudoku",
        "Affiliation": "University Mohammed V, Faculty of Medicine and Pharmacy",
        "Gene": "DHh gene",
        "Sequence": "GTTCCAGGTAGTGCCTGAAACTACTTTTCTGAAGAAGTATAATTAAAAGTAATCTTGTTTTGAGAA"
    },

    {
        "Name": "Atairoro Joshua",
        "Slack": "Atairoro Joshua",
        "Country": "Nigeria",
        "Hobby": "Music",
        "Affiliation": "None",
        "Gene": "BRCA1",
        "Sequence": "ATGGAAGTTGTCATTTTATAAAGTCAGTAGTTTCTTTGGCAGCAATGCCAGGAAAGGCTCTGAGGAA"
    },

    {
        "Name": "Bezaleel Akinbami",
        "Slack": "B3z",
        "Country": "Nigeria",
        "Hobby": "Gaming",
        "Affiliation": "None",
        "Gene": "None",
        "Sequence": "None"
    },

    {
        "Name": "Sharon Addy",
        "Slack": "Sharon Addy",
        "Country": "Ghana",
        "Hobby": "Reading",
        "Affiliation": "None",
        "Gene": "MIR1-1",
        "Sequence": "UGGAAUGUAAAGAAGUAUGUAU"
    },

    {
        "Name": "Jegede Joseph.O",
        "Slack": "Joseph",
        "Country": "Nigeria",
        "Hobby": "Gaming",
        "Affiliation": "Obafemi Awolowo University",
        "Gene": "None",
        "Sequence": "None"
    }
]

# Function to display team information
# Validate DNA sequence

def validate_dna(seq):
    """Validate that a sequence contains only DNA bases A, T, C, G"""
    if seq is None or seq.upper() == "NONE":
        return False
    valid_bases = {"A", "T", "C", "G"}
    return set(seq.upper()).issubset(valid_bases)

# Calculate GC content
def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)

# Translate DNA to protein
def translate_dna(seq):
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein += codon_table.get(codon, '')
    return protein

# Analyze each team member's gene sequence
for member in team_leucine_info:
    name = member["Name"]
    gene = member["Gene"]
    sequence = member["Sequence"]
    print(f"Analyzing {name}'s gene: {gene}")
    
    if validate_dna(sequence):
        gc = gc_content(sequence)
        protein = translate_dna(sequence)
        print(f"  Valid DNA sequence.")
        print(f"  GC Content: {gc}%")
        print(f"  Translated Protein: {protein}\n")
    else:
        print(f"  Invalid DNA sequence or no sequence provided.\n")


