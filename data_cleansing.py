# -*- coding: utf-8 -*-
import ipdb
import csv

def data_cleansing_pararius(file):

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

def data_cleansing_funda(file):

	o = open(file +'_clean','w+')
	csvfile = open(file,'r')
	
	csvfile.next() #escape headers line

	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')	
	i = 1
	for line in spamreader:
		
		price=line[0]
		furnished = line[1]
		neighborhood=line[2]
		space = line[3]

		
		price = price.replace('\xac','EU')
		price = price[price.find('EU')+4:price.find('per maand')-1].replace('.','')
		
		
		neighborhood = neighborhood[neighborhood.find('title"">')+24:neighborhood.find('</span>')-1]
		
		space = space.replace('\xc2\xb2,','').replace('\xc2\xa0m','')
		space = space[space.find('title"">')+25:space.find('</span>')-1]
		space = space.decode('utf-8').encode("ascii", "ignore").replace(' ','')

		#ipdb.set_trace()

		furnished = furnished.replace("  ","")
		furnished = furnished[furnished.find('val"">')+25:furnished.find('</span>')]
		
		# write output file
		if len(price) <6:
			#print neighborhood,precio,metros,fur
			o.write(str(neighborhood)+","+str(price)+","+str(space)+","+str(furnished)+"\n")
	csvfile.close()
	o.close()

data_cleansing_funda('funda.csv')
#data_cleansing_pararius('output.csv')