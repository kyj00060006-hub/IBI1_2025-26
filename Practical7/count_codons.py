import re
import matplotlib.pyplot as plt
from collections import Counter # Counter: not taught in course, learned from Python docs. Efficiently counts hashable objects.

#read the file
def read_fasta(filename):
    genes={}
    current_id=None
    current_seq=[]
    with open(filename,'r') as f:
        for line in f:
            line=line.strip()
            if line.startswith('>'):
                if current_id:
                    genes[current_id] = ''.join(current_seq)
                #regex gene name
                match=re.search(r'gene:(\w+)', line)
                current_id=match.group(1) if match else line.split()[0][1:]
                current_seq=[]
            else:
                current_seq.append(line)
        if current_id:
            genes[current_id]=''.join(current_seq)
    return genes

#the longest ORF
def get_longest_orf(seq, stop_target):
    pattern=re.compile(r'ATG(?:(?!' + stop_target + r')...)*' + stop_target)
    orfs=pattern.findall(seq)
    if not orfs:
        return None
    return max(orfs, key=len)

#split ORF into 3 and remove the last one
def split_codons(orf):
    if len(orf)<6:
        return[]
    coding=orf[:-3]
    return [coding[i:i+3] for i in range(0,len(coding),3) if len(coding[i:i+3])==3]

#main
if __name__=='__main__':
    #stop codon
    stop_target=input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()
    if stop_target not in ['TAA','TAG','TGA']:
        print("Invalid codon!")
        exit()

    #read FASTA
    genes=read_fasta("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")

    all_codons=[]
    for gene_name,seq in genes.items():
        best_orf=get_longest_orf(seq, stop_target)
        if not best_orf:
            continue
        codons=split_codons(best_orf)
        all_codons.extend(codons)

    if not all_codons:
        print(f"No ORFs ending with {stop_target}")
        exit()

    count=Counter(all_codons)
    print(f"\nCodon frequencies upstream of {stop_target}:")
    for codon,num in count.most_common(10):
        print(f"{codon}: {num}")

#generate pie chart
labels=list(count.keys())
sizes=list(count.values())
plt.figure(figsize=(10,7))
wedges,texts,autotexts=plt.pie(
    sizes,
    autopct=lambda p:f'{p:.1f}%'if p>1.5 else '',
    textprops={'fontsize':7},
    pctdistance=0.8
)
plt.legend(wedges,labels,title='Codon',loc='center left',
           bbox_to_anchor=(1, 0.5, 0, 1), ncol=2, fontsize=7)
plt.title(f'Codon distribution upstream of {stop_target}')
plt.tight_layout()
plt.savefig(f"codon_pie_{stop_target}.png",dpi=300,bbox_inches='tight')
plt.close()