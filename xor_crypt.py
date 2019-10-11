# алгоритм шифрования
def xor_it(str, key):
    code = ''
    y = 0
    for i in range(0, len(str)):
        if y == len(key): y = 0
        code += chr(ord(str[i:i + 1]) ^ ord(key[y:y + 1]))
        y += 1
    return code


# чтение текста и задание ключа шифра
my_file = open("text.txt")
text = my_file.read()
key = "archer"

# шифрование
crypt = xor_it(text, key)
print(crypt, '\n')

# дешифровка
decrypt = xor_it(crypt, key)
print(decrypt, '\n')
