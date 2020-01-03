from gmpy2 import *
from Crypto.Util.number import *


p = 804811499343607200702893651293
q = 839348502408870119614692320677
e = 65537
c = 0xe3712876ea77c308083ef596a32c5ce2d7edf22abbc58657e

n = p * q
phi = (p-1) * (q-1)
d = invert(e, phi) # d = divm(1, e, phi)

print ('%x' % pow(c, d, n)).decode("hex")
