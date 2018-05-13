#Author : JUNHO LEE
#According to central limit theorem, even though distribution of population does not belongs to Gaussian, distribution of the sample mean is gaussian, if event number bigger than 30
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import sys,os
import math
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *

def double_mean_Zdistribution(filename="test",sample_mean1=0, std1=1, tot1=100,sample_mean2=1, std2=2, tot2=100):
    #no return value
    MEAN = float(sample_mean1) - float(sample_mean2)
    VAR = (float(std1)*float(std1)/tot1 + float(std2)*float(std2)/tot2) 
    STD = math.sqrt(VAR)

    LOWE = MEAN - 5*STD;
    HIGHE = MEAN + 5*STD;
#    print(LOWE,HIGHE)
    tt = np.arange(LOWE, HIGHE, (HIGHE-LOWE)/10000)
    gaussian = (1/(STD * np.sqrt(2 * np.pi))*np.exp(-(tt-MEAN)**2/(2 * STD**2)))

    SUM=0; MAX=0; II = 0
    for i in range(len(gaussian)):
        SUM = SUM + gaussian[i]
        if(MAX<gaussian[i]):
            MAX=gaussian[i]
            II = i
    SUM=1
    for i in range(len(gaussian)):
        gaussian[i] = gaussian[i]/SUM


    plt.axis([LOWE,HIGHE,0,gaussian[II]*5/4])
    TEXT = "Entry sample 1: "+str(tot1)+"\n" + "MEAN sample 1 : "+"%0.3f"%(sample_mean1)+"\n" + "STD sample 1 : "+"%0.3f"%(std1)+"\n" + "Entry sample 2:  "+str(tot2)+"\n" +"MEAN sample 2 : "+"%0.3f"%(sample_mean2)+"\n" + "STD sample 2 : "+"%0.3f"%(std2)+"\n" + "Mean diff STD : "+"%0.5f"%(STD)

    one_sigma_left = "%0.3f"%(MEAN-STD); one_sigma_left = str(one_sigma_left)
    one_sigma_right = "%0.3f"%(MEAN+STD); one_sigma_right = str(one_sigma_right)
    two_sigma_left = "%0.3f"%(MEAN-2*STD); two_sigma_left = str(two_sigma_left)
    two_sigma_right = "%0.3f"%(MEAN+2*STD); two_sigma_right = str(two_sigma_right)
    plt.text(HIGHE-(HIGHE-LOWE)*0.05,gaussian[II]*24/20, TEXT, fontsize=16, ha='right', va='top', rotation=0)
    plt.text(MEAN,0,"|",fontsize=10, ha='center', va='center', rotation=0, color='b')
    plt.text(MEAN,0,"%0.3f"%(MEAN),fontsize=10, ha='center', va='bottom', rotation=0, color='b')
    plt.text(MEAN-STD,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(MEAN-STD,0,one_sigma_left,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(MEAN+STD,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(MEAN+STD,0,one_sigma_right,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(MEAN-STD,0,r"$\mu - \sigma$",fontsize=7, ha='right', va='bottom', rotation=0, color='black')
    plt.text(MEAN-2*STD,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='red')
    plt.text(MEAN-2*STD,0,two_sigma_left,fontsize=7.5, ha='center', va='top', rotation=0, color='red')
    plt.text(MEAN+2*STD,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='red')
    plt.text(MEAN+2*STD,0,two_sigma_right,fontsize=7.5, ha='center', va='top', rotation=0, color='red')
    plt.text(MEAN-2*STD,0,r"$\mu - 2\sigma$",fontsize=13, ha='right', va='bottom', rotation=0, color='red')
    plt.text(MEAN+2*STD,0,r"$\mu + 2\sigma$",fontsize=13, ha='right', va='bottom', rotation=0, color='red')
    
    plt.axvline(MEAN-2*STD)
    plt.axvline(MEAN+2*STD)
    plt.plot(tt,gaussian, color='r')
    plt.grid(True)
#    plt.show()
    SaveName = filename + "_two_sample_mean.pdf"
    plt.savefig(SaveName)
    plt.close('all')

def main():
    double_mean_Zdistribution(sample_mean1=90, std1=5, tot1=100,sample_mean2=65, std2=10, tot2=100)


if __name__=="__main__":
    main()


