my_file = open("text.txt")
text = my_file.read()
j = 0
i_r = list(); s_r = list()
for i in range(len(text)):
    if text[i] == '\n':
        i_r.append(i)
        s = 0
        for k in text[j:i]:
            s = s + bin(ord(k))[2:].count('1')
        s_r.append(s)
        j = i
print(i_r, s_r)

# добавление количества пробелов в конце каждого
p = 0  # счетчик вхождений
j = 0
s1 = ''  # новая строка
for i in range(len(text)):
    if i in i_r:
        s1 = s1 + text[j:i] + s_r[p]*' '
        j = i
        p = p + 1
print(s1)
