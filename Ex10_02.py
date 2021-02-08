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
        hr = words[5][:2]
        counts[hr] = counts.get(hr,0)+1

lst = sorted([ (k,v) for k,v in counts.items() ])

for (k,v) in lst:
    print(k,v)
