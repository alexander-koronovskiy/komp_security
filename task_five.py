CHARS_SIM = {"а": "a", "с": "c", "е": "e", "о": "o", "р": "p", "у": "y", "х": "x",
             "А": "A", "В": "B", "С": "C", "Е": "E", "О": "O", "Р": "P", "Х": "X", "Н": "H"}
PHRASE = "надеюсьвсеработаетправильно"


# алгоритм шифрования
def enc(text):
    colomn = ''
    for i in text:
        symbol_bytes = bin(ord(i))[2:]
        for j in symbol_bytes:
            colomn = colomn + str(j)
    return colomn


# зашифрованное в двоичном коде сообщение
s = enc(PHRASE)

# все позиции в тексте с похожими символами
my_file = open("text.txt")
text = my_file.read()

sym = list()    # символы keys()
p = list()      # позиции символов
j = 0
for i in text:
    j = j + 1
    if i in CHARS_SIM.keys():
        sym.append(i)
        p.append(j)

# реализовать алгоритм замены
# позиции keys
# позиции values
#
