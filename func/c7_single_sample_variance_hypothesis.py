import sys,os
import math
from scipy.stats import chi2
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *


def Sample_Variance_both_side(filename,ALPHA=0.05, test_VAR=10):
#returns [Low_chi2,High_chi2,test_chi2,Low_sigma2,High_sigma2,test_sigma2(test_VAR),ALPHA, Var ,p-value]  
#             0       1         2          3          4           5                   6     7      8
    # H0 : Var = test_VAR
    # H1 : Var != test_VAR

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
    infile = filename

    BIN_NUM = bin_num(infile);        #print(BIN_NUM)
    Mode = most_frequent_bin(infile); #print(type(Mode)); print(Mode)
    Median = c1_median(infile)
    Range = c1_data_range(infile);    #print(Range)
    Total_Entry = c1_total_ENTRY(infile); Total_Entry = int(Total_Entry); str_TE = str(Total_Entry)
    Mean = c1_mean(infile);  str_Mean = "%0.3f"%(Mean); str_Mean = str(str_Mean)
    Var = c1_variance(infile);
    Std = c1_standard_deviation(infile); str_Std = "%0.3f"%(Std); str_Std = str(str_Std)
#    Var = 0.5325
    str_Var = "%0.3f"%(Var) ;str_Var = str(str_Var)
    df = Total_Entry-1

    LOW_chi2 = chi2.ppf(ALPHA/2, df); HIGH_chi2 = chi2.ppf(1-ALPHA/2, df)
    LOW_sigma = (df*Var)/chi2.ppf(1-ALPHA/2, df); HIGH_sigma = (df*Var)/chi2.ppf(ALPHA/2, df)
    test_Chi2 = df*Var/test_VAR
#    if((test_VAR>=LOW_sigma)&(test_VAR<=HIGH_sigma)):
#        deter = "ACCEPT H0, VAR = test_VAR"
#    else:
#        deter = "REJECT H0, VAR!=test_VAR" 

    pValue = -100
    if(test_Chi2<=chi2.ppf(0.5,df)):
        pValue = 2*chi2.cdf(test_Chi2,df)
    elif(test_Chi2>=chi2.ppf(0.5,df)):
        pValue = 2*(1 - chi2.cdf(test_Chi2,df))  # alpla'/2 * 2 to get pValue


    R_LIST = [float("%0.6f"%(LOW_chi2)),float("%0.6f"%(HIGH_chi2)),float("%0.6f"%(test_Chi2)),float("%0.6f"%(LOW_sigma)),float("%0.6f"%(HIGH_sigma)),float("%0.6f"%(test_VAR)),"ALPHA = "+str(ALPHA),float("%0.6f"%(Var)), float("%0.6f"%(pValue))]
    return R_LIST


def main():
    infile = "gaus100.txt" 
    Hypo = Sample_Variance_both_side(infile,ALPHA=0.05, test_VAR=5.8)
    print(Hypo)

if __name__=="__main__":
    main()

