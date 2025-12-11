""" x = y = z = "Orange"
print(x)
print(y)
print(z)

x = 2
print(type(x)) 


a = 2
a = 3
A = 5
#print(a)
#print(A) 



# Assign values
expression_1 = 554
expression_2 = 789

# Add expression_1 and expression_2
total_expression = expression_1 + expression_2

# Assign sample size
sample_size = 15

# Divide total_expression by sample_size
average_expression = total_expression / sample_size

# Multiply expression_1 and expression_2
expression_product = expression_1 * expression_2

# Calculate the difference between expression_1 and expression_2
difference = expression_2 - expression_1

# Calculate expression fold change
fold_change = (expression_2 - expression_1) / expression_2

# Print results
print("Expression 1:", expression_1)
print("Expression 2:", expression_2)
print("Total Expression:", total_expression)
print("Average Expression:", average_expression)
print("Expression Product:", expression_product)
print("Difference:", difference)
print("Fold Change:", fold_change)


# List of DNA sequences
sequence = ["ATGCGTAC", "GCTTAGCT", "CGTACGTA"]

# Loop through each sequence
for seq in sequence:
    # Count the bases
    g_count = seq.count("G")
    c_count = seq.count("C")
    total_length = len(seq)
    
    # Calculate GC content
    gc_content = ((g_count + c_count) / total_length) * 100
    
    # Print details
    print(f"Sequence: {seq}")
    print(f"  Length: {total_length}")
    print(f"  G count: {g_count}")
    print(f"  C count: {c_count}")
    print(f"  GC Content: {gc_content:.2f}%\n")
    

x = 2

def my_function():
    #global x
    x = 5
    #print("Value of x inside function:", x)

my_function()
print("Value of x outside function:", x)

a = "Hello"
b = "World"
print(a+b)
"""

"""ninitial_population = 200
growth_rate = 1.03
for generation in range(1, 16):
    population = initial_population * (growth_rate ** generation)
    print(f"Generation {generation}: Population = {int(population)}")


def gc_content(sequence):
    dna_sequence = "ATGCGTAC"
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    gc_content_percentage = ((g_count + c_count) / len(sequence)) * 100
    return gc_content_percentage

# Define the sequence here
dna_sequence = "ATGCGTAC"

gc = gc_content(dna_sequence)
print(f"GC content of {dna_sequence}: {gc:.2f}%")


#Write a function to calculate the AT content of a DNA sequence.

def at_content(sequence):
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    at_content_percentage = ((a_count + t_count) / len(sequence)) * 100
    return at_content_percentage

dna_sequence = "ATGCGTAC"

at = at_content(dna_sequence)
print(f"AT content of {dna_sequence}: {at:.2f}%")

def gc_content(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    gc = ((g + c) / len(sequence)) * 100
    return gc

result = gc_content("ATGC")
print(result)

import pandas as pd
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

df = pd.DataFrame(data)

#print(df)

print(df.loc[0:2])


import seaborn as sns
import pandas as pd
df = sns.load_dataset("penguins")
# scatterplot of bill length vs bill depth
#sns.scatterplot(df, x="bill_length_mm", y="bill_depth_mm", hue="species", style="sex")
#sns.histplot(df, x="flipper_length_mm")
#sns.catplot(df, x="species", y="bill_length_mm")
#sns.catplot(df, x="species", y="bill_length_mm", kind="swarm", hue="sex")
#sns.jointplot(df, x="bill_length_mm", y="bill_depth_mm", hue="species", height=4)
sns.pairplot(data=df, hue="species")
"""
