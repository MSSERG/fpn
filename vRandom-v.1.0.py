import random

input(' ')

while True:
	
	v1 = random.randint( 1, 36 )
	v2 = random.randint( 1, 36 )
	v3 = random.randint( 1, 36 )
	v4 = random.randint( 1, 36 )
	v5 = random.randint( 1, 36 )
	v6 = random.randint( 1, 36 )
	
	if ( v1 != v2
	and  v1 != v3
	and  v1 != v4
	and  v1 != v5
	and  v1 != v6
	
	and  v2 != v3
	and  v2 != v4
	and  v2 != v5
	and  v2 != v6
	
	and  v3 != v4
	and  v3 != v5
	and  v3 != v6
	
	and  v4 != v5
	and  v4 != v6
	
	and  v5 != v6 ):
		
		print( '  ', v1, v2, v3, v4, v5, v6, end='' )
		
		resetGood = ""
		
		reset = input()
		
		if reset == resetGood:
			
			continue
		
		break
	
	else:
		
		continue

input(' ')