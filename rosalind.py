import sys
from Bio.Seq import Seq
from Bio import SeqIO

def gc_content(s):
    return 100.0 * (s.count('C') + s.count('G')) / len(s)

def dna(s):
    seq = Seq(s)
    print seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')

def rna(s):
    print Seq(s).transcribe()

def revc(s):
    print Seq(s).reverse_complement()

def gc(stdin):
    max_record = max(SeqIO.parse(stdin, 'fasta'),
            key = lambda record: gc_content(record.seq))
    print max_record.name
    print gc_content(max_record.seq)

#dna(raw_input())
#rna(raw_input())
#revc(raw_input())
gc(sys.stdin)
