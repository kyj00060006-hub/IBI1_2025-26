import re
input_file="Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file="stop_genes.fa"
pattern=re.compile(r'(?=(ATG(?:[ACGT]{3})*?(TAA|TAG|TGA)))')

def process_and_write(seq_id,seq,outfile):
    if not seq_id or not seq:
        return
    matches=pattern.findall(seq)
    if matches:
        found_stop_codons=set([m[1] for m in matches])
        stop_str=",".join(sorted(list(found_stop_codons)))
        outfile.write(f">{seq_id};{stop_str}\n")
        outfile.write(f"{seq}\n")

with open(input_file,'r') as infile,open(output_file,'w') as outfile:
    current_id=""
    current_seq=""
    
    for line in infile:
        line=line.strip()
        if line.startswith(">"):
            process_and_write(current_id, current_seq, outfile)
            current_id=line.split()[0][1:]
            current_seq=""
        else:
            current_seq+=line
    process_and_write(current_id,current_seq,outfile)

print(f"Processing complete. Results saved to {output_file}.")