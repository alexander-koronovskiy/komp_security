def enc(text):
    s = list()
    for i in text:
        s.append(bin(ord(i))[2:].count('1') * '_')
    return s


# чтение исходного текста
my_file = open("text.txt")
text = my_file.read()
text0 = text

# счетчик строк
i_r = list()
for i in range(len(text)):
    if text[i] == '\n':
        i_r.append(i)

# шифрование фразы (т.е. скрытой части текста)
phrase = text[60:62]
phrase_crypt = enc(phrase)

# добавление шифра в исхдный файл
s1 = ''; j = 0; p = 0; k = 0
if len(phrase_crypt) >= len(i_r):
    for i in range(len(text)):
        if i in i_r:
            s1 = s1 + text[j:i] + phrase_crypt[p]
            j = i
            p = p + 1
    blocks = phrase_crypt[p:]
    for k in range(len(blocks)):
        s1 = s1 + '\n' + blocks[k]
if len(phrase_crypt) < len(i_r):
    for i in range(len(text)):
        if i in i_r:
            s1 = s1 + text[j:i] + phrase_crypt[p]
            j = i
            p = p + 1
            if p == len(phrase_crypt):
                s1 = s1 + text[j:]
                break
print(s1)
