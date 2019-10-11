from collections import Counter
from tkinter import filedialog as fd


# функция поиска нужного файла вручную
def insertText():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    f.close()
    return s


# запись символов по частоте встречаемости (абсолютной)
a = insertText()
dictionary = {}
for key1, value in Counter(a.lower()).items():
    if key1.isalpha():
        dictionary[key1] = value

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
print(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
