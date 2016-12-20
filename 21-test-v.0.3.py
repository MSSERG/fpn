import random

koloda = [ 6, 7, 8, 9, 10, 2, 3, 4, 11 ] * 4

random.shuffle( koloda )

while True:
	
	countOne = 0; countTwo = 0; hodOne = 1; hodTwo = 1;
	
	print( '\nНачалась новая игра!' )
	
	while True:
		
		# Игрок 1
		
		if hodOne == 1:
			
			playerOne = input( '\nИгрок 1, будешь брать карту? д|н:' )
			
			if playerOne == 'д':
				
				randomKartaOne = koloda.pop()
				
				countOne += randomKartaOne
		
		elif hodOne == 0:
			
			print( '', end='' )
		
		if hodTwo == 1:
			
			playerTwo = input( 'Игрок 2, будешь брать карту? д|н:' )
			
			if playerTwo == 'д':
				
				randomKartaTwo = koloda.pop()
				
				countTwo += randomKartaTwo
		
		elif hodTwo == 0:
			
			print( '', end='' )
		
		if playerOne == 'д':
			
			print( '\nИгрок 1 получил карту достоинством %d, ' %randomKartaOne, end='' )
			
			if countOne > 21:
				
				print( 'перебор, вы проиграли, ваш счёт %d.' %countOne )
				
				playerOne = ''
				
				hodOne -= 1
				
				break
			
			elif countOne == 21:
				
				print( 'поздравляем, вы набрали 21 очко!' )
				
				playerOne = ''
				
				hodOne -= 1
			
			else:
				
				print( 'итого у игрока %d очков.' %countOne )
		
		elif playerOne == 'н':
			
			print( '\nИгрок 1, отказался брать карту, его счёт %d ' %countOne, end='' )
			
			playerOne = ''
			
			hodOne -= 1
			
			if countOne > countTwo and countOne < 22:
				
				print( 'и он победил игрока 2, со счётом %d.' %countTwo )
				
				break
			
			elif countOne < countTwo and countOne < 22:
				
				print( 'и он проиграл игроку 2, со счётом %d.' %countTwo )
				
				break
			
			elif countOne == countTwo and countOne < 22:
				
				print( 'и он равен счёту игрока 2.' )
				
				break
			
			elif countOne == countTwo and countOne > 21:
				
				print( 'и он проиграл.' )
				
				break
		
		# Игрок 2
		
		if playerTwo == 'д':
			
			print( 'Игрок 2 получил карту достоинством %d, ' %randomKartaTwo, end='' )
			
			if countTwo > 21:
				
				print( 'перебор, вы проиграли, ваш счёт %d.' %countTwo )
				
				playerTwo = ''
				
				hodTwo -= 1
				
				break
			
			elif countTwo == 21:
				
				print( 'поздравляем, вы набрали 21 очко!' )
				
				playerTwo = ''
				
				hodTwo -= 1
			
			else:
				
				print( 'итого у игрока %d очков.' %countTwo )
		
		elif playerTwo == 'н':
			
			print( 'Игрок 2, отказался брать карту, его счёт %d ' %countTwo, end='' )
			
			playerTwo = ''
			
			hodTwo -= 1
			
			if countTwo > countOne and countTwo < 22:
				
				print( 'и он победил игрока 1, со счётом %d.' %countOne )
				
				break
			
			elif countTwo < countOne and countTwo < 22:
				
				print( 'и он проиграл игроку 1, со счётом %d.' %countOne )
				
				break
			
			elif countTwo == countOne and countTwo < 22:
				
				print( 'и он равен счёту игрока 1.' )
				
				break
			
			elif countTwo == countOne and countTwo > 21:
				
				print( 'и он проиграл.' )
				
				break