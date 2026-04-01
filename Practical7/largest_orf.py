import re
seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
#Regex
pattern=re.compile(r'(?=(AUG(?:[ACGU]{3})*?(?:UAA|UAG|UGA)))')
#find all matches through lookahead group
matche=pattern.findall(seq)

if matche:
    longest_orf=max(matche,key=len)
    print(f"Longest ORF:{longest_orf}")
    print(f"Length:{len(longest_orf)} nucleotides")
else:
    print("No ORF found in the given sequence.")