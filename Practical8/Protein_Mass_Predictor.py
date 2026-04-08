AMINO_ACID_MASSES={
    'G':57.02,#Glycine
    'A':71.04,#Alanine
    'S':87.03,#Serine
    'P':97.05,#Proline
    'V':99.07,#Valine
    'T':101.05,#Threonine
    'C':103.01,#Cysteine
    'I':113.08,#Isoleucine
    'L':113.08,#Leucine
    'N':114.04,#Asparagine
    'D':115.03,#Aspartic Acid
    'Q':128.06,#Glutamine
    'K':128.09,#Lysine
    'E':129.04,#Glutamic Acid
    'M':131.04,#Methionine
    'H':137.06,#Histidine
    'F':147.07,#Phenylalanine
    'R':156.10,#Arginine
    'Y':163.06,#Tyrosine
    'W':186.08#Tryptophan
}

def predict_protein_mass(amino_acid_sequence):
    total_mass=0.0
    for amino_acid in amino_acid_sequence.upper():
        if amino_acid in AMINO_ACID_MASSES:
            total_mass+=AMINO_ACID_MASSES[amino_acid]
        else:
            raise ValueError(f"Error: Unknown amino acid '{amino_acid}' found in the sequence. Please check the supplied amino acids")
    return total_mass

#Example usage
print("\n--Protein Mass Predictor--")

#Example1 normal usage
try:
    sequence1="ARNDCEQGHILKMFPSTWYV"
    mass1=predict_protein_mass(sequence1)
    print(f"Example 1 (Normal): The total mass of sequence '{sequence1}' is {mass1:.2f} amu")
except ValueError as e:
    print(e)
    
#Example2 wrong usage
try:
    sequence2="KYJ"
    print(f"\nExample 2 (wrong input)'{sequence2}'):")
    mass2=predict_protein_mass(sequence2)
    print(f"This will not print: {mass2}")
except ValueError as e:
    print(f"Caught expected error: {e}")

#input
try:
    sequence_input=input('\nInput Your Sequence:')
    mass=predict_protein_mass(sequence_input)
    print(f'The total mass of protein in sequence "{sequence_input}" is: {mass:.2f} amu')
except ValueError as e:
    print(f"Error in your input: {e}")
