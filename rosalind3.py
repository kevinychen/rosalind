import sys
from Bio.Seq import Seq
from Bio.Motif import Motif
from Bio.Alphabet import IUPAC
from Bio import SeqIO, Restriction

def reverse_palindrome(s):
    return str(s) == str(s.reverse_complement())

def restriction_enzyme_search(s):
    # not used; just example of searching for specific restriction enzyme site
    return Restriction.EcoRI.search(Seq(s))

def iev(s):
    # AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
    dist = [int(i) for i in s.split(' ')]
    print 2 * (dist[0] + dist[1] + dist[2] + .75 * dist[3] + .5 * dist[4])

def subs(s, t):
    m = Motif(alphabet = IUPAC.unambiguous_dna)
    m.add_instance(Seq(t, m.alphabet))
    print ' '.join([str(pos + 1) for pos, seq in m.search_instances(Seq(s))])

def revp(stdin):
    seq = SeqIO.read(stdin, 'fasta').seq
    for length in xrange(4, 13):
        for start in xrange(len(seq) - length + 1):
            if reverse_palindrome(seq[start:start+length]):
                print start + 1, length

#iev(raw_input())
#subs(raw_input(), raw_input())
revp(sys.stdin)
