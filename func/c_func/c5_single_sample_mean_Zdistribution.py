#Author : JUNHO LEE
#According to central limit theorem, even though distribution of population does not belongs to Gaussian, distribution of the sample mean is gaussian, if event number bigger than 30
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import sys,os
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *

# recommand to use on sample size bigger than 30, i.e. n>=30
# Make sure the distribution follows gaussian distribution
def Fit_Sample_Gaus_histo(filename,calc_file='', Xaxis_Name='', SIGMA=2,exp_Mean_error=0.1, norm=0, Show=True, Show_sample=True):
    # returns [Mean-n*sigma,Mean+n*sigma,Total_Entry,Expected number to reach given sigma confidence interval, SIGMA, MEAN,sample_mean_error(std) ,exp_Mean_error]  (exp_MEAN_error =  length of the half of confidence interval you want)

    # Xaxis_Name :: put what you want for Axis name
    # norm :: 0 for normalized histogram showing. (suggest do not change this value)
    # exp_Mean_error :: expected Mean error in given SIGMA level confidence interval
    # SIGMA :: pick your sigma range to be returned
    # Show :: if True, the maximum y value of canvas would be sample_mean_distribution's Maximum value
    # Show_sample :: if True, it will print the sample distribution as well

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
    SSEM = c1_sample_standard_error_of_mean(calc_infile); 
    shorten_SSEM = "%0.4f"%(SSEM)
    str_SSEM = str(shorten_SSEM)

    FROM = Range[0]; END = Range[1];  #print(BIN_NUM, FROM, END)
    Brange = (END-FROM)/BIN_NUM;
    Brange_s = (END-FROM)/BIN_NUM*(SSEM/Std)
    RANGE = END-FROM

    t = np.arange(FROM-RANGE, END+RANGE, Brange_s) 
    tt = np.arange(FROM-RANGE, END+RANGE, Brange_s)   
    gaussian = (1/(Std * np.sqrt(2 * np.pi))*np.exp(-(t-Mean)**2/(2 * Std**2)))
    sample_gaussian = (1/(SSEM * np.sqrt(2 * np.pi))*np.exp(-(tt-Mean)**2/(2 * SSEM**2)))

    LENGTH = (Mean+5*SSEM) - (Mean-5*SSEM)
    HIGHT = 2/LENGTH

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
    WEIGHT = float(Total_Entry)
    for i in range(len(gaussian)):
        gaussian[i] = gaussian[i]/Total_Entry
#            print("!!!",SCALE)
#            sample_gaussian[i] = sample_gaussian[i] / SCALE
#            print(sample_gaussian[i])
#            print(gaussian[i])

#    if(norm==1):
#        for i in range(len(sample_gaussian)):
#            SCALE = sample_gaussian[i] / gaussian[i]
#            sample_gaussian[i] = sample_gaussian[i] / SCALE *9/10
            
    MAX = 0; MAX_S = 0
    for i in range(len(gaussian)):
        if(MAX<gaussian[i]):
            MAX=gaussian[i]

    for i in range(len(sample_gaussian)):
        if(MAX_S<sample_gaussian[i]):
            MAX_S=sample_gaussian[i]

    SCALE_SAM = HIGHT/MAX_S
    MAX_S = 0
    for i in range(len(sample_gaussian)):
        sample_gaussian[i] = sample_gaussian[i] * SCALE_SAM
        if(MAX_S<sample_gaussian[i]):
            MAX_S=sample_gaussian[i]
 
    MAX_Y=0
    for i in range(len(Y_VALUE)):
        Y_VALUE[i] = float(Y_VALUE[i])/WEIGHT
        if(MAX_Y<Y_VALUE[i]):
            MAX_Y=Y_VALUE[i]
    SCALE_Y=MAX_S/MAX_Y
    for i in range(len(Y_VALUE)):
        Y_VALUE[i] = SCALE_Y * Y_VALUE[i]

    SCALE_ALL = MAX_S/MAX
    for i in range(len(gaussian)):
        gaussian[i] = SCALE_ALL * gaussian[i]

    

    plt.figure(1)
#    plt.plot(t,s2)
    plt.plot(t,gaussian)
    plt.plot(tt,sample_gaussian, color='r')
    plt.grid(True)
    plt.ylabel("Probability of Sample Mean", color='r')
    plt.yticks(color ='red')
    if(Xaxis_Name == ''):
        XLABEL = filename_No_Txt.replace("_hist",'')
    else:
        XLABEL = Xaxis_Name
    plt.xlabel(XLABEL)


#    YLIST = [0,float(int(Mode[2]/5)), float(int(Mode[2]/5*2)), float(int(Mode[2]/5*3)), float(int(Mode[2]/5*4)),  float(int(Mode[2]))]
#    print(YLIST)    
    if(Show_sample==True):
#        plt.twinx()
#        print(plt.yticks())
#        plt.yticks( color="green")
#        plt.yticks(np.arange(len(plt.yticks())),YLIST)
        barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0],fill=False)
        for i in range(len(barlist)):
            barlist[i].set_color('g')
    plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,MAX_S*21/20])
    MAX = MAX_S

    '''
    if(Show == False):
        plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,Mode[2]*10/9/WEIGHT])
    else:
        plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,MAX_S])
        MAX = MAX_S
    '''

    locs, labels = plt.xticks()
    TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "POP Mean Est: " + str_Mean + "\n" + "POP Std Est: " + str_Std \
           + "\n" + "Sample Mean STD: " + str_SSEM
    ''''
    if(Show == False): 
        plt.text(Range[1]-(Range[1]-Range[0])*0.05, Mode[2]*21/20/WEIGHT, TEXT, fontsize=16, ha='right', va='top', rotation=0)
    else:
        plt.text(Range[1]-(Range[1]-Range[0])*0.05, MAX_S*20/21, TEXT, fontsize=16, ha='right', va='top', rotation=0)
    '''
    plt.text(Range[1]-(Range[1]-Range[0])*0.05, MAX_S*20/21, TEXT, fontsize=16, ha='right', va='top', rotation=0)

    one_sigma_left = "%0.3f"%(Mean-Std); one_sigma_left = str(one_sigma_left)
    one_sigma_right = "%0.3f"%(Mean+Std); one_sigma_right = str(one_sigma_right)
    two_sigma_left = "%0.3f"%(Mean-2*Std); two_sigma_left = str(two_sigma_left)
    two_sigma_right = "%0.3f"%(Mean+2*Std); two_sigma_right = str(two_sigma_right)
    plt.text(Mean-2*Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean-2*Std,0,two_sigma_left,fontsize=7.5, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean+2*Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean+2*Std,0,two_sigma_right,fontsize=7.5, ha='center', va='top', rotation=0, color='black')
#    plt.text(Mean,0,r"$\mu \pm 2\sigma$",fontsize=20, ha='right', va='bottom', rotation=0, color='black')
 
    plt.text(Mean,0,"|",fontsize=10, ha='center', va='center', rotation=0, color='b')

    plt.text(Mean-Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean-Std,0,one_sigma_left,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean+Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean+Std,0,one_sigma_right,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean-Std,0,r"$\mu - \sigma$",fontsize=7, ha='right', va='bottom', rotation=0, color='black')

    sample_two_sigma_left = "%0.3f"%(Mean-2*SSEM); sample_two_sigma_left = str(sample_two_sigma_left)
    sample_two_sigma_right = "%0.3f"%(Mean+2*SSEM); sample_two_sigma_right = str(sample_two_sigma_right)
    plt.text(Mean-2*SSEM,0,"|",fontsize=13, ha='center', va='bottom', rotation=0, color='r')
    plt.text(Mean-2*SSEM,MAX/4,"$\overline{x}  - 2\sigma_x$", fontsize=18, ha='right', va='top', rotation=0, color='r')
    plt.text(Mean+2*SSEM,0,"|",fontsize=13, ha='center', va='bottom', rotation=0, color='r')
    plt.text(Mean+2*SSEM,MAX/4,"$\overline{x}  + 2\sigma_x$", fontsize=18, ha='left', va='top', rotation=0, color='r')
    plt.text(Mean-2*SSEM,MAX/6,sample_two_sigma_left,fontsize=7.5, ha='right', va='bottom', rotation=0, color='r')
    plt.text(Mean+2*SSEM,MAX/6,sample_two_sigma_right,fontsize=7.5, ha='left', va='bottom', rotation=0, color='r')

    plt.xlabel(XLABEL)
    plt.title(filename_No_Txt)
    SaveName = filename_No_Txt +"_Gaussian_normalized"+ ".pdf"
    plt.grid(True)
    plt.savefig(SaveName)
#    plt.show()
    plt.close('all')
    f.close()
    Ex_Num = (SIGMA*Std/exp_Mean_error)*(SIGMA*Std/exp_Mean_error)
    return_list = [float("%0.6f"%(Mean-SIGMA*SSEM)),float("%0.6f"%(Mean+SIGMA*SSEM)),Total_Entry,float("%0.3f"%(Ex_Num)),str(SIGMA)+" SIGMA",float("%0.6f"%(Mean)),float("%0.6f"%(SSEM)), exp_Mean_error]

    print("Careful!!!!")
    print("Event number better larger than 30 !!!!!")
    print("Current Event number is : ",Total_Entry)
    return return_list


def main():
    inputfile = "gaus100.txt"
#    inputfile = "ZRXBTC_1T_f_quote_volume_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/AQI_BEIJING/AQI_BEIJING_tree_cut_AQI_BEIJING_f_AQI_hist.txt"
#    inputfile = "beer_0319Mon_LA_s_tree_beer_0319Mon_LA_s_V2_hist.txt"
#    inputfile = "tea_0319Mon_LA_s_tree_tea_0319Mon_LA_s_V2_hist.txt"

    Two_sigma_range = Fit_Sample_Gaus_histo(inputfile, ".X-axis.", SIGMA=2, Show_sample=True, Show = True, exp_Mean_error=0.1)
#    Two_sigma_range = Fit_Sample_Gaus_histo(inputfile,SIGMA=1.96, exp_Mean_error=0.05)
    print(Two_sigma_range)

if __name__ == "__main__":
    main()

