# MSSERG | 30.11.2016

a = ' а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ь ы ъ э ю я\n'; b = ''; i = 0;

while i < 22:
	
	i+=1
	
	b += a

f = open( 'text.txt', 'w' )

f.write( b )

f.close

input( 'запись завершена' )

f = open( 'text.txt', 'r' )

print( f.read() )

f.close

input( 'чтение завершено' )