import numpy as np
import math
import sys,os
import scipy
from scipy import stats
from statsmodels.stats import weightstats
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *

#Single hypothesis examination of SAMPLE_MEAN value. To see whether given "TEST_MEAN" significantly different with sample "MEAN"
# "pvalue < alpha", say alpha = 0.05, reject H0, accept H1 within alpha level. 
# Assume under n>=30, the t distribution could be smear to gaussian, but we do Ttest to be more precised. 
def bothSide_hypothesis(filename, TEST_MEAN=0):
    #returns : [Zc(sigma),p value, sample_SAMPLE_MEAN, TEST_MEAN]
    
    #filename :: input filename
    #TEST_MEAN :: The mean value to be tested, whether it is significantly different with sample mean. 

    # H0 : SAMPLE_MEAN = TEST_MEAN
    # H1 : SAMPLE_MEAN != TEST_MEAN
    
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

    SAMPLE_MEAN = c1_mean(infile)
    Total_Entry = c1_total_ENTRY(infile);
    Std = c1_standard_deviation(infile)
    
    
    DF = Total_Entry-1
    INT_Confi = stats.t(df=DF).ppf((0.025,0.975))
    INT_Confi = [SAMPLE_MEAN+INT_Confi[0]*Std/math.sqrt(Total_Entry),SAMPLE_MEAN+INT_Confi[1]*Std/math.sqrt(Total_Entry)]
    print("95% confi interval",INT_Confi)

    DATA_LIST = []
    f = open(infile,'r')
    for line in f:
        _,xaxis0,xaxis1, yaxis = line.split()
        X1 = float(xaxis0); X2 = float(xaxis1); Y = int(float(yaxis))
        if Y==0:
            continue
        else:
            for i in range(Y):
                DATA_LIST.append(X1+(X2-X1)/2)
#    print(DATA_LIST)
#    print(len(DATA_LIST))
    f.close()

#    Ztest = weightstats.ztest(DATA_LIST, value=TEST_MEAN ,alternative='two-sided') 
    Ttest = stats.ttest_1samp(DATA_LIST,TEST_MEAN)
#    print(Ttest[0]); print(Ttest[1])
    List = [float("%0.6f"%(Ttest[0])), float("%0.6f"%(Ttest[1])), float("%0.6f"%(SAMPLE_MEAN)), TEST_MEAN]
    return List


def main():
    inputfile = "gaus100.txt"
    T_test = bothSide_hypothesis(inputfile, TEST_MEAN = 9.6)
    print(T_test)

if __name__=="__main__":
    main()



