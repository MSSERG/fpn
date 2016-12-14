# MSSERG | 14.12.2016

# http://vk.com/images/gifts/256/230.jpg

import urllib.request

i = -1; k = -1; counter = 0;

f = open( 'imageURL.html', 'w' )

while i < 10000:
	
	i += 1; k = 0;
	
	f.write( '\n<hr />' )
	
	while k < 10000:
		
		k += 1; counter += 1;
		
		imageURL = '\n<img src="' + str( i ) + '~' + str( k ) + '.jpg" />'
		
		print( imageURL )
		
		f.write( imageURL )
		
		imageURL = 'http://vk.com/images/gifts/' + str( i ) + '/' + str( k ) + '.jpg'
		
		imageName = str( i ) + '~' + str( k ) + '.jpg'
		
		try:
			imageDownload = urllib.request.urlopen( imageURL ).read()
			
			img = open( imageName, 'wb' )
			
			img.write( imageDownload )
			
			img.close()
		
		except IOError as startyem:
			
			print( 'except IOError' )
			
			continue
		
		print( 'Download image:', imageName )

f.close()

print( 'All    imageURL =', counter )

print( 'Unique imageURL =', i )

input( '\nFinish write' )