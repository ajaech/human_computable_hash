# Blum's Human Computable Machine Unbreakable Hash Function (HCMU)
# Algorithm copied from:
# http://www.scilogs.com/hlf/mental-cryptography-and-good-passwords/
# Video description from Manuel Blum
# http://www.heidelberg-laureate-forum.org/blog/video/lecture-monday-september-22-2014-manuel-blum/
import argparse
import random
import string


parser = argparse.ArgumentParser()
parser.add_argument('input', help='input string to hash')
parser.add_argument('--seed', help='set the random seed')
parser.add_argument('--verbose', help='print out the random secrets',
                    action='store_true')
args = parser.parse_args()

# set the random seed value
if args.seed:
  random.seed(args.seed)
else:
  random.seed(666)

INPUT = args.input.lower()  # convert the input to lower case

# generate a random permutation of the digits 0-9 and call it g
g = range(10)
random.shuffle(g)
# build a lookup table for the permutation
g_lookup = dict(zip(g, g[1:] + [g[0]]))

# this defines the allowable characterset
alphabet = list(string.ascii_lowercase + string.digits)
f = [random.randint(0, 9) for _ in alphabet]
f_lookup = dict(zip(alphabet, f))  # map each character to a digit

# print the random secrets
if args.verbose:
  print 'random mapping f:'
  print f_lookup

  print 'random permutation g:'
  print g


# map the input to digits
a = [f_lookup[char] for char in INPUT if char in f_lookup]

# only hash strings that have at least two digits in the character set
if len(a) < 2:
  print 'ERROR: input is too short. Could not hash.'
  exit()

# compute the hash
b = []
b_prev = a[-1]
for i in a:
  b_prev = g_lookup[(b_prev + i) % 10]
  b.append(b_prev)

print ''.join([str(digit) for digit in b])
