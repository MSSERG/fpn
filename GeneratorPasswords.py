# MSSERG | 19:51 03.11.2018
# Generator Password to F.N.L.

while True:

	InputOut = ''
	Counter0 = 0
	Counter1 = 0

	InputIn = str( input( "\n  Введите фамилию, имя или отчество: " ) )

	for i in InputIn:

		if( i == "а" or i == "А" ):
		
			InputOut = InputOut + "1"
			
		elif( i == "б" or i == "Б" ):
		
			InputOut = InputOut + "10"
			
		elif( i == "в" or i == "В" ):
		
			InputOut = InputOut + "11"
			
		elif( i == "г" or i == "Г" ):
		
			InputOut = InputOut + "100"
			
		elif( i == "д" or i == "Д" ):
		
			InputOut = InputOut + "101"
			
		elif( i == "е" or i == "Е" ):
		
			InputOut = InputOut + "111"
			
		elif( i == "ё" or i == "Ё" ):
		
			InputOut = InputOut + "1000"
			
		elif( i == "ж" or i == "Ж" ):
		
			InputOut = InputOut + "1001"
			
		elif( i == "з" or i == "З" ):
		
			InputOut = InputOut + "1011"
			
		elif( i == "и" or i == "И" ):
		
			InputOut = InputOut + "1111"
			
		elif( i == "й" or i == "Й" ):
		
			InputOut = InputOut + "10000"
			
		elif( i == "к" or i == "К" ):
		
			InputOut = InputOut + "10001"
			
		elif( i == "л" or i == "Л" ):
		
			InputOut = InputOut + "10011"
			
		elif( i == "м" or i == "М" ):
		
			InputOut = InputOut + "10111"
			
		elif( i == "н" or i == "Н" ):
		
			InputOut = InputOut + "11111"
			
		elif( i == "о" or i == "О" ):
		
			InputOut = InputOut + "100000"
			
		elif( i == "п" or i == "П" ):
		
			InputOut = InputOut + "100001"
			
		elif( i == "р" or i == "Р" ):
		
			InputOut = InputOut + "100011"
			
		elif( i == "с" or i == "С" ):
		
			InputOut = InputOut + "100111"
			
		elif( i == "т" or i == "Т" ):
		
			InputOut = InputOut + "101111"
			
		elif( i == "у" or i == "У" ):
		
			InputOut = InputOut + "111111"
			
		elif( i == "ф" or i == "Ф" ):
		
			InputOut = InputOut + "1000000"
			
		elif( i == "х" or i == "Х" ):
		
			InputOut = InputOut + "1000001"
			
		elif( i == "ц" or i == "Ц" ):
		
			InputOut = InputOut + "1000011"
			
		elif( i == "ч" or i == "Ч" ):
		
			InputOut = InputOut + "1000111"
			
		elif( i == "ш" or i == "Ш" ):
		
			InputOut = InputOut + "1001111"
			
		elif( i == "щ" or i == "Щ" ):
		
			InputOut = InputOut + "1011111"
			
		elif( i == "ъ" or i == "Ъ" ):
		
			InputOut = InputOut + "1111111"
			
		elif( i == "ы" or i == "Ы" ):
		
			InputOut = InputOut + "10000000"
			
		elif( i == "ь" or i == "Ь" ):
		
			InputOut = InputOut + "10000001"
			
		elif( i == "э" or i == "Э" ):
		
			InputOut = InputOut + "10000011"
			
		elif( i == "ю" or i == "Ю" ):
		
			InputOut = InputOut + "10000111"
			
		elif( i == "я" or i == "Я" ):
		
			InputOut = InputOut + "10001111"
				
		else:
		
			continue

	print( "\n ", InputOut )

	for i in InputOut:

		if( i == "0" ):
		
			Counter0 = Counter1 + 1

		elif( i == "1" ):
		
			Counter1 = Counter1 + 1
			
		else:
			
			continue
			
	print( "\n  1 = ", Counter1, ";", "0 = ", Counter0 )