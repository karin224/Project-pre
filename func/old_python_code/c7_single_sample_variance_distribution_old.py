from matplotlib import pyplot as plt
import numpy as np
import sys,os
from sympy import exp,sqrt,pi,Integral
import math
from scipy.stats import chi2
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *

# plotting APLHA with 0.025, 0.05, 0.95,0.975
def Sample_Variance(filename, ALPHA=0.05):
    # return value : [Lower_chi2 on given ALPHA, Higher_chi2 on given ALPHA, Lower_Sigma2 on given ALPHA, Higher_Sigma2 on given ALPHA, Total_Entry, ALPHA, Mean, Variance]

    if(filename[0]=="/"):
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
#    df = 8
    x = np.linspace(chi2.ppf(0.000001, df), chi2.ppf(0.999999, df), 10000)
    xs = np.linspace(df*Var/chi2.ppf(0.999999, df),df*Var/chi2.ppf(0.000001, df), 10000)
#    print(xs)
    MAX_CHI2 = 0
    TEST_LIST = chi2.pdf(x, df)
    for i in range(len(TEST_LIST)):
        if(MAX_CHI2 < TEST_LIST[i]):
            MAX_CHI2 = TEST_LIST[i]

    plt.axis([chi2.ppf(0.000001, df), chi2.ppf(0.999999, df), 0, MAX_CHI2*24/20])
    plt.plot(x, chi2.pdf(x, df),'r-', lw=1, alpha=0.6, label='chi2 pdf')
    plt.grid(True)
    plt.title(filename_No_Txt)
    plt.xlabel("$\chi^2$")
    TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "POP Var Est : " + str_Var + "\n"+ "POP STD Est : " + str_Std + "\n POP Mean Est : "+str_Mean
    plt.text((chi2.ppf(0.999999, df)-(chi2.ppf(0.999999, df)-chi2.ppf(0.000001, df))*0.05),MAX_CHI2*23/20,TEXT, fontsize=16, ha='right', va='top', rotation=0)
    p05 = "%0.3f"%(chi2.ppf(0.05,df)); p05 = str(p05)
    p025= "%0.3f"%(chi2.ppf(0.025,df));p025= str(p025)
    p95 = "%0.3f"%(chi2.ppf(0.95,df)); p95 = str(p95)
    p975= "%0.3f"%(chi2.ppf(0.975,df));p975= str(p975)
    p025s= "%0.3f"%((df*Var)/chi2.ppf(0.975, df));p025s= str(p025s)
    p975s= "%0.3f"%((df*Var)/chi2.ppf(0.025, df));p975s= str(p975s)
    p025ss= "%0.3f"%(math.sqrt((df*Var)/chi2.ppf(0.975, df)));p025ss= str(p025ss)
    p975ss= "%0.3f"%(math.sqrt((df*Var)/chi2.ppf(0.025, df)));p975ss= str(p975ss)
    plt.text(chi2.ppf(0.05,df),0,"|",fontsize=6, ha='center', va='center', rotation=0, color='g')
    plt.text(chi2.ppf(0.05,df),0,p05,fontsize=7, ha='center', va='top', rotation=0, color='g')
    plt.text(chi2.ppf(0.025,df),0,"|",fontsize=6, ha='center', va='center', rotation=0, color='r')
    plt.text(chi2.ppf(0.025,df),0,p025,fontsize=7, ha='center', va='bottom', rotation=0, color='r')
    plt.text(chi2.ppf(0.025,df),MAX_CHI2/6,p025s,fontsize=14, ha='center', va='bottom', rotation=0, color='b')
    plt.text(chi2.ppf(0.95,df),0,"|",fontsize=6, ha='center', va='center', rotation=0, color='g')
    plt.text(chi2.ppf(0.95,df),0,p95,fontsize=7, ha='center', va='top', rotation=0, color='g')
    plt.text(chi2.ppf(0.975,df),0,"|",fontsize=6, ha='center', va='center', rotation=0, color='r')
    plt.text(chi2.ppf(0.975,df),0,p975,fontsize=7, ha='center', va='bottom', rotation=0, color='r')
    plt.text(chi2.ppf(0.975,df),MAX_CHI2/6,p975s,fontsize=14, ha='center', va='bottom', rotation=0, color='b')
    plt.text(chi2.ppf(0.025,df),MAX_CHI2/8,"|",fontsize=14, ha='center', va='bottom', rotation=0, color='b')
    plt.text(chi2.ppf(0.975,df),MAX_CHI2/8,"|",fontsize=14, ha='center', va='bottom', rotation=0, color='b')
    plt.text(chi2.ppf(0.025,df)+(chi2.ppf(0.975,df)-chi2.ppf(0.025,df))/2,MAX_CHI2/8,"<-- $\sigma^2$ -->",fontsize=14, ha='center', va='bottom', rotation=0, color='b')
#    plt.show()
    SaveName = filename_No_Txt +"_Variance"+ ".pdf"
    plt.savefig(SaveName)
    plt.close('all')

    MAX_STD = 0
    TEST_LIST = 1/chi2.pdf(x, df)
    XS_MIN = xs[0]; XS_MAX = xs[len(xs)-1]
    for i in range(len(xs)):
        if(MAX_STD<TEST_LIST[i]):
            MAX_STD=TEST_LIST[i]

    LOW_chi2 = chi2.ppf(ALPHA/2, df); HIGH_chi2 = chi2.ppf(1-ALPHA/2, df)
#    print(LOW_chi2, HIGH_chi2)
    LOW_sigma = (df*Var)/chi2.ppf(1-ALPHA/2, df); HIGH_sigma = (df*Var)/chi2.ppf(ALPHA/2, df)
#    print(LOW_sigma,HIGH_sigma)


    plt.axis([(df*Var)/chi2.ppf(0.999, df), (df*Var)/chi2.ppf(0.001, df), 0, MAX_STD*24/20])
    plt.plot(xs, 1/chi2.pdf(x, df),'r-', lw=1, alpha=0.6, label='chi2 pdf')
    plt.grid(True)
    plt.xlabel("$\sigma^2$")
    TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "POP Var Est : " + str_Var +"\n"+ "POP STD Est: " + str_Std
    plt.text((df*Var)/chi2.ppf(0.999, df)+((df*Var)/chi2.ppf(0.001, df)-(df*Var)/chi2.ppf(0.999, df)),MAX_STD*23/20,TEXT, fontsize=16, ha='right', va='top', rotation=0)
    p05 = "%0.3f"%((df*Var)/chi2.ppf(0.95, df)); p05 = str(p05)
    p025= "%0.3f"%((df*Var)/chi2.ppf(0.975, df));p025= str(p025)
    p95 = "%0.3f"%((df*Var)/chi2.ppf(0.05, df)); p95 = str(p95)
    p975= "%0.3f"%((df*Var)/chi2.ppf(0.025, df));p975= str(p975)
    plt.text((df*Var)/chi2.ppf(0.95, df),0,"|",fontsize=6, ha='center', va='center', rotation=0, color='g')
    plt.text((df*Var)/chi2.ppf(0.95, df),0,p05,fontsize=7, ha='center', va='top', rotation=0, color='g')
    plt.text((df*Var)/chi2.ppf(0.975, df),0,"|",fontsize=6, ha='center', va='center', rotation=0, color='r')
    plt.text((df*Var)/chi2.ppf(0.975, df),0,p025,fontsize=7, ha='center', va='bottom', rotation=0, color='r')
    plt.text((df*Var)/chi2.ppf(0.05, df),0,"|",fontsize=6, ha='center', va='center', rotation=0, color='g')
    plt.text((df*Var)/chi2.ppf(0.05, df),0,p95,fontsize=7, ha='center', va='top', rotation=0, color='g')
    plt.text((df*Var)/chi2.ppf(0.025, df),0,"|",fontsize=6, ha='center', va='center', rotation=0, color='r')
    plt.text((df*Var)/chi2.ppf(0.025, df),0,p975,fontsize=7, ha='center', va='bottom', rotation=0, color='r')

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

    RETURN_LIST = [float("%0.6f"%(LOW_chi2)), float("%0.6f"%(HIGH_chi2)), float("%0.6f"%(LOW_sigma)), float("%0.6f"%(HIGH_sigma)), Total_Entry, "alpha = " +str(ALPHA), float("%0.6f"%(Mean)),float("%0.6f"%(Var))]
    return RETURN_LIST

def main():
#    infile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_tree_cut_Aqi_Beijing_f_AQI_hist.txt"
    infile = "gaus100.txt"
#    infile = "gaus60.txt"
#    infile = "tea_0319Mon_LA_s_tree_tea_0319Mon_LA_s_V2_hist.txt"

    SV = Sample_Variance(infile)
    print(SV)

if __name__=="__main__":
    main()



