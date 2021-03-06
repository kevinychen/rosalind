from Bio.Seq import Seq

# calculate n choose 2
def c2(n):
    return n * (n - 1) / 2

def fib(s):
    n, k = map(int, s.split(' '))
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a * k + b
    print a

def hamm(s, t):
    print sum([c != d for c, d in zip(s, t)])

def prot(s):
    print Seq(s).translate(to_stop = True)

def iprb(s):
    k, m, n = map(int, s.split(' '))
    print (c2(k) + k * m + .75 * c2(m) + k * n + .5 * m * n) / c2(k + m + n)

#fib(raw_input())
#hamm(raw_input(), raw_input())
#prot(raw_input())
iprb(raw_input())
