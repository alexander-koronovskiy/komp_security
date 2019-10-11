def enc(text):
    s = list()
    for i in text:
        s.append(bin(ord(i))[2:].count('0') * 'c')
    return s


# чтение исходного текста
my_file = open("text.txt")
text = my_file.read()

# шифрование фразы (т.е. скрытой части текста)
phrase = text[60:244]
phrase_crypt = enc(phrase)

# запись шифрованной фразы
with open(r"lines.txt", "w") as file:
    file.writelines("%s\n" % line for line in phrase_crypt)

# чтение зашифрованного файла
s1 = ''
with open(r"lines.txt", "r") as file:
    for line in file:
        s1 = s1 + str(line.count('c'))

# шифрование всего текста
s2 = ''
for i in text:
    s2 = s2 + str(bin(ord(i))[2:].count('0'))

# поиск подстроки
i = s2.find(s1)
j = i + len(s1)
print(text[i:j])
