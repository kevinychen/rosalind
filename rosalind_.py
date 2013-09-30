import fileinput as fp
from string import maketrans

def dna(s):
    print s.count('A'), s.count('C'), s.count('G'), s.count('T')

def rna(s):
    print s.replace('T', 'U')

def revc(s):
    print s[::-1].translate(maketrans("ACGT", "TGCA"))

def gc(lines):
    dnas = []
    for line in lines:
        if line[0] == '>':
            dnas.append({'label': line[1:-1], 'string': ''})
        else:
            dnas[-1]['string'] += line[:-1]

    def gc_content(s):
        return 100.0 * (s.count('C') + s.count('G')) / len(s)
    for dna in dnas:
        dna['gc_content'] = gc_content(dna['string'])

    max_gc_content_dna = max(dnas, key=lambda dna: dna['gc_content'])
    print max_gc_content_dna['label']
    print max_gc_content_dna['gc_content']

