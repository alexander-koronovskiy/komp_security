my_file = open("text.txt")
text = my_file.read()
key = 15

# Шифрование
# A = 65 ASCII
# B = 66
# C = 67 ...

crypt = ""
for i in text:
	try:
		crypt += chr(ord(i) ^ ord(key))
	except TypeError:
		crypt += chr(ord(i) ^ key)

with open("crypt.txt", "w") as file:
	file.write(crypt)
print('после шифрования:')
print(crypt, '\n')

# Расшифрование
decrypt = ""
with open("crypt.txt", "r") as file:
	for j in file.read():
		try:
			decrypt += chr(ord(j)^ord(key))
		except TypeError:
			decrypt += chr(ord(j)^key)
print('после расшифрования:')
print(decrypt)
