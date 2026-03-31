import matplotlib.pyplot as plt
from collections import Counter

def parse_fasta(filename):
    genes =[]
    header=''
    seq=''
    with open(filename,'r') as f:
        for line in f:
            line=line.strip()
            if line.startswith('>'):
                if header:
                    genes.append((header, seq))
                header=line
                seq=''
            else:
                seq+=line
        if header:
            genes.append((header, seq))
    return genes

def get_longest_orf_up_to_stop(seq,target_stop):
    longest_codons=[]
    for i in range(len(seq)-2):
        if seq[i:i+3]=='ATG':
            codons=[]
            for j in range(i, len(seq)-2, 3):
                codon=seq[j:j+3]
                if codon==target_stop:
                    if len(codons)>len(longest_codons):
                        longest_codons=codons.copy()
                    break
                codons.append(codon)
    return longest_codons

#main
def main():
    filename='Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    genes = parse_fasta(filename)
    target = input("input(TAA/TAG/TGA):").strip().upper()
    if target not in ('TAA','TAG','TGA'):
        print("input again! u can only input TAA/TAG/TGA")
        return
    
    all_codons=[]
    for _, seq in genes:
        codons=get_longest_orf_up_to_stop(seq,target)
        all_codons.extend(codons)
    counter=Counter(all_codons)
    print("Codon counts:")
    for codon,cnt in counter.most_common(10):
        print(f"{codon}: {cnt}")
    
    #generate the pie chart
    labels=list(counter.keys())
    sizes=list(counter.values())
    plt.figure(figsize=(10,10))
    plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)
    plt.title(f'Codon distribution upstream of {target}')
    plt.savefig('codon_pie.png',dpi=300,bbox_inches='tight')
    plt.close()
    print("the pie chart is saved as codon_pie.png")

if __name__ == '__main__':
    main()