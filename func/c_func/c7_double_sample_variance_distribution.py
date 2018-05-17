import matplotlib
matplotlib.use('TkAgg')
from scipy.stats import f as F_TEST
import matplotlib.pyplot as plt
import numpy as np

def double_Sample_Variance(outputname = "test", VAR1 = 1, tot1=100, VAR2 = 0.5, tot2=100):
    #no return value
    F = VAR1 / VAR2
    df1 = tot1-1; df2 = tot2-1;
    x = np.linspace(F_TEST.ppf(0.0001, df1, df2),F_TEST.ppf(0.9999, df1, df2), 10000)
    str_tot1 = str(tot1)
    str_tot2 = str(tot2)
    MAX = 0
    for aa in F_TEST.pdf(x, df1, df2):
        if(MAX<aa):
            MAX=aa

    plt.plot(x, F_TEST.pdf(x, df1, df2),'r')
    plt.axis([F_TEST.ppf(0.0001, df1, df2), F_TEST.ppf(0.9999, df1, df2), 0,MAX*5/4])
    TEXT = "Sample 1 Entry : "+str_tot1+"\n" + "Sample 1 VAR : "+"%0.3f"%(VAR1)+"\n"+ "Sample 2 Entry : "+str_tot2+"\n" + "Sample 2 VAR : "+"%0.3f"%(VAR2)
    plt.text(F_TEST.ppf(0.9999, df1, df2)-(F_TEST.ppf(0.9999, df1, df2)-F_TEST.ppf(0.0001, df1, df2))*0.05, MAX*23/20,TEXT, fontsize=16, ha='right', va='top', rotation=0)
    
    p025= "%0.3f"%(F_TEST.ppf(0.025, df1, df2));p025= str(p025)
    p975= "%0.3f"%(F_TEST.ppf(0.975, df1, df2));p975= str(p975)
    plt.axvline(p025); plt.axvline(p975)
    plt.text(F_TEST.ppf(0.025,df1, df2),0,p025,fontsize=14, ha='left', va='bottom', rotation=0, color='r')
    plt.text(F_TEST.ppf(0.975,df1, df2),0,p975,fontsize=14, ha='right', va='bottom', rotation=0, color='r')
    plt.text(F_TEST.ppf(0.025,df1, df2),0,"P975",fontsize=7, ha='right', va='top', rotation=0, color='green')
    plt.text(F_TEST.ppf(0.975,df1, df2),0,"P025",fontsize=7, ha='left', va='top', rotation=0, color='green')

    plt.grid(True)
#    plt.show()
    SaveName = outputname + "2sample_VAR_F_dist.pdf"
    plt.savefig(SaveName)
    plt.close('all')


def main():
    double_Sample_Variance(outputname = "test", VAR1 = 10, tot1=10000, VAR2=10.5, tot2=10000)


if __name__=="__main__":
    main()

