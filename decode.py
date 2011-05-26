#!/usr/bin/python

import sys
from math import *

def pfactor(x):
	factorlist = []

	if x == 1:
		factorlist.append(x)

	while x % 2 == 0:
		factorlist.append(2)
		x /= 2

	limit = 1 + int(sqrt(x))
	for factor in range(3, limit, 2):
		while x % factor == 0:
			factorlist.append(factor)
			x /= factor

	if x > 1:
		factorlist.append(x)

	return factorlist

if len(sys.argv) != 1 + 2:
	charset = ' Wadefhlnost'
	# all 23 prime factors are of order 1
	s = 13682311570832829480888979137834570837851469148689544502986
else:
	charset = sys.argv[1]
	s = int(sys.argv[2])
modulo = len(charset)
while len(pfactor(modulo)) != 1:
	modulo += 1

num = iter(range(2, 9999))
while s != 1 :
        n = num.next()
        if s % n == 0 :
                sys.stdout.write("%s" % charset[(n - 1) % modulo])
		print " n= %d, %d * %d + %d, pfactor(n - 1) = (%s)" % (
			n,
			(n - 1) / modulo,
			modulo, (n - 1) % modulo,
			str(pfactor(n - 1)),)
                s /= n
sys.stdout.write("\n")
