import sys
from Bio import SeqIO, motifs

def cons(stdin):
    m = motifs.create([record.seq for record in SeqIO.parse(stdin, 'fasta')])
    print m.consensus
    for c in 'ACGT':
        print c + ': ' + ' '.join(map(str, m.counts[c]))

cons(sys.stdin)
