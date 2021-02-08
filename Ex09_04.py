fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    else:
        counts[words[1]] = counts.get(words[1],0)+1

bigsender = None
bigcount = None

for k, v in counts.items():
    if bigcount is None or v > bigcount:
        bigsender = k
        bigcount = v
print(bigsender, bigcount)
