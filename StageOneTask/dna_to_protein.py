# Task 1: Write a python function for translating DNA to protein

# Define a function that takes a DNA sequence as input and returns the translated protein

def translate_dna_to_protein(dna_sequence):
    # Dictionary that maps DNA codons (groups of 3 bases) to amino acids (single-letter codes)
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',   # Isoleucine, Methionine (start)
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',   # Threonine
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',   # Asparagine, Lysine
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',   # Serine, Arginine
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',   # Leucine
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',   # Proline
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',   # Histidine, Glutamine
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',   # Arginine
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',   # Valine
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',   # Alanine
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',   # Aspartic acid, Glutamic acid
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',   # Glycine
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',   # Serine
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',   # Phenylalanine, Leucine
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',   # Tyrosine, Stop codons (_)
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',   # Cysteine, Tryptophan
    }
    
    # Create an empty string to store the resulting protein sequence
    protein_sequence = ""
    
    # Process the DNA sequence three letters (one codon) at a time
    for i in range(0, len(dna_sequence), 3):
        # Extract a group of 3 bases (a codon) from the DNA sequence
        codon = dna_sequence[i:i+3]
        
        # Check if the codon has exactly 3 bases
        if len(codon) == 3:
            # Look up the corresponding amino acid from the codon table
            # If the codon is not found, return an empty string ('')
            amino_acid = codon_table.get(codon, '')
            
            # Add the amino acid to the growing protein sequence
            protein_sequence += amino_acid
            
    # Return the full translated protein sequence
    return protein_sequence


# DNA sequence
dna_seq = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGACCGATAG"

# Call the translation function and store the protein result
protein_seq = translate_dna_to_protein(dna_seq)

# Print both the original DNA sequence and the resulting protein sequence
print("DNA Sequence: ", dna_seq)
print("Protein Sequence: ", protein_seq)

# Task 2: Write a python function for calculating the hamming distance between your 
# slack username (e.g josoga) and twitter/X (joseph) handle (synthesize one if you don’t have one).
# Feel free to pad it with extra words if they are not of the same length.

def hamming_distance(name1, name2):
    # Make both names equal length by padding the shorter one with spaces
    max_length = max(len(name1), len(name2))
    name1 = name1.ljust(max_length)  #ljust pads the shorter name with spaces on the right
    name2 = name2.ljust(max_length)
    
    # initialized a distance counter
    distance = 0
    #compare each character in both names
    for x, y in zip(name1, name2):  #zip pairs characters from both names
        if x != y:
            distance += 1
    
    return distance

# defined my slack username and twitter handle
slack_username = "Chioma"
twitter_handle = "your_tech_sista"

# Calculated and printed the hamming distance
distance = hamming_distance(slack_username, twitter_handle)
print(f"Hamming Distance between '{slack_username}' and '{twitter_handle}': {distance}")


# Surprise Task
# Reproduce the figures 1A-F below using Python Data Libraries (Pandas, Seaborn and maybe matplotlib)

# Part A – Gene Expression Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the provided URL
data_path = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/hbr_uhr_top_deg_normalized_counts.csv"
data_path_2 = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/hbr_uhr_deg_chr22_with_significance.csv"
data = pd.read_csv(data_path)
deg_data = pd.read_csv(data_path_2)

#set gene names as index
data = data.set_index('Unnamed: 0')
data.index.name = None

# to verify data is loaded correctly
print(data.head())
print(deg_data.head())
print(data.shape)
data.info()

# a. Heatmap
# Use the normalized gene expression dataset to plot a clustered heatmap of
# the top differentially expressed genes between HBR and UHR samples.
# Label both genes and samples.
# Use a color gradient (e.g., Blues) to indicate expression levels.

# Plot clustered heatmap
g = sns.clustermap(data, cmap='Blues', standard_scale=1, figsize=(8, 6))
g.figure.suptitle('Clustered Heatmap of Top Differentially Expressed Genes between HBR and UBR Samples', fontsize=14)
g.figure.subplots_adjust(top=0.9)
plt.show()

# b. Volcano Plot
# Plot log2FoldChange vs log10(Padj) from the DEG results.
# Color points by significance:
# Upregulated: green
# Downregulated: orange
# Not significant: grey
# Add dashed vertical lines at log2FoldChange = ±1.

# Map colors for significance
colors = {'up':'green', 'down':'orange', 'ns':'grey'}

# Plot volcano plot
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=deg_data,
    x='log2FoldChange',
    y='-log10PAdj',
    hue='significance',
    palette=colors,
    alpha=0.7
)

# Add dashed vertical lines at log2FoldChange = ±1
plt.axvline(x=1, color='black', linestyle='--')
plt.axvline(x=-1, color='black', linestyle='--')

# Labels and title
plt.xlabel('log2(Fold Change)')
plt.ylabel('-log10(PAdj)')
plt.title('Volcano Plot of DEGs')
plt.legend(title='Significance')

# Show plot
plt.show()

# Part B – Breast Cancer Data Exploration
# c. Scatter Plot (radius vs texture)
# Plot texture_mean vs radius_mean and color points by diagnosis (M = malignant, B = benign).

# Load breast cancer dataset
breast_cancer_data_path = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv"
breast_cancer_data = pd.read_csv(breast_cancer_data_path)

# to verify data is loaded correctly
print(breast_cancer_data.head())
print(breast_cancer_data.info())

# Plot scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=breast_cancer_data,
    x='radius_mean',
    y='texture_mean',
    hue='diagnosis',
    palette={'M':'red', 'B':'blue'},
    alpha=0.7
)
# Labels and title
plt.xlabel('Radius Mean')
plt.ylabel('Texture Mean')
plt.title('Scatter Plot of Texture Mean vs Radius Mean')
plt.legend(title='Diagnosis')
# Show plot
plt.show()

# d. Correlation Heatmap
# Compute the correlation matrix of six key features:
#radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean.
# Plot as a heatmap with correlation values annotated.
key_features = [
    'radius_mean', 'texture_mean', 'perimeter_mean',
    'area_mean', 'smoothness_mean', 'compactness_mean'
]
# Subset data
subset = breast_cancer_data[key_features]

# Compute correlation
corr_matrix = subset.corr()

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(
    corr_matrix,
    annot=True,    # show correlation values
    fmt=".1f",     # 2 decimal places
    cmap='Blues',
    vmin=-1, vmax=1,
    linewidths=0.5
)
plt.title("Correlation Heatmap of Key Breast Cancer Features", fontsize=14)
plt.xticks(rotation=40, ha='right', fontsize=7) 
plt.show()


# e. Scatter Plot (smoothness vs compactness)
# Plot compactness_mean vs smoothness_mean colored by diagnosis.
# Include gridlines and clear axis labels.

plt.figure(figsize=(8,6))
sns.scatterplot(
    data=breast_cancer_data,
    x='smoothness_mean',
    y='compactness_mean',
    hue='diagnosis',
    palette={'M':'red', 'B':'blue'},
    alpha=0.7
)
# Labels and title
plt.xlabel('Smoothness Mean')
plt.ylabel('Compactness Mean')
plt.title('Scatter Plot of Compactness Mean vs Smoothness Mean')
plt.legend(title='Diagnosis')
plt.grid(True)
# Show plot
plt.show()

# e. Density Plot (area distribution)
# Plot kernel density estimates (KDE) of area_mean for both M and B diagnoses on the same axis.
# Add legend and labeled axes.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

breast_cancer_data_path = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv"
breast_cancer_data = pd.read_csv(breast_cancer_data_path)

breast_cancer_data['diagnosis'].unique()
plt.figure(figsize=(8,6))
sns.kdeplot(
    data=breast_cancer_data,
    x='area_mean',
    fill=True,
    hue='diagnosis',
    palette={'M':'red', 'B':'blue'},
    common_norm=False,
    alpha=0.5
)
# Labels and title
plt.xlabel('Area Mean')
plt.ylabel('Density')
plt.title('Density Plot of Area Mean by Diagnosis')
plt.legend(title='Diagnosis', labels=['M', 'B'])
# Show plot
plt.show()