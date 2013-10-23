#!/usr/bin/env python
# coding: utf-8

import numpy
from datetime import timedelta

in_file_name = "AT18-02_CTD_3.txt"
in_file = open(in_file_name, 'r')
out_file_name = "0104_CTD_Data_5.txt"
out_file = open(out_file_name, 'w')

counter = 0
data_set_id = '0104'
depth_unit = 'm'
time_unit = 'UTC'
sample_medium = 'water'
out_file.write('\t'.join(['Data Set ID','Data Point ID','Latitude','Longitude','Depth','Depth Unit','Date','Time','Time Unit','Parameter','Value','Unit','Measurement Device','Sample Medium','Uncertainty','Uncertainty Unit'+ '\n']))

def get_sample_time(time_start,time_elapsed):
	time_s = str(time_start)
	start_hour_s = time_s[:2]
	start_hour_d = int(start_hour_s)
	start_minute_s = time_s[2:]
	start_minute_d = float(start_minute_s)
	t1 = timedelta(hours=start_hour_d,minutes=start_minute_d)
	if time_elapsed != '-9999.0':
		time_change = float(time_elapsed)
		t2 = timedelta(seconds=time_change)
		time = t1 + t2
	else:
		time = ''
	return str(time)
	
def calculate_avg_and_uncertainty(table):
	avg = numpy.mean(table)
	highest_value = max(table)
	uncert = (highest_value - avg) * 2
	average = str(avg)
	uncertainty = str(uncert)
	return (average,uncertainty)

def reformat_date(date):
	date1 = date.split('/')
	year = date1[2]
	month = date1[0]
	day = date1[1]
	if len(month) == 1:
		month = '0' + month
	if len(day) == 1:
		day = '0' + day
	ref_data = year + month + day
	return ref_data

for line in in_file:
	counter = counter + 1
	print counter
	abba = line.replace(' ','')
	row = abba.strip().split('\t')
	date = row[2]
	time_start = row[3]
	depth = row[6]
	time_elapsed = row[9]
	latitude = row[10]
	longitude = row[11]
	temperature1 = row[12]
	temperature2 = row[13]
	salinity1 = row[16]
	salinity2 = row[17]
	oxygen = row[24]
	chlorophyll = row[30]
	turbidity = row[31]
	cdom = row[32]
	if temperature1 and temperature2 != -9999.0:
		temperature_table = [float(temperature1),float(temperature2)]
		temperature, temp_uncertainty = calculate_avg_and_uncertainty(temperature_table)
	elif temperature1 == -9999.0:
		temperature = temerature2
		temp_uncertainty = ''
	elif temperature2 == -9999.0:
		temperature = temperature1
		temp_uncertainty = ''
	else:
		temperature = ''
		temp_uncertainty = ''
	if salinity1 and salinity2 != -9999.0:
		salinity_table = [float(salinity1),float(salinity2)]
		salinity, sal_uncertainty = calculate_avg_and_uncertainty(salinity_table)
	elif salinity1 == -9999.0:
		salinity = salinity2
		sal_uncertainty = ''
	elif salinity2 == -9999.0:
		salinity = salinity1
		sal_uncertainty = ''
	else:
		salinity = ''
		sal_uncertainty = ''
	time = get_sample_time(time_start,time_elapsed)
	date1 = reformat_date(date)
	variables = [('temperature',temperature,'°C','CTD SBE 911',temp_uncertainty,'°C'),('salinity',salinity,'psu','CTD SBE 911',sal_uncertainty,'psu'),('oxygen',oxygen,'μmol/kg','SBE43','',''),('chlorophyll',chlorophyll,'μg/L','CTD SBE 911','',''),('turbidity',turbidity,'NTU','CTD SBE 911','',''),('cdom',cdom,'mg/m^3','CTD SBE 911','','')]
	for variable in variables:
		parameter = variable[0]
		value = variable[1]
		unit = variable[2]
		measurement_device = variable[3]
		uncertainty = variable[4]
		uncertainty_unit = variable[5]
		data_point_id = str('CTD' + str(date) + str(depth) + parameter[:3])
		out_file.write('\t'.join([data_set_id,data_point_id,latitude,longitude,depth,depth_unit,date1,time,time_unit,parameter,value,unit,measurement_device,sample_medium,uncertainty,uncertainty_unit + '\n']))
out_file.close()