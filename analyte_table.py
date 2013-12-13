#!/usr/bin/env python
# coding: utf-8

in_file_name = 'Union of All Datasets (Standardized)-view.txt'
in_file = open(in_file_name, 'r')
out_file_name = "count_data.txt"
out_file = open(out_file_name, 'w')

total = []
week1 = []
week1_date = ['4/18/2010','4/19/2010','4/20/2010','4/21/2010','4/22/2010','4/23/2010','4/24/2010']
week2 = []
week2_date = ['4/25/2010','4/26/2010','4/27/2010','4/28/2010','4/29/2010','4/30/2010','5/1/2010']
week3 = []
week3_date = ['5/2/2010','5/3/2010','5/4/2010','5/5/2010','5/6/2010','5/7/2010','5/8/2010']
week4 = []
week4_date = ['5/9/2010','5/10/2010','5/11/2010','5/12/2010','5/13/2010','5/14/2010','5/15/2010']
week5 = []
week5_date = ['5/16/2010','5/17/2010','5/18/2010','5/19/2010','5/20/2010','5/21/2010','5/22/2010']
week6 = []
week6_date = ['5/23/2010','5/24/2010','5/25/2010','5/26/2010','5/27/2010','5/28/2010','5/29/2010']
week7 = []
week7_date = ['5/30/2010','5/31/2010','6/1/2010','6/2/2010','6/3/2010','6/4/2010','6/5/2010']
week8 = []
week8_date = ['6/6/2010','6/7/2010','6/8/2010','6/9/2010','6/10/2010','6/11/2010','6/12/2010']
week9 = []
week9_date = ['6/13/2010','6/14/2010','6/15/2010','6/16/2010','6/17/2010','6/18/2010','6/19/2010']
week10 = []
week10_date = ['6/20/2010','6/21/2010','6/22/2010','6/23/2010','6/24/2010','6/25/2010','6/26/2010']
week11 = []
week11_date = ['6/27/2010','6/28/2010','6/29/2010','6/30/2010','7/1/2010','7/2/2010','7/3/2010']
week12 = []
week12_date = ['7/4/2010','7/5/2010','7/6/2010','7/7/2010','7/8/2010','7/9/2010','7/10/2010']
week13 = []
week13_date = ['7/11/2010','7/12/2010','7/13/2010','7/14/2010','7/15/2010','7/16/2010','7/17/2010']
week14 = []
week14_date = ['7/18/2010','7/19/2010','7/20/2010','7/21/2010','7/22/2010','7/23/2010','7/24/2010']
week15 = []
week15_date = ['7/25/2010','7/26/2010','7/27/2010','7/28/2010','7/29/2010','7/30/2010','7/31/2010']
week16 = []
week16_date = ['8/1/2010','8/2/2010','8/3/2010','8/4/2010','8/5/2010','8/6/2010','8/7/2010']
week17 = []
week17_date = ['8/8/2010','8/9/2010','8/10/2010','8/11/2010','8/12/2010','8/13/2010','8/14/2010']
week18 = []
week18_date = ['8/15/2010','8/16/2010','8/17/2010','8/18/2010','8/19/2010','8/20/2010','8/21/2010']
week19 = []
week19_date = ['8/22/2010','8/23/2010','8/24/2010','8/25/2010','8/26/2010','8/27/2010','8/28/2010']
week20 = []
week20_date = ['8/29/2010','8/30/2010','8/31/2010','9/1/2010','9/2/2010','9/3/2010','9/4/2010']
week21 = []
week21_date = ['9/5/2010','9/6/2010','9/7/2010','9/8/2010','9/9/2010','9/10/2010','9/11/2010']
week22 = []
week22_date = ['9/12/2010','9/13/2010','9/14/2010','9/15/2010','9/16/2010','9/17/2010','9/18/2010']
week23 = []
week23_date = ['9/19/2010','9/20/2010','9/21/2010','9/22/2010','9/23/2010','9/24/2010','9/25/2010']
week24 = []
week24_date = ['9/26/2010','9/27/2010','9/28/2010','9/29/2010','9/30/2010','10/1/2010','10/2/2010'] 

counter = 1

for line in in_file:
	print counter
	line = line.strip()
	row = line.split('\t')
	if counter == 2:
		analyte = row[7]
	if len(row) == 17:
		print 'Replicate'
	else:
		print 'Data'
		total.append(row)
		date = row[5].split(' ')[0]
		if date in week1_date:
			week1.append(row)
		elif date in week2_date:
			week2.append(row)
		elif date in week3_date:
			week3.append(row)
		elif date in week4_date:
			week4.append(row)
		elif date in week5_date:
			week5.append(row)
		elif date in week6_date:
			week6.append(row)
		elif date in week7_date:
			week7.append(row)
		elif date in week8_date:
			week8.append(row)
		elif date in week9_date:
			week9.append(row)
		elif date in week10_date:
			week10.append(row)
		elif date in week11_date:
			week11.append(row)
		elif date in week12_date:
			week12.append(row)
		elif date in week13_date:
			week13.append(row)
		elif date in week14_date:
			week14.append(row)
		elif date in week15_date:
			week15.append(row)
		elif date in week16_date:
			week16.append(row)
		elif date in week17_date:
			week17.append(row)
		elif date in week18_date:
			week18.append(row)
		elif date in week19_date:
			week19.append(row)
		elif date in week20_date:
			week20.append(row)
		elif date in week21_date:
			week21.append(row)
		elif date in week22_date:
			week22.append(row)
		elif date in week23_date:
			week23.append(row)
		elif date in week24_date:
			week24.append(row)
		else:
			print 'Outside Date Range'
	counter = counter + 1
print analyte
out_file.write(str(len(week1)) + '\t' + str(len(week2)) + '\t' + str(len(week3)) + '\t' + str(len(week4)) + '\t' + str(len(week5)) + '\t' + str(len(week6)) + '\t' + str(len(week7)) + '\t' + str(len(week8)) + '\t' + str(len(week9)) + '\t' + str(len(week10)) + '\t' + str(len(week11)) + '\t' + str(len(week12)) + '\t' + str(len(week13)) + '\t' + str(len(week14)) + '\t' + str(len(week15)) + '\t' + str(len(week16)) + '\t' + str(len(week17)) + '\t' + str(len(week18)) + '\t' + str(len(week19)) + '\t' + str(len(week20)) + '\t' + str(len(week21)) + '\t' + str(len(week22)) + '\t' + str(len(week23)) + '\t' + str(len(week24)) + '\t' + str(len(total)))

