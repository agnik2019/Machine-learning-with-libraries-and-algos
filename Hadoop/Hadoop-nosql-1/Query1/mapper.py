import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    print('%s\t%s' % (words[0],1))