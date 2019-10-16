import re
from collections import Counter


# метод разбиения текста на пары слов
def chunk(iterable, size=2):
    length = len(iterable) - 1  # stop before reaching last character
    result = []
    for i in range(length):
        result.append(iterable[i:i+size])
    return result


# в каждой из строк текста удаляются символы, не входящие в состав русского алфавита
new_words = []
with open('text.txt', 'r') as infile:
    lines = [line for line in infile.readlines() if line.strip()]
for line in lines:
    clean_line = re.sub(r'(\b(section\s[\d]{1,2})\b)', '', line)
    clean_line_2 = re.sub(r'([()])', '', clean_line)
    new_words.append(clean_line_2.lower().replace('.', '').replace(';', '')
                     .replace('\n', '').replace('-', ' ').replace(" ", "").replace("?", "")
                     .replace(",", "").replace("!", ""))

# рассчет абсолютной частоты встречаемости
new_words_unit = ''.join(new_words)
size = 2
new_words_pairs = chunk(new_words_unit, size)  # chunk string
new_words_pairs = [''.join(i) for i in new_words_pairs if len(i) == size]  # filter single chars
dictionary = Counter(new_words_pairs); # print(dictionary)

# рассчет относительной частоты встречаемости
a = sum(list(dictionary.values()))
t = list(dictionary.values())
for i in range(len(t)):
    t[i] = t[i] / a

# запись в словарь относительной частоты встречаемости
b = list(dictionary.keys())
for i in range(len(t)):
    dictionary[b[i]] = round(t[i], 3)

# вывод результата в консоль
print(dictionary)
