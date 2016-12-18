# Decryptot

file = open( 'file.txt', 'w' )

file.close

def decryptor():
	
	strDecryptor=input( '\n  Введите или вставьте текст для дешифрования ↓\n\n ' )
	
	print( '\n  ', end = '' )
	
	notDecryptorValue = ''
	
	allDecryptorValue = ''
	
	for v in strDecryptor:
		
		# Low literal
		
		if v == 'q':
			v = 'й'
		elif v == 'w':
			v = 'ц'
		elif v == 'e':
			v = 'у'
		elif v == 'r':
			v = 'к'
		elif v == 't':
			v = 'е'
		elif v == 'y':
			v = 'н'
		elif v == 'u':
			v = 'г'
		elif v == 'i':
			v = 'ш'
		elif v == 'o':
			v = 'щ'
		elif v == 'p':
			v = 'з'
		elif v == '[':
			v = 'х'
		elif v == ']':
			v = 'ъ'
		elif v == 'a':
			v = 'ф'
		elif v == 's':
			v = 'ы'
		elif v == 'd':
			v = 'в'
		elif v == 'f':
			v = 'а'
		elif v == 'g':
			v = 'п'
		elif v == 'h':
			v = 'р'
		elif v == 'j':
			v = 'о'
		elif v == 'k':
			v = 'л'
		elif v == 'l':
			v = 'д'
		elif v == ';':
			v = 'ж'
		elif v=="'":
			v = 'э'
		elif v == 'z':
			v = 'я'
		elif v == 'x':
			v = 'ч'
		elif v == 'c':
			v = 'с'
		elif v == 'v':
			v = 'м'
		elif v == 'b':
			v = 'и'
		elif v == 'n':
			v = 'т'
		elif v == 'm':
			v = 'ь'
		elif v == ',':
			v = 'б'
		elif v == '.':
			v = 'ю'
		elif v == '/':
			v = '.'
		
		# Tall literal
		
		elif v == 'Q':
			v = 'Й'
		elif v == 'W':
			v = 'Ц'
		elif v == 'E':
			v = 'У'
		elif v == 'R':
			v = 'К'
		elif v == 'T':
			v = 'Е'
		elif v == 'Y':
			v = 'Н'
		elif v == 'U':
			v = 'Г'
		elif v == 'I':
			v = 'Ш'
		elif v == 'O':
			v = 'Щ'
		elif v == 'P':
			v = 'З'
		elif v == '{':
			v = 'Х'
		elif v == '}':
			v = 'Ъ'
		elif v == 'A':
			v = 'Ф'
		elif v == 'S':
			v = 'Ы'
		elif v == 'D':
			v = 'В'
		elif v == 'F':
			v = 'А'
		elif v == 'G':
			v = 'П'
		elif v == 'H':
			v = 'Р'
		elif v == 'J':
			v = 'О'
		elif v == 'K':
			v = 'Л'
		elif v == 'L':
			v = 'Д'
		elif v == ':':
			v = 'Ж'
		elif v == '"':
			v = 'Э'
		elif v == 'Z':
			v = 'Я'
		elif v == 'X':
			v = 'Ч'
		elif v == 'C':
			v = 'С'
		elif v == 'V':
			v = 'М'
		elif v == 'B':
			v = 'И'
		elif v == 'N':
			v = 'Т'
		elif v == 'M':
			v = 'Ь'
		elif v == '<':
			v = 'Б'
		elif v == '>':
			v = 'Ю'
		elif v == '?':
			v = ','
		
		# Other fee literal
		
		
		elif v == '`':
			v = 'ё'
		elif v == '~':
			v = 'Ё'
		elif v == '@':
			v = '"'
		elif v == '#':
			v = '№'
		elif v == '$':
			v = ';'
		elif v == '^':
			v = ':'
		elif v == '&':
			v = '?'
		
		# Not decrypt value
		
		else: notDecryptorValue += v
		
		# Save all values v
		
		allDecryptorValue += v
		
		# Print
		
		print( v, end = '' )
	
	# Write to file.txt
	
	file = open( 'file.txt', 'a' )
	
	file.write( 'Весь дешифрованный текст:\n\n' )
	
	file.write( str( allDecryptorValue ) )
	
	file.write( '\n\nВесь не дешифрованный текст:\n\n' )
	
	file.write( str( notDecryptorValue ) )
	
	file.write( '\n\n' )
	
	file.close()

while True:
	
	decryptor()
	
	input( '\n\n  Процесс дешифрования завершён, текст выведен на экран и записан в файл.' )