#!/usr/bin/env python
# coding: utf-8

"""
Convert multiple formats of latitude and longitude into decimal degrees
"""



def check_format(latitude1, longitude1):
	if latitude1.find(' |N|S|W|E') == -1:
		if latitude1.find('.') != -1:
			print 'Already correctly formatted'
			outfile.write("\t".join(latitude1, longitude1) + '\n')
		else:
			print 'Needs formatting'
	else:
		print 'Needs formatting'
		return latitude1, longitude1
"""
This function checks a latitude and longitude to see if it needs to be formatted or if it 
is already in decimal degrees.
"""

def split_parts(latitude1, longitude1):
	latitude2 = latitude1.replace('N|S|-','')
	longitude2 = longitude1.replace('W|E|-','')
	latitude3 = latitude2.split(' |°|\'|\"')
	longitude3 = longitude2.split('  |°|\'|\"')
	return latitude3, longitude3
"""
This function separates the parts of the latitude and longitude
"""

def define_parts(latitude3, longitude3)
	if len(latitude3) == 1:
		return latitude3, longitude3
	elif len(latitude3) == 2:
		latitude_degree = latitude3[0]
		latitude_minute = latitude3[1]
		decimal_latitude = float(latitude_degree) + (float(latitude_minute) / 60)
		longitude_degree = longitude3[0]
		longitude_minute = longitude3[1]
		decimal_longitude = float(longitude_degree) + (float(longitude_minute) / 60)
		return decimal_latitude, decimal longitude
	else:
		latitude_degree = latitude3[0]
		latitude_minute = latitude3[1]
		latitude_second = latitude3[2]
		decimal_latitude = float(latitude_degree) + (float(latitude_minute) / 60) + (float(latitude_second) / 3600)
		longitude_degree = longitude3[0]
		longitude_minute = longitude3[1]
		longitude_second = longitude3[2]
		decimal_longitude = float(longitude_degree) + (float(longitude_minute) / 60) + (float(longitude_second) / 3600)
		return decimal_latitude, decimal longitude
"""
This function separates the parts of a lat long and calculates the decimal degree.
"""

def find_hemisphere(latitude1, longitude1):
	if latitude1.find('N') != -1:
		latitude_hemisphere = 'N'
	elif latitude1.find('S') != -1:
		latitude_hemisphere = 'S'
	elif latitude1.find('-') != -1:
		latitude_hemisphere = 'S'
	return latitude_hemisphere
	
	if longitude1.find('E') != -1:
		longitude_hemisphere = 'E'
	elif longitude1.find('W') != -1:
		longitude_hemisphere = 'W'
	elif longitude1.find('-') != -1:
		longitude_hemisphere = 'W'
	return longitude_hemisphere
"""
This function determines the hemisphere of the lat longs
"""

def assign_hemisphere(latitude_hemisphere, longitude_hemisphere, decimal_latitude, decimal_longitude)
	if latitude_hemisphere == 'S':
		lat_value = '-' + decimal_latitude
	else:
		lat_value = decimal_latitude
		
	if longitude_hemisphere == 'W':
		long_value = '-' + decimal_longitude
	else:
		long_value = decimal_longitude
	
	return lat_value, long_value
"""
This function assigns a '-' if the hemisphere is S or W
"""			

		
in_file_name = "lat_long_test_data.txt"
in_file = open(in_file_name, 'r')
out_file_name = "lat_long_test_output.txt"
out_file = open(out_file_name, 'w')

for line in in_file:
	row = line.split('\t|,')
	latitude1 = row[0].strip()	#how do we know latitude will always be first?
	longitude1 = row[1].strip()
	out_file.write("\t".join(lat_value, long_value) + '\n')