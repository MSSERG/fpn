# MSSERG | 1.12.2016

a = ' а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ь ы ъ э ю я '; b = ':'; i = 0;

f = open( 'text.txt', 'a' )

while i < 10000000:
	
	i += 1
	
	f.write( a )
	
	f.write( b )
	
	f.write( str( i ) )
	
	f.write( '\n' )

f.close()

input('запись завершена')