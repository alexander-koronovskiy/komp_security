CHARS_SIM = {"а": "a", "с": "c", "е": "e", "о": "o", "р": "p", "у": "y", "х": "x",
             "А": "A", "В": "B", "С": "C", "Е": "E", "О": "O", "Р": "P", "Х": "X", "Н": "H"}
PHRASE = "надеюсьвсеработаетправильно"


# алгоритм шифрования
def enc(text):
    colomn = ''
    for i in text:
        symbol_bytes = bin(ord(i))[2:]
        for j in symbol_bytes:
            colomn += str(j)
    return colomn


# алгоритм дешифровки
def decrypt(text):
    s = ""
    for i in text:
        if i in CHARS_SIM.keys():
            s += "1"
        if i in CHARS_SIM.values():
            s += "0"
    return s


# шифрование сообщения
s = enc(PHRASE)

# чтение первоначального текста из файла
my_file = open("text.txt")
text = my_file.read()

# шифрование
text_new = ''
j = 0
k = 0
for i in text:
    k += 1
    if i in CHARS_SIM.keys():
        if s[j] == "0":
            text_new += CHARS_SIM[i]
        else:
            text_new += i
        j += 1
        if j == len(s):
            break
    else:
        text_new += i
text_new += text[k:]

# запись результата в файл
with open(r"index.txt", "w") as file:
    file.write(text_new)

# чтение из записанного файла
# my_file_new = open("text.txt")
# text_new = my_file_new.read()

# дешифровка
s_new = decrypt(text_new)

symbols = list(map(''.join, zip(*[iter(s_new)] * 11)))
s1 = ''
for k in range(len(symbols)):
    s1 = s1 + chr(int(symbols[k], 2))
print(s1)
