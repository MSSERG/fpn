# MSSERG | 15.12.2016

# https://vk.com/images/stickers/1/64.png
# .........................................
# https://vk.com/images/stickers/3717/512.png

import urllib.request

i = 0; k = 32; counter = 0; unique = 0;

file = open( 'imageURL.html', 'w' )

file.close()

while i < 3717:
	
	i += 1; k = 32;
	
	file = open( 'imageURL.html', 'a' )
	
	file.write( '\n<hr />' )
	
	file.close()
	
	while k < 512:
		
		k *= 2; unique += 1;
		
		try:
			
			imageURL = '\n<img src="' + str( i ) + '~' + str( k ) + '.png" />'
			
			file = open( 'imageURL.html', 'a' )
			
			file.write( imageURL )
			
			file.close()
			
			#imageURL = 'https://vk.com/images/stickers/' + str( i ) + '/' + str( k ) + '.png'
			
			#imageName = str( i ) + '~' + str( k ) + '.png'
			
			#imageDownload = urllib.request.urlopen( imageURL ).read()
			
			#img = open( imageName, 'wb' )
			
			#img.write( imageDownload )
			
			#img.close()
			
			#print( 'Download image:', imageName )
			
		except IOError as qwerty:
			
			#print( 'Download failed image:', imageName )
			
			counter += 1
			
			continue

print( 'All    imageURL =', unique )

unique /= 4; unique -= counter;

print( 'Unique imageURL =', int(unique) )

input( '\nFinish write' )