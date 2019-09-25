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

messagebox.showinfo('result',
                    sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
