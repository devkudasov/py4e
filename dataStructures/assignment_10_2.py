fhand = open('mbox-short.txt')

hours = dict()

for line in fhand:
    if line.startswith('From '):
        key = line.split()[5].split(':')[0]
        hours[key] = hours.get(key, 0) + 1

[print(key, val) for (key, val) in sorted(hours.items())]
