# -*- coding: utf-8 -*-
import ipdb
def data_cleansing(file):

	o = open(file +'_clean','w+')
	f = open(file,'r')
	print f
	for line in f:
		#print line
		line = line.replace('\xc2\xb2,','2').replace('\xac','EU')
		
		neighborhood = line[line.find('<span>')+6:line.find('</span>')]
		metros = line[line.find('"')+1:line.find('m2')-1]
		precio = line[line.find('EU')+3:line.find('-,')-1].replace('.','')

		#find furnished (last position)
		last_comma = line.rfind(',')
		fur = line[line.rfind(',',0,last_comma)+1:last_comma]
		if fur == 'or unfurnished"':
			fur = 'Furnished'


		#ipdb.set_trace()
		# write output file
		if len(precio) <6:
			#print neighborhood,precio,metros,fur
			o.write(str(neighborhood)+","+str(precio)+","+str(metros)+","+str(fur)+"\n")
	f.close()
	o.close()		


data_cleansing('output.csv')