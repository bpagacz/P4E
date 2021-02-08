# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
cnt_spam = 0
x_spam = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        cnt_spam +=1
        x_spam = x_spam + float(line.strip()[20:])
avg = x_spam / cnt_spam
print("Average spam confidence:",avg)
