#initialise sequence, longest orf, longest length
#define start/stop codon
seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start_codon='AUG'
stop_codon={'UAA','UAG','UGA'}
longest_orf=''
longest_length=0

#scan all possible start positions, double cycle
for i in range(len(seq)-2):
    if seq[i:i+3]==start_codon:
        for j in range(i,len(seq)-2,3):
            current_codon=seq[j:j+3]
            if current_codon in stop_codon:
                current_orf=seq=seq[i:j+3]
                current_length=len(current_orf)
                if current_length>longest_length:
                    longest_length=current_length
                    longest_orf=current_orf
                break

#print the results
print(f'the longest orf sequence is {longest_orf} and the length of the longest orf(nucleotides) is {longest_length}')           