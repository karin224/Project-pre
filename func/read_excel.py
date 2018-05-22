import sys
import numpy as np
sys.path.append("C:/Users/manggny/Desktop")
sys.path.append("C:/Users/manggny/PycharmProjects/Project-pre/func")

from d0_makelist_column import MakeList_column

means_list = []
days_list = []
year = 2014
list_mon = ['01','02','03','04','05','06','07','08','09','10','11','12']
list_days=[]
for i in range(1,32):
	if i/10<1:
		list_days.append("0"+str(i))
	else:
		list_days.append(str(i))

#print(list_days)


for month in list_mon:
	for days in list_days:
		filename = "C:/Users/manggny/Desktop/data/MagIch_2014/MagIch_2014"+month+days+".txt"
		column = []
		try:
			column = MakeList_column(filename)
			#print('2')
		except:
			#print('1')
			continue
		new_c = []

		for line in column:
			new = []
			for i in range(len(line)):
				new.append(line[i].replace(",",''))
			new_c.append(new)

		val = []
		for i in new_c[6]:
			if i == 'NaN':
				#print(1)
				continue
			try:
				val.append(float(i))
			except:
		#		print(i)
				continue


		means_list.append(np.mean(val))
		days_list.append(str(year)+str(month)+str(days))

print(means_list[72])
txt_file = open("mean_"+str(year)+".txt",'w+')
for i in range(len(means_list)):
	print(type(means_list[i]))
	txt_file.write(days_list[i]+" "+str(means_list[i])+"\n")


		#print(new_c[6])
		#print(np.mean(new_c[6]))

