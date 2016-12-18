print( '\n  Перевод символов в ASCII код.\n' )

while True:
	
	try:
		
		text = input( '  Введите любое значение:' )
		
		for l in text:
			
			print( ' ', l, '=', ord( l ), '\a' )
	
	except IOError as qwerty:
		
		text = '0'