PHRASE = "приветдивныйновыймир"


# алгоритм шифрования
def enc(text):
    colomn = list()
    for i in text:
        symbol_bytes = bin(ord(i))[2:]
        for j in symbol_bytes:
            if j == '1':
                colomn.append('')
            if j == '0':
                colomn.append('с')
    return colomn


# алгоритм "стенографии"
def sten():

    # текст
    my_file = open("text.txt")
    text = my_file.read()

    # шифрованнная фраза
    phrase = PHRASE
    phrase_crypt = enc(phrase)

    # счетчик строк в тексте
    i_r = list()
    for i in range(len(text)):
        if text[i] == '\n':
            i_r.append(i)

    # добавление шифра в исходный файл
    s1 = ''
    j = 0
    p = 0
    for i in range(len(text)):
        if i in i_r:
            s1 = s1 + text[j:i] + phrase_crypt[p]
            j = i
            p = p + 1
            if p == len(phrase_crypt):
                s1 = s1 + text[j:]
                break
    if len(phrase_crypt) >= len(i_r):
        blocks = phrase_crypt[p:]
        for k in range(len(blocks)):
            s1 = s1 + '\n' + blocks[k]

    # запись результата в файл
    with open(r"index.txt", "w") as file:
        file.write(s1)


def dec():
    # чтение зашифрованного файла
    colomn = list()
    s = ''
    with open(r"index.txt", "r") as file:
        for line in file:
            colomn.append(line[-2:-1])
        for j in colomn:
            if j == 'с':
                s = s + '0'
            else:
                s = s + '1'
    symbols = list(map(''.join, zip(*[iter(s)] * 11)))
    s1 = ''
    for k in range(len(symbols) - 1):
        s1 = s1 + chr(int(symbols[k], 2))
    s1 = s1 + chr(int(symbols[k+1], 2) - 1)
    print(s1)


def main():
    sten()
    dec()


if __name__ == "__main__":
    main()
