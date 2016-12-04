# MSSERG | 3.12.2016

# http://vk.com/images/stickers/112/128.png

linkPart1 = '<img src="http://vk.com/images/stickers/'; linkPart2 = '/128.png" />\n'; i = 0;

f = open( 'linkStickersVK.txt', 'a' )

while i < 3669:
	
	i += 1
	
	print( 'завершена', i, 'из 3669 строк')
	
	f.write( linkPart1 )
	
	f.write( str(i) )
	
	f.write( linkPart2 )

f.close()

input( 'запись завершена' )