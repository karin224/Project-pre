#Author : JUNHO LEE
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import sys,os
import math
from scipy.stats import t
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import * 

#### The sample should be extracted from Gaussian distribution of Population 
#### In the case n<=30
def t_distribution(filename,calc_file='',Xaxis_Name='', Show_T=True, Show_sample=True, Show_Gaus=False):
    #return [Sample_Mean-2sigma,Sample_Mean+2sigma,Total_Entry,Sample_Mean]

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
    Mean = c1_mean(calc_infile);  str_Mean = str(Mean); str_Mean = str_Mean[:len(str_TE)+2];
    Var = c1_variance(calc_infile);
    Std = c1_standard_deviation(calc_infile); str_Std = str(Std); str_Std = str_Std[:len(str_TE)+2];
    SSEM = c1_sample_standard_error_of_mean(calc_infile);
    shorten_SSEM = "%0.4f"%(SSEM)
    str_SSEM = str(shorten_SSEM)

    FROM = Range[0]; END = Range[1];
    Brange_s = (END-FROM)/BIN_NUM;
    RANGE = END-FROM
    df = Total_Entry-1
    x = np.arange(FROM-RANGE, END+RANGE, Brange_s/100)
#    x = np.linspace(t.ppf(0.0001, df),t.ppf(0.9999, df), 10000)
#    print(t.ppf(0.0001, df)); print(t.ppf(0.9999, df))
#    t_dist = t.pdf(Mean-x, df)
    t_dist = t.pdf((Mean-x)/Std*math.sqrt(Total_Entry), df)
    gaussian = (1/(Std * np.sqrt(2 * np.pi))*np.exp(-(x-Mean)**2/(2 * Std**2)))

    MAX_T=0
    for i in range(len(t_dist)):
        if(t_dist[i]>MAX_T):
            MAX_T = t_dist[i]
    MAX_G=0
    for i in range(len(gaussian)):
        if(gaussian[i]>=MAX_G):
            MAX_G = gaussian[i]
    for i in range(len(gaussian)):
        gaussian[i] = gaussian[i] * MAX_T/MAX_G

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

    INT_Confi = t(df=df).ppf((0.025,0.975))
    INT_Confi = [Mean+INT_Confi[0]*Std/math.sqrt(Total_Entry),Mean+INT_Confi[1]*Std/math.sqrt(Total_Entry)] 
#    print("95% confi interval",INT_Confi)

    MAX_Y=0
    for i in range(len(Y_VALUE)):
        if(Y_VALUE[i]>MAX_Y):
            MAX_Y=Y_VALUE[i]
    for i in range(len(Y_VALUE)):
        Y_VALUE[i] = Y_VALUE[i]*MAX_T/MAX_Y

#    XaxisL = Mean+t.ppf(0.0001, df); XaxisH = Mean+t.ppf(0.9999, df)
#    print(t.ppf(0.0001, df),t.ppf(0.9999, df))
#    print(XaxisL, XaxisH)
    if(Show_T==True):
        plt.plot(x, t_dist ,color='b', label='T Distribution')
    TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "POP Mean Est: " + str_Mean + "\n" + "POP Std Est: " + str_Std \
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
    plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,MAX_T*25/20])
    plt.text(Range[1]-(Range[1]-Range[0])*0.05,MAX_T*24/20, TEXT, fontsize=16, ha='right', va='top', rotation=0)
    plt.plot(x, gaussian, color='black', lw=0.5)
#        plt.text(XaxisH-(XaxisH-XaxisL)*0.005, MAX_T*24/20, TEXT, fontsize=16, ha='right', va='top', rotation=0)
    MAX = MAX_T
    if(Show_sample==True):
        barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0],fill=False)
        for i in range(len(barlist)):
            barlist[i].set_color('g')   

    one_sigma_left = "%0.3f"%(Mean-Std); one_sigma_left = str(one_sigma_left)
    one_sigma_right = "%0.3f"%(Mean+Std); one_sigma_right = str(one_sigma_right)
    two_sigma_left = "%0.3f"%(Mean-2*Std); two_sigma_left = str(two_sigma_left)
    two_sigma_right = "%0.3f"%(Mean+2*Std); two_sigma_right = str(two_sigma_right) 
    plt.text(Mean,0,"|",fontsize=10, ha='center', va='center', rotation=0, color='b')
    plt.text(Mean-Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean-Std,0,one_sigma_left,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean+Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean+Std,0,one_sigma_right,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean-Std,0,r"$\mu - \sigma$",fontsize=7, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean-2*Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean-2*Std,0,two_sigma_left,fontsize=7.5, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean+2*Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean+2*Std,0,two_sigma_right,fontsize=7.5, ha='center', va='top', rotation=0, color='black')

    sample_two_sigma_left = "%0.3f"%(INT_Confi[0]); sample_two_sigma_left = str(sample_two_sigma_left)
    sample_two_sigma_right = "%0.3f"%(INT_Confi[1]); sample_two_sigma_right = str(sample_two_sigma_right)
    plt.text(INT_Confi[0],0,"|",fontsize=13, ha='center', va='bottom', rotation=0, color='r')
    plt.text(INT_Confi[0],MAX/8,"$\overline{x}  - 2\sigma_x$", fontsize=18, ha='right', va='top', rotation=0, color='r')
    plt.text(INT_Confi[1],0,"|",fontsize=13, ha='center', va='bottom', rotation=0, color='r')
    plt.text(INT_Confi[1],MAX/8,"$\overline{x}  + 2\sigma_x$", fontsize=18, ha='left', va='top', rotation=0, color='r')
    plt.text(INT_Confi[0],MAX/24,sample_two_sigma_left,fontsize=7.5, ha='right', va='bottom', rotation=0, color='r')
    plt.text(INT_Confi[1],MAX/24,sample_two_sigma_right,fontsize=7.5, ha='left', va='bottom', rotation=0, color='r')

    if(Xaxis_Name == ''):
        XLABEL = filename_No_Txt.replace("_hist",'')
    else:
        XLABEL = Xaxis_Name
    SaveName = filename_No_Txt +"_T_distribution"+ ".pdf"
    plt.xlabel(XLABEL)
    plt.grid(True)
    plt.savefig(SaveName)
    plt.close('all')
    f.close()
#    plt.show()
    return [INT_Confi[0],INT_Confi[1],Total_Entry,Mean]


def main():
#    inputfile = "gaus100.txt"
    inputfile = "tea_0319Mon_LA_s_tree_tea_0319Mon_LA_s_V2_hist.txt"
    T_dist = t_distribution(inputfile,Show_T=True,Show_Gaus=True)
    print(T_dist)

if __name__=="__main__":
    main()


