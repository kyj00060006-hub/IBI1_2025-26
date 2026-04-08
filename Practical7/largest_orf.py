import re
seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
#regex
pattern=re.compile(r'(?=(AUG(?:(?!UAA|UAG|UGA)[ACGU]{3})*(?:UAA|UAG|UGA)))')
matche=pattern.findall(seq)

if matche:
    longest_orf=max(matche,key=len)
    print(f"Longest ORF: {longest_orf}")
    print(f"Length: {len(longest_orf)} nucleotides")
else:
    print("No ORF found in the given sequence.")