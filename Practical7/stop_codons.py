import re

def read_fasta(filename):
    genes={}
    current_id=None
    current_seq=[]
    with open(filename,'r') as f:
        for line in f:
            line=line.strip()
            if line.startswith('>'):
                if current_id:
                    genes[current_id]=''.join(current_seq)
                match=re.search(r'gene:(\w+)',line) # Extract gene name
                current_id=match.group(1) if match else line.split()[0][1:] # Fallback if 'gene:' not found
                current_seq=[]
            else:
                current_seq.append(line)
        if current_id:
            genes[current_id]=''.join(current_seq)
    return genes

def find_in_frame_stop_codons(sequence):
    stop_codons={'TAA','TAG','TGA'}
    found_stop_codons=set()
    # Find all potential ORFs starting with 'ATG'
    # The regex captures the entire ORF, and also the specific stop codon found at the end.
    # Using lookahead to find all possible ORFs, even overlapping ones.
    # The first group captures the entire ORF, the second group captures the stop codon.
    pattern =re.compile(r'(?=(ATG((?:[ACGT]{3})*?)(TAA|TAG|TGA)))')
    
    for match in pattern.finditer(sequence):
        full_orf=match.group(1) # The entire ORF
        stop_codon=match.group(4) # The specific stop codon (TAA, TAG, TGA)
        if stop_codon in stop_codons:
            found_stop_codons.add(stop_codon)
            
    return list(found_stop_codons) if found_stop_codons else None

if __name__=='__main__':
    input_fasta_file="Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_fasta_file="stop_genes.fa"

    all_genes=read_fasta(input_fasta_file)

    genes_with_stop_codons={}

    for gene_name, sequence in all_genes.items():
        found_stops=find_in_frame_stop_codons(sequence)
        if found_stops:
            genes_with_stop_codons[gene_name]={'sequence': sequence, 'stops': found_stops}

    with open(output_fasta_file,'w') as outfile:
        for gene_name, data in genes_with_stop_codons.items():
            stops_str=", ".join(sorted(data['stops']))
            outfile.write(f">{gene_name} Stop_Codons:{stops_str}\n")
            # Write sequence, breaking into 60 characters per line
            for i in range(0,len(data['sequence']),60):
                outfile.write(data['sequence'][i:i+60]+'\n')

    print(f"Processed {len(all_genes)} genes. Found {len(genes_with_stop_codons)} genes with in-frame stop codons.")
    print(f"Results written to {output_fasta_file}")