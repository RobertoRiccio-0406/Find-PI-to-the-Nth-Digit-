def to_rna(dna_strand):
    if not dna_strand:
        return ''
    temp = list(dna_strand)
    rna = []
    
    for chr in range(len(temp)):
        if temp[chr] == 'G':
            rna.append("C")
        if temp[chr] == 'C':
            rna.append("G")
        if temp[chr] == 'T':
            rna.append("A")
        if temp[chr] == 'A':
            rna.append("U")
    return ''.join(rna)
