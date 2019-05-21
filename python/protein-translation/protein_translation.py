CODON_LENGTH = 3

CODON_TO_PROTEIN = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan'
}

STOP_CODONS = ['UAA', 'UAG', 'UGA']


def split_strand(strand):
    return [strand[i:i + CODON_LENGTH]
            for i in range(0, len(strand), CODON_LENGTH)]


def proteins(strand):
    polypeptide = []
    for codon in split_strand(strand):
        if codon in STOP_CODONS:
            return polypeptide
        else:
            polypeptide.append(CODON_TO_PROTEIN[codon])
    return polypeptide
