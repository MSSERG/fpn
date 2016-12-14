# MSSERG | 14.12.2016

# https://vk.com/images/stickers/1/64.png
# .........................................
# https://vk.com/images/stickers/3717/512.png

import urllib.request

i = 0; k = 32; counter = 0;

f = open( 'imageURL.html', 'w' )

while i < 3717:
	
	i += 1; k = 32;
	
	f.write( '\n<hr />' )
	
	while k < 512:
		
		k *= 2; counter += 1;
		
		imageURL = '\n<img src="' + str( i ) + '~' + str( k ) + '.png" />'
		
		f.write( imageURL )
		
		imageURL = 'https://vk.com/images/stickers/' + str( i ) + '/' + str( k ) + '.png'
		
		imageName = str( i ) + '~' + str( k ) + '.png'
		
		imageDownload = urllib.request.urlopen( imageURL ).read()
		
		img = open( imageName, 'wb' )
		
		img.write( imageDownload )
		
		img.close()
		
		print( 'Download image:', imageName )

f.close()

print( 'All    imageURL =', counter )

print( 'Unique imageURL =', i )

input( '\nFinish write' )