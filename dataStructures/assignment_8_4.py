fhand = open('romeo.txt')
resultList = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in resultList:
            resultList.append(word)

resultList.sort()

print(resultList)
