
text_file = open("pg2600.txt", 'r', encoding="utf-8")
many_lines = text_file.readlines()
wordCounts ={}
for line in many_lines:
    words = line.split(' ')
    for word in words:
        pass
