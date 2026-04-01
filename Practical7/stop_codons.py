import re
import matplotlib.pyplot as plt
from collections import Counter

target_stop=input("Enter one of the stop codons (TAA, TAG, TGA): ").strip().upper()
if target_stop not in ['TAA', 'TAG', 'TGA']:
    print("Invalid stop codon. Please enter TAA, TAG, or TGA.")
    exit()

input_file="Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
codon_counts=Counter()
pattern = re.compile(rf'(?=(ATG(?:[ACGT]{3})*?({target_stop})))')

def count_codons_in_seq(seq):
    matches=pattern.findall(seq)
    if matches:
        longest_orf = max(matches, key=lambda x: len(x[0]))[0]
        
        for i in range(0,len(longest_orf)-3,3):
            codon=longest_orf[i:i+3]
            codon_counts[codon]+=1

with open(input_file,'r') as infile:
    current_seq=""
    for line in infile:
        line=line.strip()
        if line.startswith(">"):
            if current_seq:
                count_codons_in_seq(current_seq)
            current_seq=""
        else:
            current_seq+=line
        
    if current_seq:
        count_codons_in_seq(current_seq)

if not codon_counts:
    print(f"No ORFs found ending with {target_stop}.")
    exit()

labels=list(codon_counts.keys())
sizes=list(codon_counts.values())
plt.figure(figsize=(12, 10))
plt.pie(sizes, labels=labels, startangle=140, textprops={'fontsize': 8})
plt.axis('equal')
plt.title(f'Upstream In-Frame Codon Distribution for Longest ORFs ending in {target_stop}')
output_image=f'codon_distribution_{target_stop}.png'
plt.savefig(output_image, bbox_inches='tight')
print(f"Pie chart successfully generated and saved to '{output_image}'.")