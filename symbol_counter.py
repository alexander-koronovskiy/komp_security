from collections import Counter
from tkinter import filedialog as fd
from tkinter import messagebox


def insertText():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    f.close()
    return s

a = insertText()
dictionary = {}
for key1, value in Counter(a.lower()).items():
    if key1.isalpha():
        dictionary[key1] = value
a = sum(list(dictionary.values()))
t = list(dictionary.values())
for i in range(len(t)):
    t[i] = t[i] / a
b = list(dictionary.keys())
for i in range(len(t)):
    dictionary[b[i]] = round(t[i], 3)
print(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
