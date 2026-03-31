#read FASTA and find the target genes
def parse_fasta(filename):
    genes=[]
    header=''
    seq=''
    with open(filename,'r') as f:
        for line in f:
            line=line.strip()
            if line.startswith('>'):
                if header:
                    genes.append((header,seq))
                header=line
                seq=''
            else:
                seq+=line
        if header:
            genes.append((header, seq))
    return genes

def check_in_frame_stop(seq):
    stops={'TAA','TAG','TGA'}
    #start with ATG to examine stop codons
    for i in range(len(seq)-2):
        if seq[i:i+3]=='ATG':
            for j in range(i,len(seq)-2,3):
                codon=seq[j:j+3]
                if codon in stops:
                    return True,stops.intersection(set(seq[j:j+3] for j in range(i,len(seq)-2,3)))
    return False,set()

#main
input_fa='Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_fa='stop_genes.fa'

genes=parse_fasta(input_fa)

with open(output_fa,'w') as out:
    for header,seq in genes:
        has_stop,stop_types=check_in_frame_stop(seq)
        if has_stop:
            #gene name(simplified)
            gene_name=header.split()[0].replace('>', '')
            stop_str=','.join(sorted(stop_types))
            out.write(f'>{gene_name} stops:{stop_str}\n')
            out.write(seq + '\n')

print("Succeed! The result is saved in stop_genes.fa")