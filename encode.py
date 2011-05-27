#!/usr/bin/python

import sys
import random
import itertools
from math import sqrt

class Pfactor(object):
	def __init__(self):
		# bah, not implemented
		self.cache = []
	
	def __call__(self, x):
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
pfactor = Pfactor()

if len(sys.argv) != 1 + 1:
	msg = "What a load of nonsense"
else:
	msg = sys.argv[1]
charset_letters = sorted(list(set(msg)))
# optional, output different results
random.shuffle(charset_letters)
modulo = len(charset_letters)
while len(pfactor(modulo)) != 1:
	modulo += 1

limit = 9999
# The limit is there for two reasons:
# * it's in original.py
# * I'm not certain that all charset permutations are valid, that would be the
#   case if the following conjecture is verified:
# 	  m is prime, n is part of the natural numbers
# 	  there is no i part of the natural numbers and i < m such that
# 	  n * m + i is never prime
#   In this case, n is candidate, m is modulo and i is index
for charset in itertools.permutations(charset_letters):
	factor = []
	n = 0
	for letter in msg:
		index = charset.index(letter)
		candidate = n * modulo + index + 1
		# find the smallest n such that:
		#    factor[i] = n * modulo + index + 1 is prime and
		#    factor[i] > factor[i - 1]
		while candidate < limit and not (
			len(pfactor(candidate)) == 1 and (len(factor) == 0 or
			candidate > factor[-1])):
			n += 1
			candidate = n * modulo + index + 1

		if candidate >= limit:
			continue
		else:
			print "factor= %d, %d * %d + %d + 1" % (candidate, n, modulo, index,)
			factor.append(candidate)

	if candidate >= limit:
		print "next try"
		continue
	else:
		print modulo
		print "".join(charset)
		print reduce(lambda o1, o2: o1 * o2, factor)
		sys.exit()
