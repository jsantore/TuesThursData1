import string
translator = str.maketrans('', '', string.punctuation)
text_file = open("pg2600.txt", 'r', encoding="utf-8")
many_lines = text_file.readlines()
wordCounts ={}
for line in many_lines:
    words = line.split(' ')
    for word in words:
        bare_word = word.translate(translator)
        bare_word = bare_word.lower()
        bare_word = bare_word.strip()
        if bare_word not in wordCounts:
            wordCounts[bare_word] = 1
        else:
            wordCounts[bare_word] += 1
for word, count in wordCounts.items():
    print(f"{word}: \t{count}")
