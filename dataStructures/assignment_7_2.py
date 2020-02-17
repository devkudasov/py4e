# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total = 0
count = 0

for line in fh:
    if 'X-DSPAM-Confidence:' in line:
        iPos = line.find(':')
        total += float(line[iPos + 1:].strip())
        count += 1

print('Average spam confidence:', total / count)
