#Author : JUNHO LEE
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import sys,os
from scipy import stats
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *


def Fit_Poisson_histo(filename,calc_file='', Xaxis_Name='', norm=1):

    if calc_file =='':
        calc_file = filename

    if(filename[0]=="/"):
        filename = filename
    elif((filename[0]=="C")&(filename[1]==":")):
        filename = filename
    else:
        filename = os.getcwd() + "/" + filename   # get the path included filename
    loca=len(filename)
    for i in range (1,len(filename)+1):       # find the "/" location
        if(filename[-i] == "/"):
            loca = i-1
            break

    FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten filename
    filename_No_Txt = FILENAME.replace(".txt","")

    if(calc_file[0]=="/"):
        calc_file = calc_file
    elif((calc_file[0]=="C")&(calc_file[1]==":")):
        calc_file = calc_file
    else:
        calc_file = os.getcwd() + "/" + calc_file   # get the path included calc_file
    loca=len(calc_file)
    for i in range (1,len(calc_file)+1):       # find the "/" location
        if(calc_file[-i] == "/"):
            loca = i-1
            break

    FILENAME = calc_file.replace(calc_file[:-loca],"")   # this is the shorten calc_file
    calc_file_No_Txt = FILENAME.replace(".txt","")


    infile = filename
    calc_infile = calc_file

    BIN_NUM = bin_num(infile);        #print(BIN_NUM)
    Mode = most_frequent_bin(infile); #print(type(Mode)); print(Mode)
    Median = c1_median(calc_infile)
    Range = c1_data_range(calc_infile);    #print(Range)
    Total_Entry = c1_total_ENTRY(calc_infile); Total_Entry = int(Total_Entry); str_TE = str(Total_Entry)
    Mean = c1_mean(calc_infile);  str_Mean = str(Mean)
    Var = c1_variance(calc_infile);
    Std = c1_standard_deviation(calc_infile); str_Std = str(Std)

    FROM = Range[0]; END = Range[1];  #print(BIN_NUM, FROM, END)
    Brange = (END-FROM)/BIN_NUM; 
    t = np.arange(FROM, END, Brange) 
#    gaussian = (1/(Std * np.sqrt(2 * np.pi))*np.exp(-(t-Mean)**2/(2 * Std**2)))
    tt = np.arange(0, int(END)+1)
    Poisson = stats.poisson.pmf(tt, Mean); #print(Poisson)
    TJG=0
    MAX_P=0
    for i in range(len(Poisson)):
        TJG = TJG + Poisson[i]
        if(Poisson[i]>MAX_P):
            MAX_P = Poisson[i]
    TJG = float(Mode[2])/float(Total_Entry) / MAX_P
#    print(TJG)
#    TJG = Total_Entry / TJG 
#    print(TJG)

    for i in range(len(Poisson)):
        Poisson[i] = TJG * Poisson[i]
    #s2 = 50*np.sin(4*np.pi*t); #print(s2)

    str_Mean = str_Mean[:len(str_TE)+2]; #print(str_Mean)    
    str_Std = str_Std[:len(str_TE)+2]; #print(str_Std)

    X_AXIS = []
    X_WIDTH = []
    Y_VALUE = []

    f = open(infile,'r')
    BinN = 0
    for line in f:
        _,xaxis0,xaxis1, yaxis = line.split()
        X_AXIS.append(float(xaxis0) + (float(xaxis1)-float(xaxis0))/2)
        X_WIDTH.append((float(xaxis1)-float(xaxis0)))
        Y_VALUE.append(float(yaxis))
        BinN = BinN + 1
    
    WEIGHT = 1
    if(norm==1):
        WEIGHT = float(Total_Entry)
#        for i in range(len(Poisson)):
#            Poisson[i] = Poisson[i]/Total_Entry

    for i in range(len(Y_VALUE)):
        Y_VALUE[i] = float(Y_VALUE[i])/WEIGHT


    plt.figure(1)
#    plt.plot(t,s2)
    plt.plot(tt,Poisson)
    barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0],fill=False)
    for i in range(len(barlist)):
        barlist[i].set_color('r')
    plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,Mode[2]*10/9/WEIGHT])
    TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "Mean : " + str_Mean + "\n" + "Std : " + str_Std
    plt.text(Range[1]-(Range[1]-Range[0])*0.05, Mode[2]*21/20/WEIGHT, TEXT, fontsize=16, ha='right', va='top', rotation=0)
    plt.ylabel("Entry Number")
    if(Xaxis_Name == ''):
        XLABEL = filename_No_Txt.replace("_hist",'')
    else:
        XLABEL = Xaxis_Name
    plt.xlabel(XLABEL)
    plt.title(filename_No_Txt)
    SaveName = filename_No_Txt +"_Poisson_normalized"+ ".pdf"
    plt.grid(True)
    plt.savefig(SaveName)
#    plt.show()
    plt.close('all')
    f.close()



def main():
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/EXE/beer_0319Mon_LA_s_tree_beer_0319Mon_LA_s_V1_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/EXE/beer_0319Mon_LA_s_tree_beer_0319Mon_LA_s_V2_hist.txt"
#    inputfile = "gaus100.txt"
    inputfile= "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_day_tree_cut_Aqi_Beijing_day_f_SO2_hist.txt"

#    Fit_Poisson_histo(inputfile, ".X-axis.", norm=0)
    Fit_Poisson_histo(inputfile, ".X-axis.", norm=1)

if __name__ == "__main__":
    main()

