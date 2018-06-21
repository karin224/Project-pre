import math
import sys, os
from date_maker import DATE_MAKER
from c0_READ_PATH_FILE import read_file_name
from d0_makelist import *
from d0_makelist_column import *
from c0_Make_txt_from_Raw_list import MAKE_TXT
import numpy as np


class d_funcs(object):

	def __init__(self):
		num = 0

	def d0_exclude_1_mean(LIST):  # NOTE!!!!  Not in counting first element of the list
		TOT = 0.0
		for i in range(len(LIST)):
			if i == 0:
				continue
			TOT = TOT + float(LIST[i])
		return (TOT / float(len(LIST)))

	def d0_exclude_1_variance(LIST):  # NOTE : Not in counting first element of the list
		MEAN = d0_exclude_1_mean(LIST)
		TEMP = 0.0
		for i in range(len(LIST)):
			if i == 0:
				continue
			TEMP = TEMP + (float(LIST[i]) - MEAN) * (float(LIST[i]) - MEAN)
		return (TEMP / (float(len(LIST)) - 2.0))

	def d0_exclude_1_STD(LIST):  # NOTE : Not in counting first element of the list
		import math
		VAR = d0_exclude_1_variance(LIST)
		STD = math.sqrt(float(VAR))
		return STD

	def Counting(LIST, RANGE):
		counts = 0
		for i in range(len(LIST)):
			if i == 0:
				continue
			if ((float(LIST[i]) >= float(RANGE[0])) & (float(LIST[i]) < float(RANGE[1]))):
				counts = counts + 1
		return float(counts)

	def ADD_daily_date_FirstLine(START_YEAR=1996, START_MONTH=1, START_DAY=1, infilename="daily_test.txt"):
		filename_list = read_file_name(infilename)
		infile = filename_list[2]
		outfile = infile;
		outfile = outfile.replace(".txt", "")
		outfile = outfile + "_Daily.txt"
		year = START_YEAR
		month = START_MONTH
		day = START_DAY
		DATE_class = DATE_MAKER()
		Daily_date_list = [];
		Daily_date_list.append("DATE")
		for i in range(8036):
			DATE_num = DATE_class.DATE_MAKER(year, month, day)
			DATE_str = DATE_class.MAKE_DATE_STR(DATE_num)
			#        print(DATE_str[3])
			Daily_date_list.append(DATE_str[3])
			year = DATE_num[0]
			month = DATE_num[1]
			day = DATE_num[2] + 1
		Origin_row_list = MakeList(infile)
		#    print(Origin_row_list)
		return_list = []
		for i in range(len(Origin_row_list)):
			temp_list = []
			temp_list.append(Daily_date_list[i])
			for j in range(len(Origin_row_list[0])):
				temp_list.append(Origin_row_list[i][j])
			return_list.append(temp_list)
		MAKE_TXT(return_list, outfile)
		#    print(return_list)
		print("created file name : ", outfile)
		return outfile

	##### 2.
	def MakeMonthlyDate_BaseOnDailyDate(infilename="test.txt"):
		filename_list = read_file_name(infilename)
		infile = filename_list[2]
		outfile = infile;
		outfile = outfile.replace(".txt", "")
		outfile = outfile.replace("_Daily", "")
		outfile = outfile + "_Monthly.txt"
		row_list = MakeList(infile)
		return_list = [];
		return_list.append(row_list[0])
		refresh_date_flag = 1
		for i in range(len(row_list)):
			temp_list = []
			if (i == 0):
				continue
			if ((i == 1) | (refresh_date_flag == 0)):
				first_list = []
				iterated_num = 1
				month_date = row_list[i][0][:6]
				refresh_date_flag = 1
				temp_list.append(month_date)
				for j in range((len(row_list[0]) - 1)):
					temp_list.append(row_list[i][j + 1])
				first_list = temp_list
				#            print(first_list)
				continue

			if (row_list[i][0][:6] == month_date):
				for j in range((len(row_list[0]))):
					if (j == 0):
						temp_list.append(row_list[i][0][:6])
					else:
						calc = float(first_list[j]) + float(
							row_list[i][j]);  # calc = "%0.3f"%calc; str_calc = str(calc)
						temp_list.append(calc)
				first_list = temp_list
				iterated_num = iterated_num + 1
			#            print(first_list)

			if ((i == len(row_list) - 1)):
				return_temp_list = []
				for k in range(len(first_list)):
					if k == 0:
						return_temp_list.append(first_list[0])
					else:
						calc = float(first_list[k]) / float(iterated_num);
						calc = "%0.4f" % calc;
						str_calc = str(calc)
						return_temp_list.append(str_calc)
				return_list.append(return_temp_list)
				break

			if (row_list[i + 1][0][:6] != month_date):
				return_temp_list = []
				refresh_date_flag = 0
				for k in range(len(first_list)):
					if k == 0:
						return_temp_list.append(first_list[0])
					else:
						calc = float(first_list[k]) / float(iterated_num);
						calc = "%0.4f" % calc;
						str_calc = str(calc)
						return_temp_list.append(str_calc)
				return_list.append(return_temp_list)
		#    print(return_list)
		MAKE_TXT(return_list, outfile)
		print("created file name : ", outfile)
		return outfile


	def MakeYearlyDate_BaseOnMonthlyDate(infilename="test.txt"):
		filename_list = read_file_name(infilename)
		infile = filename_list[2]
		outfile = infile;
		outfile = outfile.replace(".txt", "")
		outfile = outfile.replace("_Monthly", "")
		outfile = outfile + "_Year.txt"
		# print(outfile)
		row_list = MakeList(infile)
		return_list = [];
		return_list.append(row_list[0])
		refresh_date_flag = 1
		for i in range(len(row_list)):
			temp_list = []
			if (i == 0):
				continue
			if ((i == 1) | (refresh_date_flag == 0)):
				first_list = []
				iterated_num = 1
				year_date = row_list[i][0][:4]
				refresh_date_flag = 1
				temp_list.append(year_date)
				for j in range((len(row_list[0]) - 1)):
					temp_list.append(row_list[i][j + 1])
				first_list = temp_list
				# print(first_list)
				continue
			if (row_list[i][0][:4] == year_date):
				for j in range((len(row_list[0]))):
					if (j == 0):
						temp_list.append(row_list[i][0][:4])
					else:
						calc = float(first_list[j]) + float(
							row_list[i][j]);  # calc = "%0.3f"%calc; str_calc = str(calc)
						temp_list.append(calc)
				first_list = temp_list
				iterated_num = iterated_num + 1
			# print(first_list)

			if ((i == len(row_list) - 1)):
				return_temp_list = []
				for k in range(len(first_list)):
					if k == 0:
						return_temp_list.append(first_list[0])
					else:
						calc = float(first_list[k]) / float(iterated_num);
						calc = "%0.4f" % calc;
						str_calc = str(calc)
						return_temp_list.append(str_calc)
				return_list.append(return_temp_list)
				break

			if (row_list[i + 1][0][:4] != year_date):
				return_temp_list = []
				refresh_date_flag = 0
				for k in range(len(first_list)):
					if k == 0:
						return_temp_list.append(first_list[0])
					else:
						calc = float(first_list[k]) / float(iterated_num);
						calc = "%0.4f" % calc;
						str_calc = str(calc)
						return_temp_list.append(str_calc)
				return_list.append(return_temp_list)
		print(return_list)
		MAKE_TXT(return_list, outfile)
		print("created file name : ", outfile)
		return outfile

	##### 4.
	def PICKING_BRANCH_n_SAVING(filename1):
		if (filename1[0] == "/"):
			filename1 = filename1
		elif (filename1[0] == '~'):
			filename1 = filename1.replace("~", os.environ['HOME'])
		elif ((filename1[0] == "C") & (filename1[1] == ":")):
			filename1 = filename1
		else:
			filename1 = os.getcwd() + "/" + filename1  # get the path included filename
		loca1 = len(filename1)
		for i in range(1, len(filename1) + 1):  # find the "/" location
			if (filename1[-i] == "/"):
				loca1 = i - 1
				break
		FILENAME1 = filename1.replace(filename1[:-loca1], "")  # this is the shorten filename
		filename1_No_Txt = FILENAME1.replace(".txt", "")
		infile1 = filename1
		print(infile1)

		RawList = MakeList(infile1)
		RawList_c = MakeList_column(infile1)
		num = 1

		print("Which branch do you want to extract? (Press 'q' to stop slecting)")
		for j in RawList[0]:
			print(num, ":", j, "", end="\n")
			num = num + 1

		# print("Please input branch name you want to extract")
		List_c = []

		print("Please input Branch Name(not branch number)!")
		for i in range(len(RawList[0])):
			print("Branch Name (Press 'q' to stop slecting): ", end='')
			Branch_name = input()
			if Branch_name in RawList[0]:
				index_num = 0
				for j in RawList[0]:
					if j == Branch_name:
						List_c.append(RawList_c[index_num])
						# print(List_c)
						break
					else:
						index_num = index_num + 1
					# print(index_num)
			elif Branch_name not in RawList[0] and Branch_name != "q":
				print("There are no such branches!")
			elif Branch_name == "q":
				break

		FN = infile1.replace(".txt", "_P.txt")
		Of = open(FN, "w+")
		for i in range(len(RawList)):
			for j in range(len(List_c)):
				Of.write("%s" % List_c[j][i])
				if (j != len(List_c) - 1):
					Of.write(" ")
				if (j == len(List_c) - 1):
					Of.write("\n")
		Of.close()
		return FN

	##### 5.
	def DATA_Merger(infilename1, infilename2):
		filename_list1 = read_file_name(infilename1)
		infile1 = filename_list1[2]
		filename_list2 = read_file_name(infilename2)
		infile2 = filename_list2[2]
		DATE_ROW = MakeList_column(infile1)
		DATA_ROW = MakeList_column(infile2)
		for i in range(len(DATA_ROW)):
			DATE_ROW.append(DATA_ROW[i])
		NEWNAME = infile1.replace(".txt", "_MERGE_" + filename_list2[0])
		FN = NEWNAME + ".txt"
		Of = open(FN, "w+")
		for j in range(len(DATE_ROW[0])):
			for i in range(len(DATE_ROW)):
				Of.write("%s" % DATE_ROW[i][j])
				if (i != len(DATE_ROW) - 1):
					Of.write(" ")
				else:
					Of.write("\n")

		#        Of.write("%s " %DATE_ROW[0][j])
		#        Of.write("%s\n" %DATE_ROW[1][j])
		Of.close()
		return FN

	def MakeList(filename):
		print(filename)
		if (filename[0] == "/"):
			filename = filename
		elif ((filename[0] == "C") & (filename[1] == ":")):
			filename = filename
		else:
			filename = os.getcwd() + "/" + filename  # get the path included filename
		loca = len(filename)
		for i in range(1, len(filename) + 1):  # find the "/" location
			if (filename[-i] == "/"):
				loca = i - 1
				break

	def MakeList_column(filename):
		Row_List = MakeList(filename)
		#    print(Row_List)
		Col_List = []
		for j in range(len(Row_List[0])):
			Temp_List = []
			for i in range(len(Row_List)):
				#            print(i)
				Temp_List.append(Row_List[i][j])
			Col_List.append(Temp_List)
		#        print(Col_List)
		return Col_List

	def min_max_range(LIST):
		MAX = float(LIST[1])
		MIN = float(LIST[1])
		for i in range(len(LIST)):
			if i == 0:
				continue
			if (float(LIST[i]) > MAX):
				MAX = float(LIST[i])
			if (float(LIST[i]) < MIN):
				MIN = float(LIST[i])
		L_lim = MIN - (MAX - MIN) * 0.05
		H_lim = MAX + (MAX - MIN) * 0.05
		return [MIN, MAX, L_lim, H_lim]

	def Month_divide(filename):
		FILE = read_file_name(filename)
		infile1 = FILE[2]
		OUTPUT_PATH = FILE[3] + FILE[0]
		COL_LIST1 = MakeList_column(infile1)

		# print(COL_LIST1)

		M_LIST = []

		for k in range(len(COL_LIST1[0])):
			gg = []
			for m in range(len(COL_LIST1)):
				gg.append(COL_LIST1[m][k])

			M_LIST.append(gg)
		#    if k==0:
		#        continue

		# print(M_LIST)

		RETURN_LIST = []
		bb = []
		for a in range(len(M_LIST)):
			#    aa=[]
			#    aa.append(M_LIST[a])
			if a > 1 and (float(M_LIST[a][0]) - float(M_LIST[a - 1][0])) > 1:
				# print(bb)
				FN = "M" + str(int(M_LIST[a - 1][0]) // 100) + ".txt"
				FN = OUTPUT_PATH + "_" + FN
				RETURN_LIST.append(FN)
				Of = open(FN, "w+")
				for i in range(len(bb)):
					for j in range(len(bb[i])):
						Of.write("%s" % bb[i][j])
						if (j != len(bb[i]) - 1):
							Of.write(" ")
						if (j == len(bb[i]) - 1):
							Of.write("\n")
				Of.close()
				bb = []
				bb.append(M_LIST[0])
				cc = bb
			bb.append(M_LIST[a])
		#    print(bb)
		# print(bb)
		# print(cc)
		FN = "M" + str(int(cc[1][0]) // 100) + ".txt"
		FN = OUTPUT_PATH + "_" + FN
		Of = open(FN, "w+")
		for i in range(len(cc)):
			for j in range(len(cc[i])):
				Of.write("%s" % cc[i][j])
				if (j != len(cc[i]) - 1):
					Of.write(" ")
				if (j == len(cc[i]) - 1):
					Of.write("\n")
		Of.close()
		RETURN_LIST.append(FN)
		return RETURN_LIST

	def N_sigma_skimming(filename, N_Of_Sigma=5):
		if (filename[0] == "/"):
			filename = filename
		elif ((filename[0] == "C") & (filename[1] == ":")):
			filename = filename
		else:
			filename = os.getcwd() + "/" + filename  # get the path included filename
		loca = len(filename)
		for i in range(1, len(filename) + 1):  # find the "/" location
			if (filename[-i] == "/"):
				loca = i - 1
				break
		FILENAME = filename.replace(filename[:-loca], "")  # this is the shorten filename
		filename_No_Txt = FILENAME.replace(".txt", "")
		infile = filename

		ROW_list = MakeList(infile)
		COL_list = MakeList_column(infile)

		Mean_list = list()
		Std_list = list()
		#    VAR_list = list()
		Name_list = list()
		for i in range(len(COL_list)):
			Name_list.append(COL_list[i][0])
			Mean_list.append(d0_exclude_1_mean((COL_list[i])))
			#        VAR_list.append(d0_exclude_1_variance((COL_list[i])))
			Std_list.append(d0_exclude_1_STD((COL_list[i])))
		#    print(Name_list)
		#    print(Mean_list)
		'''
		RE_COL_LIST = []
		for i in range(len(COL_list)): 
			if((COL_list[i][0] == DATE) | (COL_list[i][0] == HOLI) | (COL_list[i][0] == DAYS)): 
				continue
			L_NSIGMA = Mean_list[i] - N_Of_Sigma*Std_list[i]
			H_NSIGMA = Mean_list[i] + N_Of_Sigma*Std_list[i]

			for j in range(len(COL_list[i])):
		'''
		ttt = 0
		RE_ROW_LIST = []
		for i in range(len(ROW_list)):
			if (i == 0):
				RE_ROW_LIST.append(ROW_list[i])
				continue
			for j in range(len(ROW_list[i])):
				if (((Name_list[j] == "DATE") | (Name_list[j] == "HOLI") | (Name_list[j] == "DAYS")) & (
						j != (len(ROW_list[i]) - 1))):
					continue
				L_NSIGMA = Mean_list[j] - N_Of_Sigma * Std_list[j]
				H_NSIGMA = Mean_list[j] + N_Of_Sigma * Std_list[j]
				#            print(L_NSIGMA, H_NSIGMA)
				if ((j == (len(ROW_list[i]) - 1)) & (
						(Name_list[j] == "DATE") | (Name_list[j] == "HOLI") | (Name_list[j] == "DAYS"))):
					RE_ROW_LIST.append(ROW_list[i])
				elif ((float(ROW_list[i][j]) > L_NSIGMA) & (float(ROW_list[i][j]) < H_NSIGMA)):
					if (j == (len(ROW_list[i]) - 1)):
						RE_ROW_LIST.append(ROW_list[i])
					else:
						continue
				else:
					ttt = ttt + 1
					break
		#    print(ttt)
		#    print(RE_ROW_LIST)

		FN = infile.replace(".txt", "S.txt")
		Of = open(FN, "w+")
		for i in range(len(RE_ROW_LIST)):
			for j in range(len(RE_ROW_LIST[i])):
				Of.write("%s" % RE_ROW_LIST[i][j])
				if (j != len(RE_ROW_LIST[i]) - 1):
					Of.write(" ")
				if (j == len(RE_ROW_LIST[i]) - 1):
					Of.write("\n")
		Of.close()
		#    print(FN)
		return FN

	def Merge(filename1, filename2):

		if (filename1[0] == "/"):
			filename1 = filename1
		elif ((filename1[0] == "C") & (filename1[1] == ":")):
			filename1 = filename1
		else:
			filename1 = os.getcwd() + "/" + filename1  # get the path included filename
		loca1 = len(filename1)
		for i in range(1, len(filename1) + 1):  # find the "/" location
			if (filename1[-i] == "/"):
				loca1 = i - 1
				break
		FILENAME1 = filename1.replace(filename1[:-loca1], "")  # this is the shorten filename
		filename1_No_Txt = FILENAME1.replace(".txt", "")
		infile1 = filename1

		if (filename2[0] == "/"):
			filename2 = filename2
		elif ((filename2[0] == "C") & (filename2[1] == ":")):
			filename2 = filename2
		else:
			filename2 = os.getcwd() + "/" + filename2  # get the path included filename
		loca2 = len(filename2)
		for i in range(1, len(filename2) + 1):  # find the "/" location
			if (filename2[-i] == "/"):
				loca2 = i - 1
				break
		FILENAME2 = filename2.replace(filename2[:-loca2], "")  # this is the shorten filename
		filename2_No_Txt = FILENAME2.replace(".txt", "")
		infile2 = filename2

		DATE_ROW = MakeList_column(infile1)
		DATA_ROW = MakeList_column(infile2)
		#    DATE_ROW.append(DATA_ROW[0])
		for i in range(len(DATA_ROW)):
			DATE_ROW.append(DATA_ROW[i])
		#    print(DATE_ROW)
		#    print(len(DATE_ROW[0]))
		#    print(len(DATE_ROW[1]))

		NEWNAME = infile1.replace(".txt", "_MERGE_" + filename2_No_Txt)
		FN = NEWNAME + ".txt"
		Of = open(FN, "w+")
		for j in range(len(DATE_ROW[0])):
			for i in range(len(DATE_ROW)):
				if DATE_ROW[i][j] is None:
					continue
				else:
					Of.write("%s" % DATE_ROW[i][j])
					if (i != len(DATE_ROW) - 1):
						Of.write(" ")
					else:
						Of.write("\n")

		#        Of.write("%s " %DATE_ROW[0][j])
		#        Of.write("%s\n" %DATE_ROW[1][j])
		Of.close()
		return FN

	def formation(filename1, filename2):  # it's the function which make file2 same format of file1

		if (filename1[0] == "/"):
			filename1 = filename1
		elif ((filename1[0] == "C") & (filename1[1] == ":")):
			filename1 = filename1
		else:
			filename1 = os.getcwd() + "/" + filename1  # get the path included filename
		loca1 = len(filename1)
		for i in range(1, len(filename1) + 1):  # find the "/" location
			if (filename1[-i] == "/"):
				loca1 = i - 1
				break
		FILENAME1 = filename1.replace(filename1[:-loca1], "")  # this is the shorten filename
		filename1_No_Txt = FILENAME1.replace(".txt", "")
		infile1 = filename1

		if (filename2[0] == "/"):
			filename2 = filename2
		elif ((filename2[0] == "C") & (filename2[1] == ":")):
			filename2 = filename2
		else:
			filename2 = os.getcwd() + "/" + filename2  # get the path included filename
		loca2 = len(filename2)
		for i in range(1, len(filename2) + 1):  # find the "/" location
			if (filename2[-i] == "/"):
				loca2 = i - 1
				break
		FILENAME2 = filename2.replace(filename2[:-loca2], "")  # this is the shorten filename
		filename2_No_Txt = FILENAME2.replace(".txt", "")
		infile2 = filename2

		DATE_ROW = MakeList_column(infile1)
		DATA_ROW = MakeList_column(infile2)
		'''
		con = 1
		while con >0
			a = input("What Colume do you want to add?")
		'''

		form_date = DATE_ROW[0]
		data_date = DATA_ROW[0]
		list_amount = DATA_ROW[8]
		list_volume = DATA_ROW[7]
		ch_amount = []
		ch_volume = []
		j = 1
		nones = 0
		for i in range(len(form_date)):
			if i == 0:
				ch_amount.append(list_amount[i])
				ch_volume.append(list_volume[i])
				continue
			else:
				while 1:
					if j >= (len(data_date) - 1):
						ch_amount.append(None)
						ch_volume.append(None)
						nones += 1
						j = 1
						break
					elif form_date[i] == data_date[j]:
						a = list_amount[j].replace(',', '')
						b = list_volume[j].replace(',', '')
						ch_amount.append(a)
						ch_volume.append(b)
						break
					else:
						j += 1
		NEWNAME = infile1.replace(".txt", "_Changed_" + filename2_No_Txt)
		FN = NEWNAME + ".txt"
		Of = open(FN, "w+")
		for j in range(len(ch_amount)):
			Of.write(str(ch_amount[j]) + " " + str(ch_volume[j]) + "\n")

		Of.close()
		return FN


	def missing_value(filename1):
		if (filename1[0] == "/"):
			filename1 = filename1
		elif ((filename1[0] == "C") & (filename1[1] == ":")):
			filename1 = filename1
		else:
			filename1 = os.getcwd() + "/" + filename1  # get the path included filename
		loca1 = len(filename1)
		for i in range(1, len(filename1) + 1):  # find the "/" location
			if (filename1[-i] == "/"):
				loca1 = i - 1
				break
		FILENAME1 = filename1.replace(filename1[:-loca1], "")  # this is the shorten filename
		filename1_No_Txt = FILENAME1.replace(".txt", "")
		infile1 = filename1
		DATA_ROW = MakeList_column(infile1)
		arr_row = np.array(DATA_ROW)
		i, j = 0, 0
		print(len(arr_row), len(arr_row[0]))
		while i <= (len(arr_row) - 1):
			while j <= (len(arr_row[0]) - 1):
				if arr_row[i][j] == 'None':
					# print(1)
					arr_row = np.delete(arr_row, j, axis=1)
				else:
					j += 1
			i += 1
			j = 0
		NEWNAME = infile1.replace(filename1_No_Txt + ".txt", "missing_deleted_" + filename1_No_Txt)
		FN = NEWNAME + ".txt"
		Of = open(FN, "w+")
		for j in range(len(arr_row[0])):
			for i in range(len(arr_row)):
				if i == (len(arr_row) - 1):
					Of.write(arr_row[i][j] + "\n")
				else:
					Of.write(arr_row[i][j] + " ")

		Of.close()
		return FN

	def show_branch(filename1):
		if (filename1[0] == "/"):
			filename1 = filename1
		elif (filename1[0] == '~'):
			filename1 = filename1.replace("~", os.environ['HOME'])
		elif ((filename1[0] == "C") & (filename1[1] == ":")):
			filename1 = filename1
		else:
			filename1 = os.getcwd() + "/" + filename1  # get the path included filename
		loca1 = len(filename1)
		for i in range(1, len(filename1) + 1):  # find the "/" location
			if (filename1[-i] == "/"):
				loca1 = i - 1
				break
		FILENAME1 = filename1.replace(filename1[:-loca1], "")  # this is the shorten filename
		filename1_No_Txt = FILENAME1.replace(".txt", "")
		infile1 = filename1
		print(infile1)

		RawList = MakeList(infile1)
		RawList_c = MakeList_column(infile1)
		num = 1

		print("Which branch do you want to extract? (Press 'q' to stop slecting)")
		for j in RawList[0]:
			print(num, ":", j, "", end="\n")
			num = num + 1

		# print("Please input branch name you want to extract")
		List_c = []

		print("Please input Branch Name(not branch number)!")
		for i in range(len(RawList[0])):
			print("Branch Name (Press 'q' to stop slecting): ", end='')
			Branch_name = input()
			if Branch_name in RawList[0]:
				index_num = 0
				for j in RawList[0]:
					if j == Branch_name:
						List_c.append(RawList_c[index_num])
						# print(List_c)
						break
					else:
						index_num = index_num + 1
					# print(index_num)
			elif Branch_name not in RawList[0] and Branch_name != "q":
				print("There are no such branches!")
			elif Branch_name == "q":
				break

		FN = infile1.replace(".txt", "_P.txt")
		Of = open(FN, "w+")
		for i in range(len(RawList)):
			for j in range(len(List_c)):
				Of.write("%s" % List_c[j][i])
				if (j != len(List_c) - 1):
					Of.write(" ")
				if (j == len(List_c) - 1):
					Of.write("\n")
		Of.close()
		return FN

	def MakeTXT(filename):
		if (filename[0] == "/"):
			filename = filename
		elif ((filename[0] == "C") & (filename[1] == ":")):
			filename = filename
		else:
			filename = os.getcwd() + "/" + filename  # get the path included filename
		loca = len(filename)
		for i in range(1, len(filename) + 1):  # find the "/" location
			if (filename[-i] == "/"):
				loca = i - 1
				break

		FILENAME = filename.replace(filename[:-loca], "")  # this is the shorten filename
		filename_No_Txt = FILENAME.replace(".txt", "")
		infile = filename

		ff = open(infile, "r")
		FILE_LIST = []
		for line in ff:
			FILE_LIST.append(line.split())
		ff.close()
		'''    
		for i in range(FILE_LIST):
			for j in range(FILE_LIST[i]):
				FILE_LIST[i][j] =  
		'''
		LEN = len(FILE_LIST)
		clen = len(FILE_LIST[0])
		KLIST = []
		for i in range(LEN):
			if ((len(FILE_LIST[i]) == 1) & (FILE_LIST[i][0] == '\x00')):
				pass
			else:
				KLIST.append(FILE_LIST[i])

		LEN = len(KLIST)
		KKLIST = []
		for i in range(LEN):
			for j in range(len(KLIST[i])):
				KLIST[i][j] = KLIST[i][j].replace('\x00', "")
				KLIST[i][j] = KLIST[i][j].replace('\xff\xfe', '')
			KKLIST.append(KLIST[i])

		for i in range(len(KKLIST)):
			KKLIST[i] = list(filter(None, KKLIST[i]))

		FN = infile.replace(".txt", "R.txt")
		Of = open(FN, "w+")
		for i in range(len(KKLIST)):
			for j in range(len(KKLIST[i])):
				Of.write("%s" % KKLIST[i][j])
				if (j != len(KKLIST[i]) - 1):
					Of.write(" ")
				if (j == len(KKLIST[i]) - 1):
					Of.write("\n")
		Of.close()

		return FN

	def make_monthly_data(filename):
		if (filename[0] == "/"):
			filename = filename
		else:
			filename = os.getcwd() + "/" + filename  # get the path included filename
		loca = len(filename)
		for i in range(1, len(filename) + 1):  # find the "/" location
			if (filename[-i] == "/"):
				loca = i - 1
				break

		FILENAME = filename.replace(filename[:-loca], "")  # this is the shorten filename
		filename_No_Txt = FILENAME.replace(".txt", "")
		infile = filename

		tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
		iterator = 0
		SAVENAME = filename_No_Txt + "_monthly.txt"
		print(SAVENAME)
		f = open(SAVENAME, "w+")
		OLD_LIST = MakeList(infile)

		##################################
		#### 2013
		for i in range(len(OLD_LIST)):
			if (i == 0):
				f.write('DATE AQI PM2p5 PM10 SO2 CO NO2 O3_8h\n')
				continue;
			#        print(OLD_LIST[i][0])
			if ((int(OLD_LIST[i][0]) > 20131200) & (int(OLD_LIST[i][0]) < 20140100)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20140100):
					#                f.write("201312 %f %f %f %f %f %f %f" %(tempAqi/iterator) (tempAqi/iterator) )
					f.write("201312 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")
					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			##################################
			#### 2014
			if ((int(OLD_LIST[i][0]) > 20140100) & (int(OLD_LIST[i][0]) < 20140200)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20140200):
					f.write("201401 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")
					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20140200) & (int(OLD_LIST[i][0]) < 20140300)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20140300):
					f.write("201402 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")
					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20140300) & (int(OLD_LIST[i][0]) < 20140400)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20140400):
					f.write("201403 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20140400) & (int(OLD_LIST[i][0]) < 20140500)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20140500):
					f.write("201404 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20140500) & (int(OLD_LIST[i][0]) < 20140600)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20140600):
					f.write("201405 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20140600) & (int(OLD_LIST[i][0]) < 20140700)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20140700):
					f.write("201406 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20140700) & (int(OLD_LIST[i][0]) < 20140800)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20140800):
					f.write("201407 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20140800) & (int(OLD_LIST[i][0]) < 20140900)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20140900):
					f.write("201408 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20140900) & (int(OLD_LIST[i][0]) < 20141000)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20141000):
					f.write("201409 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20141000) & (int(OLD_LIST[i][0]) < 20141100)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20141100):
					f.write("201410 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20141100) & (int(OLD_LIST[i][0]) < 20141200)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20141200):
					f.write("201411 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20141200) & (int(OLD_LIST[i][0]) < 20150100)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20150100):
					f.write("201412 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			##################################
			#### 2015

			if ((int(OLD_LIST[i][0]) > 20150100) & (int(OLD_LIST[i][0]) < 20150200)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20150200):
					f.write("201501 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20150200) & (int(OLD_LIST[i][0]) < 20150300)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20150300):
					f.write("201502 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20150300) & (int(OLD_LIST[i][0]) < 20150400)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20150400):
					f.write("201503 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20150400) & (int(OLD_LIST[i][0]) < 20150500)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20150500):
					f.write("201504 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20150500) & (int(OLD_LIST[i][0]) < 20150600)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20150600):
					f.write("201505 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20150600) & (int(OLD_LIST[i][0]) < 20150700)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20150700):
					f.write("201506 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20150700) & (int(OLD_LIST[i][0]) < 20150800)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20150800):
					f.write("201507 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20150800) & (int(OLD_LIST[i][0]) < 20150900)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20150900):
					f.write("201508 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20150900) & (int(OLD_LIST[i][0]) < 20151000)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20151000):
					f.write("201509 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20151000) & (int(OLD_LIST[i][0]) < 20151100)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20151100):
					f.write("201510 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20151100) & (int(OLD_LIST[i][0]) < 20151200)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20151200):
					#                print(tempAqi, iterator)
					f.write("201511 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20151200) & (int(OLD_LIST[i][0]) < 20160100)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20160100):
					f.write("201512 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			##################################
			#### 2016

			if ((int(OLD_LIST[i][0]) > 20160100) & (int(OLD_LIST[i][0]) < 20160200)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20160200):
					f.write("201601 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20160200) & (int(OLD_LIST[i][0]) < 20160300)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20160300):
					f.write("201602 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20160300) & (int(OLD_LIST[i][0]) < 20160400)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20160400):
					f.write("201603 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20160400) & (int(OLD_LIST[i][0]) < 20160500)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20160500):
					f.write("201604 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20160500) & (int(OLD_LIST[i][0]) < 20160600)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20160600):
					f.write("201605 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20160600) & (int(OLD_LIST[i][0]) < 20160700)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20160700):
					f.write("201606 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20160700) & (int(OLD_LIST[i][0]) < 20160800)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20160800):
					f.write("201607 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20160800) & (int(OLD_LIST[i][0]) < 20160900)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20160900):
					f.write("201608 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20160900) & (int(OLD_LIST[i][0]) < 20161000)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20161000):
					f.write("201609 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20161000) & (int(OLD_LIST[i][0]) < 20161100)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20161100):
					f.write("201610 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20161100) & (int(OLD_LIST[i][0]) < 20161200)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20161200):
					f.write("201611 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20161200) & (int(OLD_LIST[i][0]) < 20170100)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20170100):
					f.write("201612 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			##################################
			#### 2017

			if ((int(OLD_LIST[i][0]) > 20170100) & (int(OLD_LIST[i][0]) < 20170200)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20170200):
					f.write("201701 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20170200) & (int(OLD_LIST[i][0]) < 20170300)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20170300):
					f.write("201702 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20170300) & (int(OLD_LIST[i][0]) < 20170400)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20170400):
					f.write("201703 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20170400) & (int(OLD_LIST[i][0]) < 20170500)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20170500):
					f.write("201704 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20170500) & (int(OLD_LIST[i][0]) < 20170600)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20170600):
					f.write("201705 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20170600) & (int(OLD_LIST[i][0]) < 20170700)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20170700):
					f.write("201706 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20170700) & (int(OLD_LIST[i][0]) < 20170800)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20170800):
					f.write("201707 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20170800) & (int(OLD_LIST[i][0]) < 20170900)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20170900):
					f.write("201708 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20170900) & (int(OLD_LIST[i][0]) < 20171000)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20171000):
					f.write("201709 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20171000) & (int(OLD_LIST[i][0]) < 20171100)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20171100):
					f.write("201710 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20171100) & (int(OLD_LIST[i][0]) < 20171200)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20171200):
					f.write("201711 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20171200) & (int(OLD_LIST[i][0]) < 20180100)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20180100):
					f.write("201712 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			##################################
			#### 2018

			if ((int(OLD_LIST[i][0]) > 20180100) & (int(OLD_LIST[i][0]) < 20180200)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20180200):
					f.write("201801 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0

			if ((int(OLD_LIST[i][0]) > 20180200) & (int(OLD_LIST[i][0]) < 20180300)):
				tempAqi = tempAqi + float(OLD_LIST[i][1])
				pm2p5 = pm2p5 + float(OLD_LIST[i][2])
				pm10 = pm10 + float(OLD_LIST[i][3])
				so2 = so2 + float(OLD_LIST[i][4])
				co = co + float(OLD_LIST[i][5])
				no2 = no2 + float(OLD_LIST[i][6])
				o3_8h = o3_8h + float(OLD_LIST[i][7])
				iterator = iterator + 1
				if (int(OLD_LIST[i + 1][0]) > 20180300):
					f.write("201802 %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f %0.1f" % (
					(tempAqi / iterator), (pm2p5 / iterator), (pm10 / iterator), (so2 / iterator), (co / iterator),
					(no2 / iterator), (o3_8h / iterator)))
					f.write("\n")

					tempAqi, pm2p5, pm10, so2, co, no2, o3_8h = 0, 0, 0, 0, 0, 0, 0
					iterator = 0


