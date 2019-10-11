def enc(text):
    s = list()
    for i in text:
        s.append(bin(ord(i))[2:].count('1') * '_')
    return s


# чтение исходного текста
my_file = open("text.txt")
text = my_file.read()

# запись
s = list()
for i in text:
    s.append(bin(ord(i))[2:].count('1')*'_')
with open(r"lines.txt", "w") as file:
    file.writelines("%s\n" % line for line in s)

# чтение зашифрованного файла
with open(r"lines.txt", "r") as file:
    for line in file:
        print(line.count('_'))

# кодирование среза text[:]
# кодирование всего текста
# чтение зашифрованного файла
