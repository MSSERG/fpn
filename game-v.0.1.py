# MSSERG | 19.12.2016

import random

while True:
	
	value		= random.randint( 1, 1000 )
	znak		= random.randint( 0, 3 )
	peremennaya = random.randint( 1, 100 )
	
	if znak == 0:
		vopros = value + peremennaya
		znak = '+'
	
	elif znak == 1:
		vopros = value - peremennaya
		znak = '-'
	
	elif znak == 2:
		vopros = value * peremennaya
		znak = '*'
	
	elif znak == 3:
		vopros = value / peremennaya
		znak = '/'
	
	print( value, znak, peremennaya, end = ' =' )
	
	otvet = input()
	
	if otvet == vopros:
		print( 'Good' )
	
	else:
		print( 'Bad\a' )