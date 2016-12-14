# MSSERG | 14.12.2016

# https://vk.com/images/stickers/1/64.png
# .........................................
# https://vk.com/images/stickers/3717/512.png

i = 0; k = 32; counter = 0;

f = open( 'imageURL.html', 'w' )

while i < 3717:
	
	i += 1; k = 32;
	
	f.write( '<hr />' )
	
	while k < 512:
		
		k *= 2; counter += 1;
		
		imageURL = '\n<img src="https://vk.com/images/stickers/' + str( i ) + '/' + str( k ) + '.png" />\n'
		
		f.write( imageURL )

f.close()

input( 'finish write' )