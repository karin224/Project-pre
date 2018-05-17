#Author : JUNHO LEE
#Required : np>=5 and also, n(1-p)>=5
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import math
import sys,os
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *

#Make sure that : np>=5 and also, n(1-p)>=5, in order to make sample proportion distribution smear to gaussian
def Sample_proportion(proportion=0.1, event_num = 100,Title='', Xaxis_Name='', SIGMA=2, exp_Mean_error=0.001 ):
    # returns [Mean-n*sigma,Mean+n*sigma,Total_Entry,Expected number to reach given sigma confidence interval, SIGMA, MEAN,sample_mean_error(std) ,exp_Mean_error] (exp_MEAN_error :: [Mean-exp_MEAN_error ,Mean+exp_MEAN_error] within given sigma confidence interval)

    # Xaxis_Name :: put what you want for Axis name
    # exp_Mean_error :: expected Mean error in given SIGMA level confidence interval
    # SIGMA :: pick your sigma range to be returned :: Zc
    # Title :: Name the title of the plot

    Mean = proportion
    Var = proportion*(1-proportion)/event_num
    Std = math.sqrt(Var)
    t = np.arange(proportion-4*Std, proportion+4*Std, ((proportion+Std)-(proportion-Std))/100) 
    gaussian = (1/(Std * np.sqrt(2 * np.pi))*np.exp(-(t-proportion)**2/(2 * Std**2)))

    SCALE = 0
    MAX = 0
    TEST = 0
    for i in range(len(gaussian)):
        SCALE = SCALE + gaussian[i]
    for i in range(len(gaussian)):
        gaussian[i] = gaussian[i]/SCALE
        TEST = gaussian[i] + TEST
        if gaussian[i]>MAX:
            MAX = gaussian[i]
#    print(TEST)

    plt.figure(1)
    plt.plot(t,gaussian)
    plt.axis([proportion-5*Std, proportion+5*Std, 0, MAX * 5/4])

    str_proportion = "%0.3f"%proportion; str_proportion = str(str_proportion)
    str_Std = "%0.4f"%Std; str_Std = str(str_Std)

    TEXT = "Sample Prop Mean : " + str_proportion + "\n" + "Sample Prop Std : " + str_Std
    plt.text((proportion+5*Std)*20/21, MAX*6/5, TEXT, fontsize=16, ha='right', va='top', rotation=0)

    one_sigma_left = "%0.5f"%(Mean-Std); one_sigma_left = str(one_sigma_left)
    one_sigma_right = "%0.5f"%(Mean+Std); one_sigma_right = str(one_sigma_right)
    two_sigma_left = "%0.5f"%(Mean-2*Std); two_sigma_left = str(two_sigma_left)
    two_sigma_right = "%0.5f"%(Mean+2*Std); two_sigma_right = str(two_sigma_right)

    plt.text(Mean-2*Std,0,"|",fontsize=24, ha='right', va='bottom', rotation=0, color='g')
    plt.text(Mean-2*Std,0,two_sigma_left,fontsize=7.5, ha='center', va='top', rotation=0, color='g')
    plt.text(Mean+2*Std,0,"|",fontsize=24, ha='right', va='bottom', rotation=0, color='g')
    plt.text(Mean+2*Std,0,two_sigma_right,fontsize=7.5, ha='center', va='top', rotation=0, color='g')
#    plt.text(Mean,0,r"$\mu \pm 2\sigma$",fontsize=20, ha='right', va='bottom', rotation=0, color='g')

    plt.text(Mean,0,"|",fontsize=13, ha='center', va='center', rotation=0, color='b')

    plt.text(Mean-Std,0,"|",fontsize=24, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean-Std,0,one_sigma_left,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean+Std,0,"|",fontsize=24, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean+Std,0,one_sigma_right,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean,0,r"$\mu \pm \sigma$",fontsize=20, ha='center', va='bottom', rotation=0, color='black')

    plt.grid(True)
    if(Title == ''):
        TITLE = "Single Sample Proportion distribution"
    else:
        TITLE = Title
    plt.title(TITLE)

    if(Xaxis_Name == ''):
        XLABEL = "Proportion"
    else:
        XLABEL = Xaxis_Name
    plt.xlabel(XLABEL)
    plt.ylabel("Probability")
    SaveName = TITLE; SaveName = SaveName.replace(" ","_"); SaveName = SaveName+".pdf"
#    print(SaveName)
    plt.savefig(SaveName)
#    plt.show()
    plt.close('all')

    Ex_Num = (SIGMA*math.sqrt(proportion*(1-proportion))/exp_Mean_error)*(SIGMA*math.sqrt(proportion*(1-proportion))/exp_Mean_error)

#    print(Ex_Num)
    R_LIST = [float("%0.6f"%(Mean-SIGMA*Std)), float("%0.6f"%(Mean+SIGMA*Std)),event_num, float("%0.3f"%(Ex_Num)), str(SIGMA)+" SIGMA", float("%0.6f"%(Mean)), float("%0.6f"%(Std)), exp_Mean_error]
    return R_LIST


def main():
    Total = 63886.0; pos = 1841.0
    pos_pro= pos/Total; #print(pos_pro)
    twoSigma_region = Sample_proportion(proportion=pos_pro, event_num = Total, SIGMA = 3, exp_Mean_error=0.001)
#    twoSigma_region = Sample_proportion(proportion=0.031, event_num = 10000, SIGMA = 3, exp_Mean_error=0.0005)
    print(twoSigma_region)    

if __name__ == "__main__":
    main()

