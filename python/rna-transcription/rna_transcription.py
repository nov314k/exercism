DNA_TO_RNA = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_strand):
    rna = ''
    for nucleotide in dna_strand:
        rna += DNA_TO_RNA[nucleotide]
    return rna
