import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import sys,os
from scipy import stats
import math
#from statsmodels.stats import weightstats
from scipy.stats import chi2
#from statsmodels.stats import proportion
from scipy.stats import f as F_TEST
from sympy import exp,sqrt,pi,Integral

class c_funcs(object):

	def __init__(self):
		num = 0
	def help(num=1):
		localval3 = 300    #函数内部的局部变量
		print("Show all functions list and infos")
		# ex) mean(x) : x is the data which will be averaged, and it's data type is 'list'; the output is x's mean value, data type is 'float'.
	    # read_file_name(filename) , returning [filename, filename.txt, absolute path filename.txt, absolute path]
	def read_file_name(filename):

		if(filename[0] == '/'):                 # 'filename' of absoulte location
			filename = filename
		elif(filename[0] == '~'):
			filename = filename.replace("~",os.environ['HOME'])
		elif((filename[0]=="C")&(filename[1]==":")):
			filename = filename
		else:
			filename = os.getcwd() + "/" + filename

		loca = len(filename)
		for i in range(1,len(filename)+1):       # find the "/" location
			if(filename[-i] == '/'):
				loca = i-1
				break
		FILENAME = filename.replace(filename[:-loca],"")
		FILE = FILENAME.replace(".txt","")    #filetxt
		filename_NoRoot = filename.replace(filename[len(filename)-loca:len(filename)],"")

		filelist = [FILE, FILENAME, filename, filename_NoRoot]
		return(filelist)

	def Counting_range(LIST, RANGE):
		counts = 0
		for i in range(len(LIST)):
			if i == 0:
				continue
			if ((float(LIST[i]) >= float(RANGE[0])) & (float(LIST[i]) < float(RANGE[1]))):
				counts = counts + 1
		return float(counts)


	def bin_num(filename):
		infile = open(filename, "r")
		ii = 0
		for line in infile:
			ii = ii + 1
		infile.close()
		return ii


	def most_frequent_bin(filename):
		infile = open(filename, "r")
		point = 0.0
		W = 0
		for line in infile:
			binN, ibin, fbin, entry = line.split()
			if (float(entry) >= point):
				point = float(entry)
				IBIN = ibin
				FBIN = fbin
				BINN = binN

		for line in infile:
			_, _, _, entry = line.split()
			if (entry == point):
				W = W + 1

		if (W >= 2):
			print("There are", W, " mode points!")
			return None
		RLIST = [];
		RLIST.append(float(IBIN));
		RLIST.append(float(FBIN))
		LIST = []
		LIST.append(BINN + "th bin");
		LIST.append(RLIST);
		LIST.append(point)
		#    print(LIST)
		infile.close()
		return LIST


	def c1_median(filename):
		ENTRY = c1_total_ENTRY(filename)
		infile = open(filename, "r")

		Entry = 0.0
		for line in infile:
			point = 0
			binN, ibin, fbin, entry = line.split()
			if (Entry < ENTRY / 2):
				point = point + 1
			Entry = Entry + float(entry)
			if (Entry > ENTRY / 2):
				point = point + 1
			if (point == 2):
				break
		RANGE = []
		RANGE.append(float(ibin));
		RANGE.append(float(fbin))
		MEDIAN = []
		MEDIAN.append(binN + "th bin")
		MEDIAN.append(RANGE)
		#    print(MEDIAN)
		infile.close()
		return (MEDIAN)


	def c1_data_range(filename):
		infile = open(filename, "r")
		DATA_RANGE = []
		Init = 0
		Final = 1
		count = len(open(filename, 'rU').readlines())
		Num = 0
		for line in infile:
			Num = Num + 1
			_, ibin, fbin, entry = line.split()
			if ((Init == 0) & (float(entry) > 0.0)):
				Start_point = ibin
				Init = 1
			if ((float(entry) == 0.0) & (Final == 0)):
				End_point = ibin
			if ((float(entry) > 0.0)):
				Final = 0
			else:
				Final = 1
			if ((Num == count) & (entry != 0)):
				End_point = fbin
		DATA_RANGE.append(float(Start_point))
		DATA_RANGE.append(float(End_point))

		#    print(DATA_RANGE)
		infile.close()
		return DATA_RANGE


	def c1_total_ENTRY(filename):
		infile = open(filename, "r")
		LEntry = []
		Total_Entry = 0
		for line in infile:
			_, _, _, entry = line.split()
			LEntry.append(float(entry))
			Total_Entry = Total_Entry + float(entry)
		#    print(" Total Entry Number =",int(Total_Entry),"!!!!")
		infile.close()
		return Total_Entry


	def c1_mean(filename):
		import os
		infile = open(filename, "r")

		BinN = []
		LIBin = []
		LFBin = []
		LMBin = []  # List of middle Bin
		LEntry = []
		Total_Entry = 0
		for line in infile:
			binN, xaxis0, xaxis1, entry = line.split()
			BinN.append(int(binN))
			LIBin.append(float(xaxis0))
			LFBin.append(float(xaxis1))
			LMBin.append(float(xaxis0) + ((float(xaxis1) - float(xaxis0))) / 2)
			LEntry.append(float(entry))
			Total_Entry = Total_Entry + float(entry)

		med = 0
		for i in range(len(LMBin)):
			med = med + LEntry[i] * LMBin[i]
		MEAN = med / Total_Entry
		#    print(" Mean Value =",MEAN,"!!!!")
		infile.close()
		return MEAN


	def c1_square_sum(filename):
		import os
		infile = open(filename, "r")
		BinN = []
		LIBin = []
		LFBin = []
		LMBin = []  # List of middle Bin
		LEntry = []
		Total_Entry = 0
		for line in infile:
			binN, xaxis0, xaxis1, entry = line.split()
			BinN.append(int(binN))
			LIBin.append(float(xaxis0))
			LFBin.append(float(xaxis1))
			LMBin.append(float(xaxis0) + ((float(xaxis1) - float(xaxis0))) / 2)
			LEntry.append(float(entry))
			Total_Entry = Total_Entry + float(entry)
		Square_Sum = 0
		for i in range(len(LMBin)):
			if (LEntry[i] == 0.0):
				continue
			else:
				deno = float(LFBin[i] - LIBin[i]) / float(LEntry[i])
				for j in range((int(LEntry[i]))):
					deno_m = float(LIBin[i]) + deno * (2 * j + 1) / 2
					Square_Sum = Square_Sum + deno_m * deno_m
		infile.close()
		return Square_Sum

	def c1_variance(filename):  # actually, this is variance of a sample from population.
		import os
		infile = open(filename, "r")
		BinN = []
		LIBin = []
		LFBin = []
		LMBin = []  # List of middle Bin
		LEntry = []
		Total_Entry = 0
		for line in infile:
			binN, xaxis0, xaxis1, entry = line.split()
			BinN.append(int(binN))
			LIBin.append(float(xaxis0))
			LFBin.append(float(xaxis1))
			LMBin.append(float(xaxis0) + ((float(xaxis1) - float(xaxis0))) / 2)
			LEntry.append(float(entry))
			Total_Entry = Total_Entry + float(entry)

		MEAN = c1_mean(filename)
		med_var = 0
		'''
		for i in range(len(LMBin)):
			for j in range((int(LEntry[i]))):
				med_var = med_var + (LMBin[i] - MEAN)*(LMBin[i] - MEAN)
		'''
		for i in range(len(LMBin)):
			if (LEntry[i] == 0.0):
				continue
			else:
				deno = float(LFBin[i] - LIBin[i]) / float(LEntry[i])
				for j in range((int(LEntry[i]))):
					deno_m = float(LIBin[i]) + deno * (2 * j + 1) / 2
					med_var = med_var + (deno_m - MEAN) * (deno_m - MEAN)

		VAR = med_var / (Total_Entry - 1)

		#    print(" Variance Value =",VAR,"!!!!")
		infile.close()
		return VAR

	def c1_standard_deviation(filename):
		import os
		import math

		VAR = c1_variance(filename)
		STD = math.sqrt(VAR)

		#    print(" Standard Deviation Value =",STD,"!!!!")
		return STD


	def c1_sample_standard_error_of_mean(filename):
		import os
		import math
		STD = c1_standard_deviation(filename)
		TOT = c1_total_ENTRY(filename)
		SSEM = STD / (math.sqrt(TOT))

		return SSEM

	def Basic_histo(filename, calc_file='', Xaxis_Name='', norm=0):

		if calc_file == '':
			calc_file = filename

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

		if (calc_file[0] == "/"):
			calc_file = calc_file
		elif ((calc_file[0] == "C") & (calc_file[1] == ":")):
			calc_file = calc_file
		else:
			calc_file = os.getcwd() + "/" + calc_file  # get the path included calc_file
		loca = len(calc_file)
		for i in range(1, len(calc_file) + 1):  # find the "/" location
			if (calc_file[-i] == "/"):
				loca = i - 1
				break

		FILENAME = calc_file.replace(calc_file[:-loca], "")  # this is the shorten calc_file
		calc_file_No_Txt = FILENAME.replace(".txt", "")

		infile = filename
		calc_infile = calc_file

		Mode = most_frequent_bin(infile);  # print(type(Mode)); print(Mode)
		Median = c1_median(calc_infile)
		Range = c1_data_range(calc_infile);  # print(Range)
		Total_Entry = c1_total_ENTRY(calc_infile);
		Total_Entry = int(Total_Entry);
		str_TE = str(Total_Entry)
		Mean = c1_mean(calc_infile);
		str_Mean = str(Mean)
		Var = c1_variance(calc_infile);
		Std = c1_standard_deviation(calc_infile);
		str_Std = str(Std)

		str_Mean = str_Mean[:len(str_TE) + 2];  # print(str_Mean)
		str_Std = str_Std[:len(str_TE) + 2];  # print(str_Std)

		X_AXIS = []
		X_WIDTH = []
		Y_VALUE = []

		f = open(infile, 'r')
		BinN = 0
		for line in f:
			_, xaxis0, xaxis1, yaxis = line.split()
			X_AXIS.append(float(xaxis0) + (float(xaxis1) - float(xaxis0)) / 2)
			X_WIDTH.append((float(xaxis1) - float(xaxis0)))
			Y_VALUE.append(float(yaxis))
			BinN = BinN + 1
		#    print(X_AXIS[0]); print(X_AXIS[BinN-1])

		WEIGHT = 1
		if (norm == 1):
			WEIGHT = float(Total_Entry)
		for i in range(len(Y_VALUE)):
			Y_VALUE[i] = float(Y_VALUE[i]) / WEIGHT

		fig = plt.figure(1)
		#    barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0])
		barlist = plt.bar(X_AXIS, Y_VALUE, X_WIDTH[0], fill=False)
		#    print(len(barlist))
		for i in range(len(barlist)):
			barlist[i].set_color('b')
		plt.axis([X_AXIS[0], X_AXIS[BinN - 1], 0, Mode[2] * 10 / 9 / WEIGHT])
		TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "Mean : " + str_Mean + "\n" + "Std : " + str_Std
		plt.text(Range[1] - (Range[1] - Range[0]) * 0.05, Mode[2] * 21 / 20 / WEIGHT, TEXT, fontsize=16, ha='right',
				 va='top', rotation=0)
		#    print(plt.ylim()); print(type(plt.ylim()))
		plt.ylabel("Entry Number")
		if (Xaxis_Name == ''):
			XLABEL = filename_No_Txt.replace("_hist", '')
		else:
			XLABEL = Xaxis_Name
		plt.xlabel(XLABEL)
		plt.title(filename_No_Txt)
		SaveName = filename_No_Txt + ".pdf"
		plt.grid(True)
		plt.savefig(SaveName)
		#    plt.show()
		plt.close('all')
		f.close()

	def looping_Basic_histo(filenameList, Xaxis_Name=''):
		for filename in filenameList:
			Basic_histo(filename, Xaxis_Name='')

	def Basic_histo(filename, calc_file='', Xaxis_Name='', norm=0):

		if calc_file == '':
			calc_file = filename

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

		if (calc_file[0] == "/"):
			calc_file = calc_file
		elif ((calc_file[0] == "C") & (calc_file[1] == ":")):
			calc_file = calc_file
		else:
			calc_file = os.getcwd() + "/" + calc_file  # get the path included calc_file
		loca = len(calc_file)
		for i in range(1, len(calc_file) + 1):  # find the "/" location
			if (calc_file[-i] == "/"):
				loca = i - 1
				break

		FILENAME = calc_file.replace(calc_file[:-loca], "")  # this is the shorten calc_file
		calc_file_No_Txt = FILENAME.replace(".txt", "")

		infile = filename
		calc_infile = calc_file

		Mode = most_frequent_bin(infile);  # print(type(Mode)); print(Mode)
		Median = c1_median(calc_infile)
		Range = c1_data_range(calc_infile);  # print(Range)
		Total_Entry = c1_total_ENTRY(calc_infile);
		Total_Entry = int(Total_Entry);
		str_TE = str(Total_Entry)
		Mean = c1_mean(calc_infile);
		str_Mean = str(Mean)
		Var = c1_variance(calc_infile);
		Std = c1_standard_deviation(calc_infile);
		str_Std = str(Std)

		str_Mean = str_Mean[:len(str_TE) + 2];  # print(str_Mean)
		str_Std = str_Std[:len(str_TE) + 2];  # print(str_Std)

		X_AXIS = []
		X_WIDTH = []
		Y_VALUE = []

		f = open(infile, 'r')
		BinN = 0
		for line in f:
			_, xaxis0, xaxis1, yaxis = line.split()
			X_AXIS.append(float(xaxis0) + (float(xaxis1) - float(xaxis0)) / 2)
			X_WIDTH.append((float(xaxis1) - float(xaxis0)))
			Y_VALUE.append(float(yaxis))
			BinN = BinN + 1
		#    print(X_AXIS[0]); print(X_AXIS[BinN-1])

		WEIGHT = 1
		if (norm == 1):
			WEIGHT = float(Total_Entry)
		for i in range(len(Y_VALUE)):
			Y_VALUE[i] = float(Y_VALUE[i]) / WEIGHT

		fig = plt.figure(1)
		#    barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0])
		barlist = plt.bar(X_AXIS, Y_VALUE, X_WIDTH[0], fill=False)
		#    print(len(barlist))
		for i in range(len(barlist)):
			barlist[i].set_color('b')
		plt.axis([X_AXIS[0], X_AXIS[BinN - 1], 0, Mode[2] * 10 / 9 / WEIGHT])
		TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "Mean : " + str_Mean + "\n" + "Std : " + str_Std
		plt.text(Range[1] - (Range[1] - Range[0]) * 0.05, Mode[2] * 21 / 20 / WEIGHT, TEXT, fontsize=16, ha='right',
				 va='top', rotation=0)
		#    print(plt.ylim()); print(type(plt.ylim()))
		plt.ylabel("Entry Number")
		if (Xaxis_Name == ''):
			XLABEL = filename_No_Txt.replace("_hist", '')
		else:
			XLABEL = Xaxis_Name
		plt.xlabel(XLABEL)
		plt.title(filename_No_Txt)
		SaveName = filename_No_Txt + ".pdf"
		plt.grid(True)
		plt.savefig(SaveName)
		#    plt.show()
		plt.close('all')
		f.close()

	def looping_Basic_histo(filenameList, Xaxis_Name=''):
		for filename in filenameList:
			Basic_histo(filename, Xaxis_Name='')

	def Fit_Gaus_histo(filename, Xaxis_Name='', norm=0, SIGMA=2):

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
		BIN_NUM = bin_num(infile);  # print(BIN_NUM)
		Mode = most_frequent_bin(infile);  # print(type(Mode)); print(Mode)
		Median = c1_median(infile)
		Range = c1_data_range(infile);  # print(Range)
		Total_Entry = c1_total_ENTRY(infile);
		Total_Entry = int(Total_Entry);
		str_TE = str(Total_Entry)
		Mean = c1_mean(infile);
		str_Mean = str(Mean)
		Var = c1_variance(infile);
		Std = c1_standard_deviation(infile);
		str_Std = str(Std)

		FROM = Range[0];
		END = Range[1];  # print(BIN_NUM, FROM, END)
		Brange = (END - FROM) / BIN_NUM;
		t = np.arange(FROM, END, Brange)
		gaussian = (1 / (Std * np.sqrt(2 * np.pi)) * np.exp(-(t - Mean) ** 2 / (2 * Std ** 2)))
		TJG = 0
		for i in range(len(gaussian)):
			TJG = TJG + gaussian[i]
		#    print(TJG)
		TJG = Total_Entry / TJG
		#    print(TJG)
		for i in range(len(gaussian)):
			gaussian[i] = TJG * gaussian[i]
		# s2 = 50*np.sin(4*np.pi*t); #print(s2)

		str_Mean = str_Mean[:len(str_TE) + 2];  # print(str_Mean)
		str_Std = str_Std[:len(str_TE) + 2];  # print(str_Std)

		X_AXIS = []
		X_WIDTH = []
		Y_VALUE = []

		f = open(infile, 'r')
		BinN = 0
		for line in f:
			_, xaxis0, xaxis1, yaxis = line.split()
			X_AXIS.append(float(xaxis0) + (float(xaxis1) - float(xaxis0)) / 2)
			X_WIDTH.append((float(xaxis1) - float(xaxis0)))
			Y_VALUE.append(float(yaxis))
			BinN = BinN + 1

		WEIGHT = 1
		if (norm == 1):
			WEIGHT = float(Total_Entry)
			for i in range(len(gaussian)):
				gaussian[i] = gaussian[i] / Total_Entry

		for i in range(len(Y_VALUE)):
			Y_VALUE[i] = float(Y_VALUE[i]) / WEIGHT

		plt.figure(1)
		#    plt.plot(t,s2)
		plt.plot(t, gaussian)
		barlist = plt.bar(X_AXIS, Y_VALUE, X_WIDTH[0], fill=False)
		for i in range(len(barlist)):
			barlist[i].set_color('r')
		plt.axis([X_AXIS[0], X_AXIS[BinN - 1], 0, Mode[2] * 10 / 9 / WEIGHT])
		locs, labels = plt.xticks()
		TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "Mean : " + str_Mean + "\n" + "Std : " + str_Std
		plt.text(Range[1] - (Range[1] - Range[0]) * 0.05, Mode[2] * 21 / 20 / WEIGHT, TEXT, fontsize=16, ha='right',
				 va='top', rotation=0)

		one_sigma_left = "%0.3f" % (Mean - Std);
		one_sigma_left = str(one_sigma_left)
		one_sigma_right = "%0.3f" % (Mean + Std);
		one_sigma_right = str(one_sigma_right)
		two_sigma_left = "%0.3f" % (Mean - 2 * Std);
		two_sigma_left = str(two_sigma_left)
		two_sigma_right = "%0.3f" % (Mean + 2 * Std);
		two_sigma_right = str(two_sigma_right)
		plt.text(Mean - 2 * Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='g')
		plt.text(Mean - 2 * Std, 0, two_sigma_left, fontsize=7.5, ha='center', va='top', rotation=0, color='g')
		plt.text(Mean + 2 * Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='g')
		plt.text(Mean + 2 * Std, 0, two_sigma_right, fontsize=7.5, ha='center', va='top', rotation=0, color='g')
		#    plt.text(Mean,0,r"$\mu \pm 2\sigma$",fontsize=20, ha='right', va='bottom', rotation=0, color='g')

		plt.text(Mean, 0, "|", fontsize=10, ha='center', va='center', rotation=0, color='b')

		plt.text(Mean - Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean - Std, 0, one_sigma_left, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean + Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean + Std, 0, one_sigma_right, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean, 0, r"$\mu \pm \sigma$", fontsize=20, ha='center', va='bottom', rotation=0, color='black')

		plt.ylabel("Entry Number")
		if (Xaxis_Name == ''):
			XLABEL = filename_No_Txt.replace("_hist", '')
		else:
			XLABEL = Xaxis_Name
		plt.xlabel(XLABEL)
		plt.title(filename_No_Txt)
		SaveName = filename_No_Txt + "Gaussian_normalized" + ".pdf"
		plt.grid(True)
		plt.savefig(SaveName)
		plt.show()
		plt.close('all')
		f.close()
		return_list = [Mean - SIGMA * Std, Mean + SIGMA * Std]

		return return_list

	def Fit_Poisson_histo(filename, calc_file='', Xaxis_Name='', norm=1):

		if calc_file == '':
			calc_file = filename

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

		if (calc_file[0] == "/"):
			calc_file = calc_file
		elif ((calc_file[0] == "C") & (calc_file[1] == ":")):
			calc_file = calc_file
		else:
			calc_file = os.getcwd() + "/" + calc_file  # get the path included calc_file
		loca = len(calc_file)
		for i in range(1, len(calc_file) + 1):  # find the "/" location
			if (calc_file[-i] == "/"):
				loca = i - 1
				break

		FILENAME = calc_file.replace(calc_file[:-loca], "")  # this is the shorten calc_file
		calc_file_No_Txt = FILENAME.replace(".txt", "")

		infile = filename
		calc_infile = calc_file

		BIN_NUM = bin_num(infile);  # print(BIN_NUM)
		Mode = most_frequent_bin(infile);  # print(type(Mode)); print(Mode)
		Median = c1_median(calc_infile)
		Range = c1_data_range(calc_infile);  # print(Range)
		Total_Entry = c1_total_ENTRY(calc_infile);
		Total_Entry = int(Total_Entry);
		str_TE = str(Total_Entry)
		Mean = c1_mean(calc_infile);
		str_Mean = str(Mean)
		Var = c1_variance(calc_infile);
		Std = c1_standard_deviation(calc_infile);
		str_Std = str(Std)

		FROM = Range[0];
		END = Range[1];  # print(BIN_NUM, FROM, END)
		Brange = (END - FROM) / BIN_NUM;
		t = np.arange(FROM, END, Brange)
		#    gaussian = (1/(Std * np.sqrt(2 * np.pi))*np.exp(-(t-Mean)**2/(2 * Std**2)))
		tt = np.arange(0, int(END) + 1)
		Poisson = stats.poisson.pmf(tt, Mean);  # print(Poisson)
		TJG = 0
		MAX_P = 0
		for i in range(len(Poisson)):
			TJG = TJG + Poisson[i]
			if (Poisson[i] > MAX_P):
				MAX_P = Poisson[i]
		TJG = float(Mode[2]) / float(Total_Entry) / MAX_P
		#    print(TJG)
		#    TJG = Total_Entry / TJG
		#    print(TJG)

		for i in range(len(Poisson)):
			Poisson[i] = TJG * Poisson[i]
		# s2 = 50*np.sin(4*np.pi*t); #print(s2)

		str_Mean = str_Mean[:len(str_TE) + 2];  # print(str_Mean)
		str_Std = str_Std[:len(str_TE) + 2];  # print(str_Std)

		X_AXIS = []
		X_WIDTH = []
		Y_VALUE = []

		f = open(infile, 'r')
		BinN = 0
		for line in f:
			_, xaxis0, xaxis1, yaxis = line.split()
			X_AXIS.append(float(xaxis0) + (float(xaxis1) - float(xaxis0)) / 2)
			X_WIDTH.append((float(xaxis1) - float(xaxis0)))
			Y_VALUE.append(float(yaxis))
			BinN = BinN + 1

		WEIGHT = 1
		if (norm == 1):
			WEIGHT = float(Total_Entry)
		#        for i in range(len(Poisson)):
		#            Poisson[i] = Poisson[i]/Total_Entry

		for i in range(len(Y_VALUE)):
			Y_VALUE[i] = float(Y_VALUE[i]) / WEIGHT

		plt.figure(1)
		#    plt.plot(t,s2)
		plt.plot(tt, Poisson)
		barlist = plt.bar(X_AXIS, Y_VALUE, X_WIDTH[0], fill=False)
		for i in range(len(barlist)):
			barlist[i].set_color('r')
		plt.axis([X_AXIS[0], X_AXIS[BinN - 1], 0, Mode[2] * 10 / 9 / WEIGHT])
		TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "Mean : " + str_Mean + "\n" + "Std : " + str_Std
		plt.text(Range[1] - (Range[1] - Range[0]) * 0.05, Mode[2] * 21 / 20 / WEIGHT, TEXT, fontsize=16, ha='right',
				 va='top', rotation=0)
		plt.ylabel("Entry Number")
		if (Xaxis_Name == ''):
			XLABEL = filename_No_Txt.replace("_hist", '')
		else:
			XLABEL = Xaxis_Name
		plt.xlabel(XLABEL)
		plt.title(filename_No_Txt)
		SaveName = filename_No_Txt + "_Poisson_normalized" + ".pdf"
		plt.grid(True)
		plt.savefig(SaveName)
		#    plt.show()
		plt.close('all')
		f.close()

	def double_mean_Zdistribution(filename="test", sample_mean1=0, std1=1, tot1=100, sample_mean2=1, std2=2, tot2=100):
		# no return value
		MEAN = float(sample_mean1) - float(sample_mean2)
		VAR = (float(std1) * float(std1) / tot1 + float(std2) * float(std2) / tot2)
		STD = math.sqrt(VAR)

		LOWE = MEAN - 5 * STD;
		HIGHE = MEAN + 5 * STD;
		#    print(LOWE,HIGHE)
		tt = np.arange(LOWE, HIGHE, (HIGHE - LOWE) / 10000)
		gaussian = (1 / (STD * np.sqrt(2 * np.pi)) * np.exp(-(tt - MEAN) ** 2 / (2 * STD ** 2)))

		SUM = 0;
		MAX = 0;
		II = 0
		for i in range(len(gaussian)):
			SUM = SUM + gaussian[i]
			if (MAX < gaussian[i]):
				MAX = gaussian[i]
				II = i
		SUM = 1
		for i in range(len(gaussian)):
			gaussian[i] = gaussian[i] / SUM

		plt.axis([LOWE, HIGHE, 0, gaussian[II] * 5 / 4])
		TEXT = "Entry sample 1: " + str(tot1) + "\n" + "MEAN sample 1 : " + "%0.3f" % (
			sample_mean1) + "\n" + "STD sample 1 : " + "%0.3f" % (std1) + "\n" + "Entry sample 2:  " + str(
			tot2) + "\n" + "MEAN sample 2 : " + "%0.3f" % (sample_mean2) + "\n" + "STD sample 2 : " + "%0.3f" % (
				   std2) + "\n" + "Mean diff STD : " + "%0.5f" % (STD)

		one_sigma_left = "%0.3f" % (MEAN - STD);
		one_sigma_left = str(one_sigma_left)
		one_sigma_right = "%0.3f" % (MEAN + STD);
		one_sigma_right = str(one_sigma_right)
		two_sigma_left = "%0.3f" % (MEAN - 2 * STD);
		two_sigma_left = str(two_sigma_left)
		two_sigma_right = "%0.3f" % (MEAN + 2 * STD);
		two_sigma_right = str(two_sigma_right)
		plt.text(HIGHE - (HIGHE - LOWE) * 0.05, gaussian[II] * 24 / 20, TEXT, fontsize=16, ha='right', va='top',
				 rotation=0)
		plt.text(MEAN, 0, "|", fontsize=10, ha='center', va='center', rotation=0, color='b')
		plt.text(MEAN, 0, "%0.3f" % (MEAN), fontsize=10, ha='center', va='bottom', rotation=0, color='b')
		plt.text(MEAN - STD, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(MEAN - STD, 0, one_sigma_left, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(MEAN + STD, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(MEAN + STD, 0, one_sigma_right, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(MEAN - STD, 0, r"$\mu - \sigma$", fontsize=7, ha='right', va='bottom', rotation=0, color='black')
		plt.text(MEAN - 2 * STD, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='red')
		plt.text(MEAN - 2 * STD, 0, two_sigma_left, fontsize=7.5, ha='center', va='top', rotation=0, color='red')
		plt.text(MEAN + 2 * STD, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='red')
		plt.text(MEAN + 2 * STD, 0, two_sigma_right, fontsize=7.5, ha='center', va='top', rotation=0, color='red')
		plt.text(MEAN - 2 * STD, 0, r"$\mu - 2\sigma$", fontsize=13, ha='right', va='bottom', rotation=0, color='red')
		plt.text(MEAN + 2 * STD, 0, r"$\mu + 2\sigma$", fontsize=13, ha='right', va='bottom', rotation=0, color='red')

		plt.axvline(MEAN - 2 * STD)
		plt.axvline(MEAN + 2 * STD)
		plt.plot(tt, gaussian, color='r')
		plt.grid(True)
		#    plt.show()
		SaveName = filename + "_two_sample_mean.pdf"
		plt.savefig(SaveName)
		plt.close('all')

	def bothSide_hypothesis(filename, TEST_MEAN=0):
		# returns : [Zc(sigma),p value, sample_SAMPLE_MEAN, TEST_MEAN]

		# filename :: input filename
		# TEST_MEAN :: The mean value to be tested, whether it is significantly different with sample mean.

		# H0 : SAMPLE_MEAN = TEST_MEAN
		# H1 : SAMPLE_MEAN != TEST_MEAN

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

		SAMPLE_MEAN = c1_mean(infile)
		Total_Entry = c1_total_ENTRY(infile);
		Std = c1_standard_deviation(infile)

		DF = Total_Entry - 1
		INT_Confi = stats.t(df=DF).ppf((0.025, 0.975))
		INT_Confi = [SAMPLE_MEAN + INT_Confi[0] * Std / math.sqrt(Total_Entry),
					 SAMPLE_MEAN + INT_Confi[1] * Std / math.sqrt(Total_Entry)]
		print("95% confi interval", INT_Confi)

		DATA_LIST = []
		f = open(infile, 'r')
		for line in f:
			_, xaxis0, xaxis1, yaxis = line.split()
			X1 = float(xaxis0);
			X2 = float(xaxis1);
			Y = int(float(yaxis))
			if Y == 0:
				continue
			else:
				for i in range(Y):
					DATA_LIST.append(X1 + (X2 - X1) / 2)
		#    print(DATA_LIST)
		#    print(len(DATA_LIST))
		f.close()

		#    Ztest = weightstats.ztest(DATA_LIST, value=TEST_MEAN ,alternative='two-sided')
		Ttest = stats.ttest_1samp(DATA_LIST, TEST_MEAN)
		#    print(Ttest[0]); print(Ttest[1])
		List = [float("%0.6f" % (Ttest[0])), float("%0.6f" % (Ttest[1])), float("%0.6f" % (SAMPLE_MEAN)), TEST_MEAN]
		return List

	def t_distribution(filename, calc_file='', Xaxis_Name='', Show_T=True, Show_sample=True, Show_Gaus=False):
		# return [Sample_Mean-2sigma,Sample_Mean+2sigma,Total_Entry,Sample_Mean]

		if calc_file == '':
			calc_file = filename

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

		if (calc_file[0] == "/"):
			calc_file = calc_file
		elif ((calc_file[0] == "C") & (calc_file[1] == ":")):
			calc_file = calc_file
		else:
			calc_file = os.getcwd() + "/" + calc_file  # get the path included calc_file
		loca = len(calc_file)
		for i in range(1, len(calc_file) + 1):  # find the "/" location
			if (calc_file[-i] == "/"):
				loca = i - 1
				break

		FILENAME = calc_file.replace(calc_file[:-loca], "")  # this is the shorten calc_file
		calc_file_No_Txt = FILENAME.replace(".txt", "")

		infile = filename
		calc_infile = calc_file

		BIN_NUM = bin_num(infile);  # print(BIN_NUM)
		Mode = most_frequent_bin(infile);  # print(type(Mode)); print(Mode)
		Median = c1_median(calc_infile)
		Range = c1_data_range(calc_infile);  # print(Range)
		Total_Entry = c1_total_ENTRY(calc_infile);
		Total_Entry = int(Total_Entry);
		str_TE = str(Total_Entry)
		Mean = c1_mean(calc_infile);
		str_Mean = str(Mean);
		str_Mean = str_Mean[:len(str_TE) + 2];
		Var = c1_variance(calc_infile);
		Std = c1_standard_deviation(calc_infile);
		str_Std = str(Std);
		str_Std = str_Std[:len(str_TE) + 2];
		SSEM = c1_sample_standard_error_of_mean(calc_infile);
		shorten_SSEM = "%0.4f" % (SSEM)
		str_SSEM = str(shorten_SSEM)

		FROM = Range[0];
		END = Range[1];
		Brange_s = (END - FROM) / BIN_NUM;
		RANGE = END - FROM
		df = Total_Entry - 1
		x = np.arange(FROM - RANGE, END + RANGE, Brange_s / 100)
		#    x = np.linspace(t.ppf(0.0001, df),t.ppf(0.9999, df), 10000)
		#    print(t.ppf(0.0001, df)); print(t.ppf(0.9999, df))
		#    t_dist = t.pdf(Mean-x, df)
		t_dist = t.pdf((Mean - x) / Std * math.sqrt(Total_Entry), df)
		gaussian = (1 / (Std * np.sqrt(2 * np.pi)) * np.exp(-(x - Mean) ** 2 / (2 * Std ** 2)))

		MAX_T = 0
		for i in range(len(t_dist)):
			if (t_dist[i] > MAX_T):
				MAX_T = t_dist[i]
		MAX_G = 0
		for i in range(len(gaussian)):
			if (gaussian[i] >= MAX_G):
				MAX_G = gaussian[i]
		for i in range(len(gaussian)):
			gaussian[i] = gaussian[i] * MAX_T / MAX_G

		X_AXIS = []
		X_WIDTH = []
		Y_VALUE = []
		f = open(infile, 'r')
		BinN = 0
		for line in f:
			_, xaxis0, xaxis1, yaxis = line.split()
			X_AXIS.append(float(xaxis0) + (float(xaxis1) - float(xaxis0)) / 2)
			X_WIDTH.append((float(xaxis1) - float(xaxis0)))
			Y_VALUE.append(float(yaxis))
			BinN = BinN + 1

		INT_Confi = t(df=df).ppf((0.025, 0.975))
		INT_Confi = [Mean + INT_Confi[0] * Std / math.sqrt(Total_Entry),
					 Mean + INT_Confi[1] * Std / math.sqrt(Total_Entry)]
		#    print("95% confi interval",INT_Confi)

		MAX_Y = 0
		for i in range(len(Y_VALUE)):
			if (Y_VALUE[i] > MAX_Y):
				MAX_Y = Y_VALUE[i]
		for i in range(len(Y_VALUE)):
			Y_VALUE[i] = Y_VALUE[i] * MAX_T / MAX_Y

		#    XaxisL = Mean+t.ppf(0.0001, df); XaxisH = Mean+t.ppf(0.9999, df)
		#    print(t.ppf(0.0001, df),t.ppf(0.9999, df))
		#    print(XaxisL, XaxisH)
		if (Show_T == True):
			plt.plot(x, t_dist, color='b', label='T Distribution')
		TEXT = "Total Entry : " + str(
			Total_Entry) + "\n" + "POP Mean Est: " + str_Mean + "\n" + "POP Std Est: " + str_Std \
			   + "\n" + "Sample Mean STD: " + str_SSEM
		#    if(Show_Gaus==True):
		#        plt.axis([XaxisL,XaxisH,0,MAX_G*25/20])
		#        plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,MAX_G*25/20])
		#        plt.plot(x, gaussian, color='black', lw=0.5)
		#        plt.text(Range[1]-(Range[1]-Range[0])*0.05,MAX_G*24/20, TEXT, fontsize=16, ha='right', va='top', rotation=0)
		#        plt.text(XaxisH-(XaxisH-XaxisL)*0.005, MAX_G*24/20, TEXT, fontsize=16, ha='right', va='top', rotation=0)
		#        MAX = MAX_T
		#    else:
		#        plt.axis([XaxisL,XaxisH,0,MAX_T*25/20])
		plt.axis([X_AXIS[0], X_AXIS[BinN - 1], 0, MAX_T * 25 / 20])
		plt.text(Range[1] - (Range[1] - Range[0]) * 0.05, MAX_T * 24 / 20, TEXT, fontsize=16, ha='right', va='top',
				 rotation=0)
		plt.plot(x, gaussian, color='black', lw=0.5)
		#        plt.text(XaxisH-(XaxisH-XaxisL)*0.005, MAX_T*24/20, TEXT, fontsize=16, ha='right', va='top', rotation=0)
		MAX = MAX_T
		if (Show_sample == True):
			barlist = plt.bar(X_AXIS, Y_VALUE, X_WIDTH[0], fill=False)
			for i in range(len(barlist)):
				barlist[i].set_color('g')

		one_sigma_left = "%0.3f" % (Mean - Std);
		one_sigma_left = str(one_sigma_left)
		one_sigma_right = "%0.3f" % (Mean + Std);
		one_sigma_right = str(one_sigma_right)
		two_sigma_left = "%0.3f" % (Mean - 2 * Std);
		two_sigma_left = str(two_sigma_left)
		two_sigma_right = "%0.3f" % (Mean + 2 * Std);
		two_sigma_right = str(two_sigma_right)
		plt.text(Mean, 0, "|", fontsize=10, ha='center', va='center', rotation=0, color='b')
		plt.text(Mean - Std, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean - Std, 0, one_sigma_left, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean + Std, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean + Std, 0, one_sigma_right, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean - Std, 0, r"$\mu - \sigma$", fontsize=7, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean - 2 * Std, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean - 2 * Std, 0, two_sigma_left, fontsize=7.5, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean + 2 * Std, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean + 2 * Std, 0, two_sigma_right, fontsize=7.5, ha='center', va='top', rotation=0, color='black')

		sample_two_sigma_left = "%0.3f" % (INT_Confi[0]);
		sample_two_sigma_left = str(sample_two_sigma_left)
		sample_two_sigma_right = "%0.3f" % (INT_Confi[1]);
		sample_two_sigma_right = str(sample_two_sigma_right)
		plt.text(INT_Confi[0], 0, "|", fontsize=13, ha='center', va='bottom', rotation=0, color='r')
		plt.text(INT_Confi[0], MAX / 8, "$\overline{x}  - 2\sigma_x$", fontsize=18, ha='right', va='top', rotation=0,
				 color='r')
		plt.text(INT_Confi[1], 0, "|", fontsize=13, ha='center', va='bottom', rotation=0, color='r')
		plt.text(INT_Confi[1], MAX / 8, "$\overline{x}  + 2\sigma_x$", fontsize=18, ha='left', va='top', rotation=0,
				 color='r')
		plt.text(INT_Confi[0], MAX / 24, sample_two_sigma_left, fontsize=7.5, ha='right', va='bottom', rotation=0,
				 color='r')
		plt.text(INT_Confi[1], MAX / 24, sample_two_sigma_right, fontsize=7.5, ha='left', va='bottom', rotation=0,
				 color='r')

		if (Xaxis_Name == ''):
			XLABEL = filename_No_Txt.replace("_hist", '')
		else:
			XLABEL = Xaxis_Name
		SaveName = filename_No_Txt + "_T_distribution" + ".pdf"
		plt.xlabel(XLABEL)
		plt.grid(True)
		plt.savefig(SaveName)
		plt.close('all')
		f.close()
		#    plt.show()
		return [INT_Confi[0], INT_Confi[1], Total_Entry, Mean]

	def Fit_Sample_Gaus_histo(filename, calc_file='', Xaxis_Name='', SIGMA=2, exp_Mean_error=0.1, norm=0, Show=True,
							  Show_sample=True):
		# returns [Mean-n*sigma,Mean+n*sigma,Total_Entry,Expected number to reach given sigma confidence interval, SIGMA, MEAN,sample_mean_error(std) ,exp_Mean_error]  (exp_MEAN_error =  length of the half of confidence interval you want)

		# Xaxis_Name :: put what you want for Axis name
		# norm :: 0 for normalized histogram showing. (suggest do not change this value)
		# exp_Mean_error :: expected Mean error in given SIGMA level confidence interval
		# SIGMA :: pick your sigma range to be returned
		# Show :: if True, the maximum y value of canvas would be sample_mean_distribution's Maximum value
		# Show_sample :: if True, it will print the sample distribution as well

		if calc_file == '':
			calc_file = filename

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

		if (calc_file[0] == "/"):
			calc_file = calc_file
		elif ((calc_file[0] == "C") & (calc_file[1] == ":")):
			calc_file = calc_file
		else:
			calc_file = os.getcwd() + "/" + calc_file  # get the path included calc_file
		loca = len(calc_file)
		for i in range(1, len(calc_file) + 1):  # find the "/" location
			if (calc_file[-i] == "/"):
				loca = i - 1
				break

		FILENAME = calc_file.replace(calc_file[:-loca], "")  # this is the shorten calc_file
		calc_file_No_Txt = FILENAME.replace(".txt", "")

		infile = filename
		calc_infile = calc_file

		BIN_NUM = bin_num(infile);  # print(BIN_NUM)
		Mode = most_frequent_bin(infile);  # print(type(Mode)); print(Mode)
		Median = c1_median(calc_infile)
		Range = c1_data_range(calc_infile);  # print(Range)
		Total_Entry = c1_total_ENTRY(calc_infile);
		Total_Entry = int(Total_Entry);
		str_TE = str(Total_Entry)
		Mean = c1_mean(calc_infile);
		str_Mean = str(Mean)
		Var = c1_variance(calc_infile);
		Std = c1_standard_deviation(calc_infile);
		str_Std = str(Std)
		SSEM = c1_sample_standard_error_of_mean(calc_infile);
		shorten_SSEM = "%0.4f" % (SSEM)
		str_SSEM = str(shorten_SSEM)

		FROM = Range[0];
		END = Range[1];  # print(BIN_NUM, FROM, END)
		Brange = (END - FROM) / BIN_NUM;
		Brange_s = (END - FROM) / BIN_NUM * (SSEM / Std)
		RANGE = END - FROM

		t = np.arange(FROM - RANGE, END + RANGE, Brange_s)
		tt = np.arange(FROM - RANGE, END + RANGE, Brange_s)
		gaussian = (1 / (Std * np.sqrt(2 * np.pi)) * np.exp(-(t - Mean) ** 2 / (2 * Std ** 2)))
		sample_gaussian = (1 / (SSEM * np.sqrt(2 * np.pi)) * np.exp(-(tt - Mean) ** 2 / (2 * SSEM ** 2)))

		LENGTH = (Mean + 5 * SSEM) - (Mean - 5 * SSEM)
		HIGHT = 2 / LENGTH

		str_Mean = str_Mean[:len(str_TE) + 2];  # print(str_Mean)
		str_Std = str_Std[:len(str_TE) + 2];  # print(str_Std)

		X_AXIS = []
		X_WIDTH = []
		Y_VALUE = []

		f = open(infile, 'r')
		BinN = 0
		for line in f:
			_, xaxis0, xaxis1, yaxis = line.split()
			X_AXIS.append(float(xaxis0) + (float(xaxis1) - float(xaxis0)) / 2)
			X_WIDTH.append((float(xaxis1) - float(xaxis0)))
			Y_VALUE.append(float(yaxis))
			BinN = BinN + 1

		WEIGHT = 1
		WEIGHT = float(Total_Entry)
		for i in range(len(gaussian)):
			gaussian[i] = gaussian[i] / Total_Entry
		#            print("!!!",SCALE)
		#            sample_gaussian[i] = sample_gaussian[i] / SCALE
		#            print(sample_gaussian[i])
		#            print(gaussian[i])

		#    if(norm==1):
		#        for i in range(len(sample_gaussian)):
		#            SCALE = sample_gaussian[i] / gaussian[i]
		#            sample_gaussian[i] = sample_gaussian[i] / SCALE *9/10

		MAX = 0;
		MAX_S = 0
		for i in range(len(gaussian)):
			if (MAX < gaussian[i]):
				MAX = gaussian[i]

		for i in range(len(sample_gaussian)):
			if (MAX_S < sample_gaussian[i]):
				MAX_S = sample_gaussian[i]

		SCALE_SAM = HIGHT / MAX_S
		MAX_S = 0
		for i in range(len(sample_gaussian)):
			sample_gaussian[i] = sample_gaussian[i] * SCALE_SAM
			if (MAX_S < sample_gaussian[i]):
				MAX_S = sample_gaussian[i]

		MAX_Y = 0
		for i in range(len(Y_VALUE)):
			Y_VALUE[i] = float(Y_VALUE[i]) / WEIGHT
			if (MAX_Y < Y_VALUE[i]):
				MAX_Y = Y_VALUE[i]
		SCALE_Y = MAX_S / MAX_Y
		for i in range(len(Y_VALUE)):
			Y_VALUE[i] = SCALE_Y * Y_VALUE[i]

		SCALE_ALL = MAX_S / MAX
		for i in range(len(gaussian)):
			gaussian[i] = SCALE_ALL * gaussian[i]

		plt.figure(1)
		#    plt.plot(t,s2)
		plt.plot(t, gaussian)
		plt.plot(tt, sample_gaussian, color='r')
		plt.grid(True)
		plt.ylabel("Probability of Sample Mean", color='r')
		plt.yticks(color='red')
		if (Xaxis_Name == ''):
			XLABEL = filename_No_Txt.replace("_hist", '')
		else:
			XLABEL = Xaxis_Name
		plt.xlabel(XLABEL)

		#    YLIST = [0,float(int(Mode[2]/5)), float(int(Mode[2]/5*2)), float(int(Mode[2]/5*3)), float(int(Mode[2]/5*4)),  float(int(Mode[2]))]
		#    print(YLIST)
		if (Show_sample == True):
			#        plt.twinx()
			#        print(plt.yticks())
			#        plt.yticks( color="green")
			#        plt.yticks(np.arange(len(plt.yticks())),YLIST)
			barlist = plt.bar(X_AXIS, Y_VALUE, X_WIDTH[0], fill=False)
			for i in range(len(barlist)):
				barlist[i].set_color('g')
		plt.axis([X_AXIS[0], X_AXIS[BinN - 1], 0, MAX_S * 21 / 20])
		MAX = MAX_S

		'''
		if(Show == False):
			plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,Mode[2]*10/9/WEIGHT])
		else:
			plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,MAX_S])
			MAX = MAX_S
		'''

		locs, labels = plt.xticks()
		TEXT = "Total Entry : " + str(
			Total_Entry) + "\n" + "POP Mean Est: " + str_Mean + "\n" + "POP Std Est: " + str_Std \
			   + "\n" + "Sample Mean STD: " + str_SSEM
		''''
		if(Show == False): 
			plt.text(Range[1]-(Range[1]-Range[0])*0.05, Mode[2]*21/20/WEIGHT, TEXT, fontsize=16, ha='right', va='top', rotation=0)
		else:
			plt.text(Range[1]-(Range[1]-Range[0])*0.05, MAX_S*20/21, TEXT, fontsize=16, ha='right', va='top', rotation=0)
		'''
		plt.text(Range[1] - (Range[1] - Range[0]) * 0.05, MAX_S * 20 / 21, TEXT, fontsize=16, ha='right', va='top',
				 rotation=0)

		one_sigma_left = "%0.3f" % (Mean - Std);
		one_sigma_left = str(one_sigma_left)
		one_sigma_right = "%0.3f" % (Mean + Std);
		one_sigma_right = str(one_sigma_right)
		two_sigma_left = "%0.3f" % (Mean - 2 * Std);
		two_sigma_left = str(two_sigma_left)
		two_sigma_right = "%0.3f" % (Mean + 2 * Std);
		two_sigma_right = str(two_sigma_right)
		plt.text(Mean - 2 * Std, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean - 2 * Std, 0, two_sigma_left, fontsize=7.5, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean + 2 * Std, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean + 2 * Std, 0, two_sigma_right, fontsize=7.5, ha='center', va='top', rotation=0, color='black')
		#    plt.text(Mean,0,r"$\mu \pm 2\sigma$",fontsize=20, ha='right', va='bottom', rotation=0, color='black')

		plt.text(Mean, 0, "|", fontsize=10, ha='center', va='center', rotation=0, color='b')

		plt.text(Mean - Std, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean - Std, 0, one_sigma_left, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean + Std, 0, "|", fontsize=8, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean + Std, 0, one_sigma_right, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean - Std, 0, r"$\mu - \sigma$", fontsize=7, ha='right', va='bottom', rotation=0, color='black')

		sample_two_sigma_left = "%0.3f" % (Mean - 2 * SSEM);
		sample_two_sigma_left = str(sample_two_sigma_left)
		sample_two_sigma_right = "%0.3f" % (Mean + 2 * SSEM);
		sample_two_sigma_right = str(sample_two_sigma_right)
		plt.text(Mean - 2 * SSEM, 0, "|", fontsize=13, ha='center', va='bottom', rotation=0, color='r')
		plt.text(Mean - 2 * SSEM, MAX / 4, "$\overline{x}  - 2\sigma_x$", fontsize=18, ha='right', va='top', rotation=0,
				 color='r')
		plt.text(Mean + 2 * SSEM, 0, "|", fontsize=13, ha='center', va='bottom', rotation=0, color='r')
		plt.text(Mean + 2 * SSEM, MAX / 4, "$\overline{x}  + 2\sigma_x$", fontsize=18, ha='left', va='top', rotation=0,
				 color='r')
		plt.text(Mean - 2 * SSEM, MAX / 6, sample_two_sigma_left, fontsize=7.5, ha='right', va='bottom', rotation=0,
				 color='r')
		plt.text(Mean + 2 * SSEM, MAX / 6, sample_two_sigma_right, fontsize=7.5, ha='left', va='bottom', rotation=0,
				 color='r')

		plt.xlabel(XLABEL)
		plt.title(filename_No_Txt)
		SaveName = filename_No_Txt + "_Gaussian_normalized" + ".pdf"
		plt.grid(True)
		plt.savefig(SaveName)
		#    plt.show()
		plt.close('all')
		f.close()
		Ex_Num = (SIGMA * Std / exp_Mean_error) * (SIGMA * Std / exp_Mean_error)
		return_list = [float("%0.6f" % (Mean - SIGMA * SSEM)), float("%0.6f" % (Mean + SIGMA * SSEM)), Total_Entry,
					   float("%0.3f" % (Ex_Num)), str(SIGMA) + " SIGMA", float("%0.6f" % (Mean)),
					   float("%0.6f" % (SSEM)), exp_Mean_error]

		print("Careful!!!!")
		print("Event number better larger than 30 !!!!!")
		print("Current Event number is : ", Total_Entry)
		return return_list

	def double_Sample_proportion(proportion1=0.1, event_num1=100, proportion2=0.5, event_num2=100, Title='',
								 Xaxis_Name='', SIGMA=2):
		# returns [sigma, mean-2sigma, mean+2sigma]

		Mean = math.fabs(proportion1 - proportion2)
		Var = proportion1 * (1 - proportion1) / event_num1 + proportion2 * (1 - proportion2) / event_num2
		Std = math.sqrt(Var)
		t = np.arange(Mean - 4 * Std, Mean + 4 * Std, ((Mean + Std) - (Mean - Std)) / 100)
		gaussian = (1 / (Std * np.sqrt(2 * np.pi)) * np.exp(-(t - Mean) ** 2 / (2 * Std ** 2)))

		SCALE = 0
		MAX = 0
		TEST = 0
		for i in range(len(gaussian)):
			SCALE = SCALE + gaussian[i]
		for i in range(len(gaussian)):
			gaussian[i] = gaussian[i] / SCALE
			TEST = gaussian[i] + TEST
			if gaussian[i] > MAX:
				MAX = gaussian[i]
		#    print(TEST)

		plt.figure(1)
		plt.plot(t, gaussian)
		plt.axis([Mean - 5 * Std, Mean + 5 * Std, 0, MAX * 5 / 4])

		str_proportion = "%0.3f" % Mean;
		str_proportion = str(str_proportion)
		str_Std = "%0.4f" % Std;
		str_Std = str(str_Std)

		TEXT = "Sample |P1-P2| Mean : " + str_proportion + "\n" + "Sample Prop Std : " + str_Std
		plt.text((Mean + 5 * Std) * 20 / 21, MAX * 6 / 5, TEXT, fontsize=16, ha='right', va='top', rotation=0)

		one_sigma_left = "%0.3f" % (Mean - Std);
		one_sigma_left = str(one_sigma_left)
		one_sigma_right = "%0.3f" % (Mean + Std);
		one_sigma_right = str(one_sigma_right)
		two_sigma_left = "%0.3f" % (Mean - 2 * Std);
		two_sigma_left = str(two_sigma_left)
		two_sigma_right = "%0.3f" % (Mean + 2 * Std);
		two_sigma_right = str(two_sigma_right)

		plt.text(Mean - 2 * Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='g')
		plt.text(Mean - 2 * Std, 0, two_sigma_left, fontsize=7.5, ha='center', va='top', rotation=0, color='g')
		plt.text(Mean + 2 * Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='g')
		plt.text(Mean + 2 * Std, 0, two_sigma_right, fontsize=7.5, ha='center', va='top', rotation=0, color='g')
		#    plt.text(Mean,0,r"$\mu \pm 2\sigma$",fontsize=20, ha='right', va='bottom', rotation=0, color='g')

		plt.text(Mean, 0, "|", fontsize=13, ha='center', va='center', rotation=0, color='b')

		plt.text(Mean - Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean - Std, 0, one_sigma_left, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean + Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean + Std, 0, one_sigma_right, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean, 0, r"$\mu \pm \sigma$", fontsize=20, ha='center', va='bottom', rotation=0, color='black')

		plt.grid(True)
		if (Title == ''):
			TITLE = "Two Sample |P1-P2| distribution"
		else:
			TITLE = Title
		plt.title(TITLE)

		if (Xaxis_Name == ''):
			XLABEL = "Proportion"
		else:
			XLABEL = Xaxis_Name
		plt.xlabel(XLABEL)
		plt.ylabel("Probability")
		SaveName = TITLE;
		SaveName = SaveName.replace(" ", "_");
		SaveName = SaveName + ".pdf"
		#    print(SaveName)
		plt.savefig(SaveName)
		#    plt.show()
		plt.close('all')

		R_LIST = [SIGMA, Mean - SIGMA * Std, Mean + SIGMA * Std]
		return R_LIST

	def bothSide_hypothesis(proportion1=0.1, event_num1=100, proportion2=0.5, event_num2=100):
		# this is Z test for proportion test
		# returns [self calculated Zc, Zc from statsmodels, p-value from statsmodels corresponding Zc]
		# H0 : P1 = P2
		# H1 : P1 != P2
		pbar = (event_num1 * proportion1 + event_num2 * proportion2) / (event_num1 + event_num2)
		Zc = (proportion1 - proportion2) / math.sqrt(pbar * (1 - pbar) / event_num1 + pbar * (1 - pbar) / event_num2)
		Ztest = proportion.proportions_ztest([int(event_num1 * proportion1), int(event_num2 * proportion2)],
											 [event_num1, event_num2], 0)
		LIST = [Zc, Ztest[0], Ztest[1]]
		return LIST

	def Sample_proportion(proportion=0.1, event_num=100, Title='', Xaxis_Name='', SIGMA=2):

		Mean = proportion
		Var = proportion * (1 - proportion) / event_num
		Std = math.sqrt(Var)
		t = np.arange(proportion - 4 * Std, proportion + 4 * Std, ((proportion + Std) - (proportion - Std)) / 100)
		gaussian = (1 / (Std * np.sqrt(2 * np.pi)) * np.exp(-(t - proportion) ** 2 / (2 * Std ** 2)))

		SCALE = 0
		MAX = 0
		TEST = 0
		for i in range(len(gaussian)):
			SCALE = SCALE + gaussian[i]
		for i in range(len(gaussian)):
			gaussian[i] = gaussian[i] / SCALE
			TEST = gaussian[i] + TEST
			if gaussian[i] > MAX:
				MAX = gaussian[i]
		#    print(TEST)

		plt.figure(1)
		plt.plot(t, gaussian)
		plt.axis([proportion - 5 * Std, proportion + 5 * Std, 0, MAX * 5 / 4])

		str_proportion = "%0.3f" % proportion;
		str_proportion = str(str_proportion)
		str_Std = "%0.4f" % Std;
		str_Std = str(str_Std)

		TEXT = "Sample Prop Mean : " + str_proportion + "\n" + "Sample Prop Std : " + str_Std
		plt.text((proportion + 5 * Std) * 20 / 21, MAX * 6 / 5, TEXT, fontsize=16, ha='right', va='top', rotation=0)

		one_sigma_left = "%0.3f" % (Mean - Std);
		one_sigma_left = str(one_sigma_left)
		one_sigma_right = "%0.3f" % (Mean + Std);
		one_sigma_right = str(one_sigma_right)
		two_sigma_left = "%0.3f" % (Mean - 2 * Std);
		two_sigma_left = str(two_sigma_left)
		two_sigma_right = "%0.3f" % (Mean + 2 * Std);
		two_sigma_right = str(two_sigma_right)

		plt.text(Mean - 2 * Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='g')
		plt.text(Mean - 2 * Std, 0, two_sigma_left, fontsize=7.5, ha='center', va='top', rotation=0, color='g')
		plt.text(Mean + 2 * Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='g')
		plt.text(Mean + 2 * Std, 0, two_sigma_right, fontsize=7.5, ha='center', va='top', rotation=0, color='g')
		#    plt.text(Mean,0,r"$\mu \pm 2\sigma$",fontsize=20, ha='right', va='bottom', rotation=0, color='g')

		plt.text(Mean, 0, "|", fontsize=13, ha='center', va='center', rotation=0, color='b')

		plt.text(Mean - Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean - Std, 0, one_sigma_left, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean + Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean + Std, 0, one_sigma_right, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean, 0, r"$\mu \pm \sigma$", fontsize=20, ha='center', va='bottom', rotation=0, color='black')

		plt.grid(True)
		if (Title == ''):
			TITLE = "Single Sample Proportion distribution"
		else:
			TITLE = Title
		plt.title(TITLE)

		if (Xaxis_Name == ''):
			XLABEL = "Proportion"
		else:
			XLABEL = Xaxis_Name
		plt.xlabel(XLABEL)
		plt.ylabel("Probability")
		SaveName = TITLE;
		SaveName = SaveName.replace(" ", "_");
		SaveName = SaveName + ".pdf"
		#    print(SaveName)
		plt.savefig(SaveName)
		#    plt.show()
		plt.close('all')

		R_LIST = [SIGMA, Mean - SIGMA * Std, Mean + SIGMA * Std]
		return R_LIST

	def Sample_proportion(proportion=0.1, event_num=100, Title='', Xaxis_Name='', SIGMA=2, exp_Mean_error=0.001):
		# returns [Mean-n*sigma,Mean+n*sigma,Total_Entry,Expected number to reach given sigma confidence interval, SIGMA, MEAN,sample_mean_error(std) ,exp_Mean_error] (exp_MEAN_error :: [Mean-exp_MEAN_error ,Mean+exp_MEAN_error] within given sigma confidence interval)

		# Xaxis_Name :: put what you want for Axis name
		# exp_Mean_error :: expected Mean error in given SIGMA level confidence interval
		# SIGMA :: pick your sigma range to be returned :: Zc
		# Title :: Name the title of the plot

		Mean = proportion
		Var = proportion * (1 - proportion) / event_num
		Std = math.sqrt(Var)
		t = np.arange(proportion - 4 * Std, proportion + 4 * Std, ((proportion + Std) - (proportion - Std)) / 100)
		gaussian = (1 / (Std * np.sqrt(2 * np.pi)) * np.exp(-(t - proportion) ** 2 / (2 * Std ** 2)))

		SCALE = 0
		MAX = 0
		TEST = 0
		for i in range(len(gaussian)):
			SCALE = SCALE + gaussian[i]
		for i in range(len(gaussian)):
			gaussian[i] = gaussian[i] / SCALE
			TEST = gaussian[i] + TEST
			if gaussian[i] > MAX:
				MAX = gaussian[i]
		#    print(TEST)

		plt.figure(1)
		plt.plot(t, gaussian)
		plt.axis([proportion - 5 * Std, proportion + 5 * Std, 0, MAX * 5 / 4])

		str_proportion = "%0.3f" % proportion;
		str_proportion = str(str_proportion)
		str_Std = "%0.4f" % Std;
		str_Std = str(str_Std)

		TEXT = "Sample Prop Mean : " + str_proportion + "\n" + "Sample Prop Std : " + str_Std
		plt.text((proportion + 5 * Std) * 20 / 21, MAX * 6 / 5, TEXT, fontsize=16, ha='right', va='top', rotation=0)

		one_sigma_left = "%0.5f" % (Mean - Std);
		one_sigma_left = str(one_sigma_left)
		one_sigma_right = "%0.5f" % (Mean + Std);
		one_sigma_right = str(one_sigma_right)
		two_sigma_left = "%0.5f" % (Mean - 2 * Std);
		two_sigma_left = str(two_sigma_left)
		two_sigma_right = "%0.5f" % (Mean + 2 * Std);
		two_sigma_right = str(two_sigma_right)

		plt.text(Mean - 2 * Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='g')
		plt.text(Mean - 2 * Std, 0, two_sigma_left, fontsize=7.5, ha='center', va='top', rotation=0, color='g')
		plt.text(Mean + 2 * Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='g')
		plt.text(Mean + 2 * Std, 0, two_sigma_right, fontsize=7.5, ha='center', va='top', rotation=0, color='g')
		#    plt.text(Mean,0,r"$\mu \pm 2\sigma$",fontsize=20, ha='right', va='bottom', rotation=0, color='g')

		plt.text(Mean, 0, "|", fontsize=13, ha='center', va='center', rotation=0, color='b')

		plt.text(Mean - Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean - Std, 0, one_sigma_left, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean + Std, 0, "|", fontsize=24, ha='right', va='bottom', rotation=0, color='black')
		plt.text(Mean + Std, 0, one_sigma_right, fontsize=7.2, ha='center', va='top', rotation=0, color='black')
		plt.text(Mean, 0, r"$\mu \pm \sigma$", fontsize=20, ha='center', va='bottom', rotation=0, color='black')

		plt.grid(True)
		if (Title == ''):
			TITLE = "Single Sample Proportion distribution"
		else:
			TITLE = Title
		plt.title(TITLE)

		if (Xaxis_Name == ''):
			XLABEL = "Proportion"
		else:
			XLABEL = Xaxis_Name
		plt.xlabel(XLABEL)
		plt.ylabel("Probability")
		SaveName = TITLE;
		SaveName = SaveName.replace(" ", "_");
		SaveName = SaveName + ".pdf"
		#    print(SaveName)
		plt.savefig(SaveName)
		#    plt.show()
		plt.close('all')

		Ex_Num = (SIGMA * math.sqrt(proportion * (1 - proportion)) / exp_Mean_error) * (
					SIGMA * math.sqrt(proportion * (1 - proportion)) / exp_Mean_error)

		#    print(Ex_Num)
		R_LIST = [float("%0.6f" % (Mean - SIGMA * Std)), float("%0.6f" % (Mean + SIGMA * Std)), event_num,
				  float("%0.3f" % (Ex_Num)), str(SIGMA) + " SIGMA", float("%0.6f" % (Mean)), float("%0.6f" % (Std)),
				  exp_Mean_error]
		return R_LIST

	def bothSide_hypothesis(Proportion=0.1, event_num=100, test_proportion=0.1):
		# this is Z test for proportion test
		# returns [self calculated Zc, Zc from statsmodels, p-value from statsmodels corresponding Zc, Sample_proportion, Test_proportion]
		# H0 : P1 = Test_proportion
		# H1 : P1 != Test_proportion

		Prop = Proportion

		Event_num = float(event_num)
		Std = math.sqrt(Prop * (1 - Prop) / Event_num)
		Zc = (Prop - test_proportion) / math.sqrt(Prop * (1 - Prop) / Event_num)

		Success = event_num * Prop;
		Success = int(Success);  # print(type(Success)); print(Success)
		Ztest = proportion.proportions_ztest(int(Success), int(event_num), value=test_proportion,
											 alternative='two-sided')
		#    Ztest = proportion.proportions_ztest(10,100,0.09)
		LIST = [Zc, Ztest[0], Ztest[1], Prop, test_proportion]
		return LIST

	def double_Sample_Variance(outputname="test", VAR1=1, tot1=100, VAR2=0.5, tot2=100):
		# no return value
		F = VAR1 / VAR2
		df1 = tot1 - 1;
		df2 = tot2 - 1;
		x = np.linspace(F_TEST.ppf(0.0001, df1, df2), F_TEST.ppf(0.9999, df1, df2), 10000)
		str_tot1 = str(tot1)
		str_tot2 = str(tot2)
		MAX = 0
		for aa in F_TEST.pdf(x, df1, df2):
			if (MAX < aa):
				MAX = aa

		plt.plot(x, F_TEST.pdf(x, df1, df2), 'r')
		plt.axis([F_TEST.ppf(0.0001, df1, df2), F_TEST.ppf(0.9999, df1, df2), 0, MAX * 5 / 4])
		TEXT = "Sample 1 Entry : " + str_tot1 + "\n" + "Sample 1 VAR : " + "%0.3f" % (
			VAR1) + "\n" + "Sample 2 Entry : " + str_tot2 + "\n" + "Sample 2 VAR : " + "%0.3f" % (VAR2)
		plt.text(F_TEST.ppf(0.9999, df1, df2) - (F_TEST.ppf(0.9999, df1, df2) - F_TEST.ppf(0.0001, df1, df2)) * 0.05,
				 MAX * 23 / 20, TEXT, fontsize=16, ha='right', va='top', rotation=0)

		p025 = "%0.3f" % (F_TEST.ppf(0.025, df1, df2));
		p025 = str(p025)
		p975 = "%0.3f" % (F_TEST.ppf(0.975, df1, df2));
		p975 = str(p975)
		plt.axvline(p025);
		plt.axvline(p975)
		plt.text(F_TEST.ppf(0.025, df1, df2), 0, p025, fontsize=14, ha='left', va='bottom', rotation=0, color='r')
		plt.text(F_TEST.ppf(0.975, df1, df2), 0, p975, fontsize=14, ha='right', va='bottom', rotation=0, color='r')
		plt.text(F_TEST.ppf(0.025, df1, df2), 0, "P975", fontsize=7, ha='right', va='top', rotation=0, color='green')
		plt.text(F_TEST.ppf(0.975, df1, df2), 0, "P025", fontsize=7, ha='left', va='top', rotation=0, color='green')

		plt.grid(True)
		#    plt.show()
		SaveName = outputname + "2sample_VAR_F_dist.pdf"
		plt.savefig(SaveName)
		plt.close('all')

	def Variance_both_side(VAR1=1, tot1=100, VAR2=0.5, tot2=100, alpha=0.05):
		# return [alpha, p_value, variance of sample1, Event number of sample1, variance of sample2, Event number of sample2]
		# H0 : sigma1 = sigma2
		# H1 : sigma1 != sigma2
		F = VAR1 / VAR2;  # print(F)
		df1 = tot1 - 1;
		df2 = tot2 - 1;
		p_value = F_TEST.cdf(F, df1, df2)
		if (p_value > 0.500):
			p_value = 1 - p_value

		p025 = F_TEST.ppf(0.025, df1, df2)
		p975 = F_TEST.ppf(0.975, df1, df2)
		# print(p025, p975)
		return [alpha, p_value, VAR1, tot1, VAR2, tot2]
	# p_value < alpha --> Reject the null hypothesis that Var(X) == Var(Y)

	def Sample_Variance(filename, calc_file='', ALPHA=0.05):
		# return value : [Lower_chi2 on given ALPHA, Higher_chi2 on given ALPHA, Lower_Sigma2 on given ALPHA, Higher_Sigma2 on given ALPHA, Total_Entry, ALPHA, Mean, Variance]

		if calc_file == '':
			calc_file = filename

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

		if (calc_file[0] == "/"):
			calc_file = calc_file
		elif ((calc_file[0] == "C") & (calc_file[1] == ":")):
			calc_file = calc_file
		else:
			calc_file = os.getcwd() + "/" + calc_file  # get the path included calc_file
		loca = len(calc_file)
		for i in range(1, len(calc_file) + 1):  # find the "/" location
			if (calc_file[-i] == "/"):
				loca = i - 1
				break

		FILENAME = calc_file.replace(calc_file[:-loca], "")  # this is the shorten calc_file
		calc_file_No_Txt = FILENAME.replace(".txt", "")

		infile = filename
		calc_infile = calc_file

		BIN_NUM = bin_num(infile);  # print(BIN_NUM)
		Mode = most_frequent_bin(infile);  # print(type(Mode)); print(Mode)
		Median = c1_median(calc_infile)
		Range = c1_data_range(calc_infile);  # print(Range)
		Total_Entry = c1_total_ENTRY(calc_infile);
		Total_Entry = int(Total_Entry);
		str_TE = str(Total_Entry)
		Mean = c1_mean(calc_infile);
		str_Mean = "%0.3f" % (Mean);
		str_Mean = str(str_Mean)
		Var = c1_variance(calc_infile);
		Std = c1_standard_deviation(calc_infile);
		str_Std = "%0.3f" % (Std);
		str_Std = str(str_Std)
		#    Var = 0.5325
		str_Var = "%0.3f" % (Var);
		str_Var = str(str_Var)

		df = Total_Entry - 1
		#    df = 8
		x = np.linspace(chi2.ppf(0.000001, df), chi2.ppf(0.999999, df), 10000)
		xs = np.linspace(df * Var / chi2.ppf(0.999999, df), df * Var / chi2.ppf(0.000001, df), 10000)
		#    print(xs)
		MAX_CHI2 = 0
		TEST_LIST = chi2.pdf(x, df)
		for i in range(len(TEST_LIST)):
			if (MAX_CHI2 < TEST_LIST[i]):
				MAX_CHI2 = TEST_LIST[i]

		plt.axis([chi2.ppf(0.000001, df), chi2.ppf(0.999999, df), 0, MAX_CHI2 * 24 / 20])
		plt.plot(x, chi2.pdf(x, df), 'r-', lw=1, alpha=0.6, label='chi2 pdf')
		plt.grid(True)
		plt.title(filename_No_Txt)
		plt.xlabel("$\chi^2$")
		TEXT = "Total Entry : " + str(
			Total_Entry) + "\n" + "POP Var Est : " + str_Var + "\n" + "POP STD Est : " + str_Std + "\n POP Mean Est : " + str_Mean
		plt.text((chi2.ppf(0.999999, df) - (chi2.ppf(0.999999, df) - chi2.ppf(0.000001, df)) * 0.05),
				 MAX_CHI2 * 23 / 20, TEXT, fontsize=16, ha='right', va='top', rotation=0)
		p05 = "%0.3f" % (chi2.ppf(0.05, df));
		p05 = str(p05)
		p025 = "%0.3f" % (chi2.ppf(0.025, df));
		p025 = str(p025)
		p95 = "%0.3f" % (chi2.ppf(0.95, df));
		p95 = str(p95)
		p975 = "%0.3f" % (chi2.ppf(0.975, df));
		p975 = str(p975)
		p025s = "%0.3f" % ((df * Var) / chi2.ppf(0.975, df));
		p025s = str(p025s)
		p975s = "%0.3f" % ((df * Var) / chi2.ppf(0.025, df));
		p975s = str(p975s)
		p025ss = "%0.3f" % (math.sqrt((df * Var) / chi2.ppf(0.975, df)));
		p025ss = str(p025ss)
		p975ss = "%0.3f" % (math.sqrt((df * Var) / chi2.ppf(0.025, df)));
		p975ss = str(p975ss)
		plt.text(chi2.ppf(0.05, df), 0, "|", fontsize=6, ha='center', va='center', rotation=0, color='g')
		plt.text(chi2.ppf(0.05, df), 0, p05, fontsize=7, ha='center', va='top', rotation=0, color='g')
		plt.text(chi2.ppf(0.025, df), 0, "|", fontsize=6, ha='center', va='center', rotation=0, color='r')
		plt.text(chi2.ppf(0.025, df), 0, p025, fontsize=7, ha='center', va='bottom', rotation=0, color='r')
		plt.text(chi2.ppf(0.025, df), MAX_CHI2 / 6, p025s, fontsize=14, ha='center', va='bottom', rotation=0, color='b')
		plt.text(chi2.ppf(0.95, df), 0, "|", fontsize=6, ha='center', va='center', rotation=0, color='g')
		plt.text(chi2.ppf(0.95, df), 0, p95, fontsize=7, ha='center', va='top', rotation=0, color='g')
		plt.text(chi2.ppf(0.975, df), 0, "|", fontsize=6, ha='center', va='center', rotation=0, color='r')
		plt.text(chi2.ppf(0.975, df), 0, p975, fontsize=7, ha='center', va='bottom', rotation=0, color='r')
		plt.text(chi2.ppf(0.975, df), MAX_CHI2 / 6, p975s, fontsize=14, ha='center', va='bottom', rotation=0, color='b')
		plt.text(chi2.ppf(0.025, df), MAX_CHI2 / 8, "|", fontsize=14, ha='center', va='bottom', rotation=0, color='b')
		plt.text(chi2.ppf(0.975, df), MAX_CHI2 / 8, "|", fontsize=14, ha='center', va='bottom', rotation=0, color='b')
		plt.text(chi2.ppf(0.025, df) + (chi2.ppf(0.975, df) - chi2.ppf(0.025, df)) / 2, MAX_CHI2 / 8,
				 "<-- $\sigma^2$ -->", fontsize=14, ha='center', va='bottom', rotation=0, color='b')
		#    plt.show()
		SaveName = filename_No_Txt + "_Variance" + ".pdf"
		plt.savefig(SaveName)
		plt.close('all')

		MAX_STD = 0
		TEST_LIST = 1 / chi2.pdf(x, df)
		XS_MIN = xs[0];
		XS_MAX = xs[len(xs) - 1]
		for i in range(len(xs)):
			if (MAX_STD < TEST_LIST[i]):
				MAX_STD = TEST_LIST[i]

		LOW_chi2 = chi2.ppf(ALPHA / 2, df);
		HIGH_chi2 = chi2.ppf(1 - ALPHA / 2, df)
		#    print(LOW_chi2, HIGH_chi2)
		LOW_sigma = (df * Var) / chi2.ppf(1 - ALPHA / 2, df);
		HIGH_sigma = (df * Var) / chi2.ppf(ALPHA / 2, df)
		#    print(LOW_sigma,HIGH_sigma)

		plt.axis([(df * Var) / chi2.ppf(0.999, df), (df * Var) / chi2.ppf(0.001, df), 0, MAX_STD * 24 / 20])
		plt.plot(xs, 1 / chi2.pdf(x, df), 'r-', lw=1, alpha=0.6, label='chi2 pdf')
		plt.grid(True)
		plt.xlabel("$\sigma^2$")
		TEXT = "Total Entry : " + str(
			Total_Entry) + "\n" + "POP Var Est : " + str_Var + "\n" + "POP STD Est: " + str_Std
		plt.text(
			(df * Var) / chi2.ppf(0.999, df) + ((df * Var) / chi2.ppf(0.001, df) - (df * Var) / chi2.ppf(0.999, df)),
			MAX_STD * 23 / 20, TEXT, fontsize=16, ha='right', va='top', rotation=0)
		p05 = "%0.3f" % ((df * Var) / chi2.ppf(0.95, df));
		p05 = str(p05)
		p025 = "%0.3f" % ((df * Var) / chi2.ppf(0.975, df));
		p025 = str(p025)
		p95 = "%0.3f" % ((df * Var) / chi2.ppf(0.05, df));
		p95 = str(p95)
		p975 = "%0.3f" % ((df * Var) / chi2.ppf(0.025, df));
		p975 = str(p975)
		plt.text((df * Var) / chi2.ppf(0.95, df), 0, "|", fontsize=6, ha='center', va='center', rotation=0, color='g')
		plt.text((df * Var) / chi2.ppf(0.95, df), 0, p05, fontsize=7, ha='center', va='top', rotation=0, color='g')
		plt.text((df * Var) / chi2.ppf(0.975, df), 0, "|", fontsize=6, ha='center', va='center', rotation=0, color='r')
		plt.text((df * Var) / chi2.ppf(0.975, df), 0, p025, fontsize=7, ha='center', va='bottom', rotation=0, color='r')
		plt.text((df * Var) / chi2.ppf(0.05, df), 0, "|", fontsize=6, ha='center', va='center', rotation=0, color='g')
		plt.text((df * Var) / chi2.ppf(0.05, df), 0, p95, fontsize=7, ha='center', va='top', rotation=0, color='g')
		plt.text((df * Var) / chi2.ppf(0.025, df), 0, "|", fontsize=6, ha='center', va='center', rotation=0, color='r')
		plt.text((df * Var) / chi2.ppf(0.025, df), 0, p975, fontsize=7, ha='center', va='bottom', rotation=0, color='r')

		#    plt.show()
		plt.savefig("test2.pdf")
		plt.close('all')

		#    if(Var - exp_Var < 0):
		#        Ex_num = 1+(exp_Var)*chi2.ppf(ALPHA/2,df)/Var
		#    elif(Var - exp_Var>0):
		#        Ex_num = 1+(Var-exp_Var)*(Var-exp_Var)*chi2.ppf(ALPHA/2,df)/Var+1
		#    print(Ex_num)
		#    print(chi2.ppf(ALPHA/2,df))
		#    print(chi2.ppf(1-ALPHA/2,df))

		RETURN_LIST = [float("%0.6f" % (LOW_chi2)), float("%0.6f" % (HIGH_chi2)), float("%0.6f" % (LOW_sigma)),
					   float("%0.6f" % (HIGH_sigma)), Total_Entry, "alpha = " + str(ALPHA), float("%0.6f" % (Mean)),
					   float("%0.6f" % (Var))]
		return RETURN_LIST

	def Sample_Variance_both_side(filename, ALPHA=0.05, test_VAR=10):
		# returns [Low_chi2,High_chi2,test_chi2,Low_sigma2,High_sigma2,test_sigma2(test_VAR),ALPHA, Var ,p-value]
		#             0       1         2          3          4           5                   6     7      8
		# H0 : Var = test_VAR
		# H1 : Var != test_VAR

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

		BIN_NUM = bin_num(infile);  # print(BIN_NUM)
		Mode = most_frequent_bin(infile);  # print(type(Mode)); print(Mode)
		Median = c1_median(infile)
		Range = c1_data_range(infile);  # print(Range)
		Total_Entry = c1_total_ENTRY(infile);
		Total_Entry = int(Total_Entry);
		str_TE = str(Total_Entry)
		Mean = c1_mean(infile);
		str_Mean = "%0.3f" % (Mean);
		str_Mean = str(str_Mean)
		Var = c1_variance(infile);
		Std = c1_standard_deviation(infile);
		str_Std = "%0.3f" % (Std);
		str_Std = str(str_Std)
		#    Var = 0.5325
		str_Var = "%0.3f" % (Var);
		str_Var = str(str_Var)
		df = Total_Entry - 1

		LOW_chi2 = chi2.ppf(ALPHA / 2, df);
		HIGH_chi2 = chi2.ppf(1 - ALPHA / 2, df)
		LOW_sigma = (df * Var) / chi2.ppf(1 - ALPHA / 2, df);
		HIGH_sigma = (df * Var) / chi2.ppf(ALPHA / 2, df)
		test_Chi2 = df * Var / test_VAR
		#    if((test_VAR>=LOW_sigma)&(test_VAR<=HIGH_sigma)):
		#        deter = "ACCEPT H0, VAR = test_VAR"
		#    else:
		#        deter = "REJECT H0, VAR!=test_VAR"

		pValue = -100
		if (test_Chi2 <= chi2.ppf(0.5, df)):
			pValue = 2 * chi2.cdf(test_Chi2, df)
		elif (test_Chi2 >= chi2.ppf(0.5, df)):
			pValue = 2 * (1 - chi2.cdf(test_Chi2, df))  # alpla'/2 * 2 to get pValue

		R_LIST = [float("%0.6f" % (LOW_chi2)), float("%0.6f" % (HIGH_chi2)), float("%0.6f" % (test_Chi2)),
				  float("%0.6f" % (LOW_sigma)), float("%0.6f" % (HIGH_sigma)), float("%0.6f" % (test_VAR)),
				  "ALPHA = " + str(ALPHA), float("%0.6f" % (Var)), float("%0.6f" % (pValue))]
		return R_LIST

	#    ...This is Anova's oneway, Compeletly Randomized designed, same event number for each process...
	#    ...The Null hypo is 'mu0 == mu1 == .. == muN' ...
	#    ...The alternative is 'at least one of the mean value of the sample is differ with others' ...

	#  sample_1  ...    sample_l
	#     A1  A2  A3 .... Al    SUM  AVERAGE
	# B1  x11 x21 x31 ... xl1   Tl1   xl1_bar
	# B2  x12 x22 x32 ... xl2   Tl2   xl2_bar
	# .   ..  ..  ..  ... ...   ...    ...
	# Bm  x1m x2m x3m ... xlm   Tlm   xlm_bar
	# SUM  T1  T2  T3  ...  Tl    T
	# AVE x1_bar .. .. .. xl_bar       x_bar_bar

	# recommand to use "*largeBin.txt"
	def Anova_oneway_Random_sameE(filelist=[], alpha=0.05):
		# return [alpha, p_value, LEVEL(kinds of samples tested), Sample's Event NUMBER for each sample, block_number]

		# ENTRY is total block number, M, for this case
		if (len(filelist) <= 2):
			print("...File number is lower than 2, recheck or try with Ztest/Ttest...")
			return 0

		FILENAME = []
		filename_No_Txt = []
		for j in range(len(filelist)):
			if (filelist[j][0] == "/"):
				filelist[j] = filelist[j]
			else:
				filelist[j] = os.getcwd() + "/" + filelist[j]  # get the path included filename
			loca = len(filelist[j])
			for i in range(1, len(filelist[j]) + 1):  # find the "/" location
				if (filelist[j][-i] == "/"):
					loca = i - 1
					break
			FILENAME.append(filelist[j].replace(filelist[j][:-loca], ""))  # this is the shorten filename
			filename_No_Txt.append(FILENAME[j].replace(".txt", ""))

		ENTRY = c1_total_ENTRY(filelist[0]);  ## M == ENTRY
		for i in range(len(filelist)):
			if (int(c1_total_ENTRY(filelist[i])) != ENTRY):
				print("...ERROR, sample size different between samples ...")
				return 0
		block_num = ENTRY

		NUM = len(filelist) * block_num;
		Tot_sample = []
		Tot_sum = 0
		for i in range(len(filelist)):
			Tot_sample.append(c1_mean(filelist[i]) * c1_total_ENTRY(filelist[i]))
			Tot_sum = Tot_sum + c1_mean(filelist[i]) * c1_total_ENTRY(filelist[i])
		CT = Tot_sum * Tot_sum / NUM;

		Square_sum = 0
		for i in range(len(filelist)):
			Square_sum = Square_sum + c1_square_sum(filelist[i])
		SST = Square_sum - CT;  # print(SST)
		sum_of_T_square = 0  # this is "sum_of_T_A_square"
		for i in range(len(Tot_sample)):
			sum_of_T_square = sum_of_T_square + Tot_sample[i] * Tot_sample[i]
		SSB = sum_of_T_square / block_num - CT;  # print(SSB)
		SSW = SST - SSB

		MSB = SSB / (len(filelist) - 1);  # print(MSB)
		MSW = SSW / (len(filelist) * (block_num - 1));  # print(MSW)
		dfB = len(filelist) - 1
		dfW = len(filelist) * (block_num - 1)
		F_Ratio = MSB / MSW;  # print(F_Ratio)

		print("There are totaly", len(filename_No_Txt), "levels")
		for i in range(len(filename_No_Txt)):
			print("Level : ", filename_No_Txt[i])
		print("Sample number : ", ENTRY)
		print("Block number : ", block_num)

		p_value = F_TEST.cdf(F_Ratio, dfB, dfW);  # print(p_value)
		p_value = 1 - p_value
		return [alpha, p_value, len(filelist), ENTRY, block_num]

	# "p_value < alpha" means: reject H0, accept alternative H1
	# https://stackoverflow.com/questions/21494141/how-do-i-do-a-f-test-in-python

	def Anova_twoWay_Randomized_Block(filelist=[], block_num='', alpha=0.05):
		#   A1 A2 A3 ... (level, one sample for a column Ai)
		# B1
		# B2
		# .
		# .
		# (Block)

		if (len(filelist) <= 2):
			print("...File number is lower than 2, recheck or try with Ztest/Ttest...")
			return 0
		FILENAME = []
		filename_No_Txt = []
		for j in range(len(filelist)):
			if (filelist[j][0] == "/"):
				filelist[j] = filelist[j]
			else:
				filelist[j] = os.getcwd() + "/" + filelist[j]  # get the path included filename
			loca = len(filelist[j])
			for i in range(1, len(filelist[j]) + 1):  # find the "/" location
				if (filelist[j][-i] == "/"):
					loca = i - 1
					break
			FILENAME.append(filelist[j].replace(filelist[j][:-loca], ""))  # this is the shorten filename
			filename_No_Txt.append(FILENAME[j].replace(".txt", ""))

		ENTRY = c1_total_ENTRY(filelist[0])
		for i in range(len(filelist)):
			if (int(c1_total_ENTRY(filelist[i])) != ENTRY):
				print("...ERROR, sample size different between samples ...")
				return 0
		if (block_num == ''):
			block_num = ENTRY
		BL = c1_data_range(filelist[0])[0]
		BH = c1_data_range(filelist[0])[1]
		for i in range(len(filelist)):
			if (c1_data_range(filelist[i])[0]) < BL:
				BL = (c1_data_range(filelist[i])[0])
			if (c1_data_range(filelist[i])[1]) > BH:
				BH = (c1_data_range(filelist[i])[1])
		#    print(BL,BH)

		NUM = len(filelist) * block_num;
		Tot_sample = []
		Tot_sum = 0
		for i in range(len(filelist)):
			Tot_sample.append(c1_mean(filelist[i]) * c1_total_ENTRY(filelist[i]))
			Tot_sum = Tot_sum + c1_mean(filelist[i]) * c1_total_ENTRY(filelist[i])
		CT = Tot_sum * Tot_sum / NUM;
		Square_sum = 0
		for i in range(len(filelist)):
			Square_sum = Square_sum + c1_square_sum(filelist[i])
		SST = Square_sum - CT;  # print(SST)
		sum_of_T_A_square = 0
		for i in range(len(Tot_sample)):
			sum_of_T_A_square = sum_of_T_A_square + Tot_sample[i] * Tot_sample[i]


#    SSB = sum_of_T_A_square/block_num - CT;


# SSAB


if __name__ == '__main__':
    inst = func_frame()
    inst.help()

'''
from func_frame import func_frame as dd

x = dd()
dd.help()

x.help()
dd.help()
'''