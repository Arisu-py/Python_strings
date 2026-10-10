import re


s = input('Введите строку: ')

words = re.findall(r'\S+', s)
reverse_words = [words[i] for i in range(len(words) - 1, -1, -1)]
reverse_letters = [s[i] for i in range(len(s) - 1, -1, -1)]

print(s, '-', ' '.join(reverse_words))
print(s, '-', ''.join(reverse_letters))
