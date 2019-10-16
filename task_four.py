PHRASE = "скоро выйдет новая часть"

# алгоритм шифрования
def enc(text):
    s = list()
    for i in text:
        s.append(bin(ord(i))[2:].count('1') * '_')
    return s


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
    s1 = ''
    with open(r"lines.txt", "r") as file:
        for line in file:
            s1 = s1 + str(line.count('_'))
    print(s1)


def main():
    # "стенография"
    # sten()
    dec()


if __name__ == "__main__":
    main()
