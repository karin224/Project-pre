import matplotlib
matplotlib.use('TkAgg')
from c0_READ_PATH_FILE import read_file_name
from d0_makelist_column import MakeList_column
import numpy as np
import matplotlib.pyplot as plt
import math

def PlotProper_YearDATE(filename,title="Development",Xlabel="Date",Ylabel="Object", MSE=1.0):
    filelist = read_file_name(filename)
    Col_list = MakeList_column(filelist[2])
    #print(len(Col_list))    
    Y_data = []
    nomi_X_date = []
    List_x = []; 
    temp_x = []
    error_low = []; error_high = [];
    error_2low = []; error_2high = [];
    sqrt_MSE = math.sqrt(MSE*MSE/365.0)
    MIN_Y=0; MAX_Y=0
    for i in range(len(Col_list[1])):
        if(i==0):
            continue
        if(i > 1):
            if float(Col_list[1][i])>MAX_Y:
                MAX_Y = float(Col_list[1][i])
            if float(Col_list[1][i])<MIN_Y:
                MIN_Y = float(Col_list[1][i])
        Y_data.append(float(Col_list[1][i]))
        error_low.append(float(Col_list[1][i])-sqrt_MSE); error_2low.append(float(Col_list[1][i])-2*sqrt_MSE)
        error_high.append(float(Col_list[1][i])+sqrt_MSE);error_2high.append(float(Col_list[1][i])+2*sqrt_MSE) 
        nomi_X_date.append(float(Col_list[0][i]))
        List_x.append(str(int(Col_list[0][i])))
        temp_x.append(i-1)
        if(i==1):
            MIN_Y = float(Col_list[1][i])
            MAX_Y = float(Col_list[1][i])
    RANGE_Y = (MAX_Y - MIN_Y)/5

    plt.grid(True)
    plt.plot(Y_data,'b^:')
    plt.fill_between(temp_x,error_2low,error_2high,edgecolor='#FF9848', facecolor='#FF9848')
    plt.fill_between(temp_x,error_low,error_high,edgecolor='#7EFF99', facecolor='#7EFF99')
    #plt.fill_between(temp_x,error_2low,error_2high,edgecolor='#CC4F1B', facecolor='#FF9848')
    plt.plot([18,19,20,21],[23.69,23.08,26.17,24.72],'r^-')  #Manually input real 2014,2015,2016,2017 DATA
    #plt.plot(temp_x,'r:')
    plt.title(title)
    plt.xlabel(Xlabel); plt.ylabel(Ylabel)
    plt.axis([-1,len(Col_list[1])-1,MIN_Y-RANGE_Y,MAX_Y+RANGE_Y])
    #plt.xticks(np.arange(len(Col_list[1])),('Tom', '', '', '', 'Sue'))
    if(len(Col_list[1]) < 10):
        plt.xticks(np.arange(len(Col_list[1]),nomi_X_date))
    else:
        XTicks = []
        tot_len = len(nomi_X_date)
        for i in range(tot_len):
            if(i==0):
                XTicks.append(List_x[i])
            elif(i == int(tot_len/4)):
                XTicks.append(List_x[i])
            elif(i == int(tot_len/2)):
                XTicks.append(List_x[i])
            elif(i == int(3*tot_len/4)):
                XTicks.append(List_x[i])
            elif(i == int(tot_len)-1): 
                XTicks.append(List_x[i])
                break
            else:
                XTicks.append("")
        plt.xticks(np.arange(len(Col_list[1])),XTicks)
    plt.legend(["Predicted PM2.5","Recorded PM2.5",r"$2 \sigma$ Error band", r"$1 \sigma$ Error band"])
    plt.show()



def main():
#    infile = "/Users/leejunho/Desktop/git/python3Env/group_study/NOT_USUALLY_VISIT/statistic_group_study/R_language/PM2p5_DNN_Since97_predicted_Monthly.txt"
    infile = "/Users/leejunho/Desktop/git/python3Env/group_study/NOT_USUALLY_VISIT/statistic_group_study/R_language/PM2p5_DNN_Since97_predicted_Year.txt"
    PlotProper_YearDATE(infile, title="PM2.5 in SEOUL",Xlabel="DATE (Year)",Ylabel= r"PM2.5 Density $(\mu g/m^3)$",MSE=18.7915)

if __name__=="__main__":
    main()
