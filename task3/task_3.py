import re


text = input('Введите текст: ')

splitted_text = re.findall(r"\b\w+\b", text.lower())
counted_words = {}

for word in splitted_text:
    counted_words[word] = counted_words.get(word, 0) + 1

sorted_words = sorted(counted_words.items(), key=lambda x: x[1], reverse=True)

for i in range(min(5, len(splitted_text))):
    print(sorted_words[i][0])
