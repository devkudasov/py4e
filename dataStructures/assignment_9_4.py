fhand = open('mbox-short.txt')

senders = dict()

for line in fhand:
    if line.startswith('From '):
        key = line.split()[1]
        senders[key] = senders.get(key, 0) + 1

count = 0
biggestSender = None

for sender, total in senders.items():
    if count < total:
        count = total
        biggestSender = sender

print(biggestSender, count)
