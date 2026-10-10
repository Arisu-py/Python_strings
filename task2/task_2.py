import re


print('Введите текст:')

list_text = []
user_text = input()
while '.' not in user_text:
    list_text.append(user_text)
    user_text = input()

last_text = ''
for el in user_text:
    if el == '.':
        last_text += el
        break
    else:
        last_text += el
list_text.append(last_text)

text = '\n'.join(list_text)
split_text = re.findall(r'\b\w+\b', text)
k = max([len(word) for word in split_text])

new_text = ''
for el in text:
    if 'a' <= el <= 'z':
        new_text += chr((ord(el) - ord('a') + k) % 26 + ord('a'))
    elif 'A' <= el <= 'Z':
        new_text += chr((ord(el) - ord('A') + k) % 26 + ord('A'))
    else:
        new_text += el

print(new_text)
