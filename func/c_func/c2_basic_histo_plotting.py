#Author : JUNHO LEE
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy
import sys,os
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *


def Basic_histo(filename,calc_file='', Xaxis_Name='', norm=0):

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
    
    Mode = most_frequent_bin(infile); #print(type(Mode)); print(Mode)
    Median = c1_median(calc_infile)
    Range = c1_data_range(calc_infile);   # print(Range)
    Total_Entry = c1_total_ENTRY(calc_infile); Total_Entry = int(Total_Entry); str_TE = str(Total_Entry)
    Mean = c1_mean(calc_infile);  str_Mean = str(Mean)
    Var = c1_variance(calc_infile);
    Std = c1_standard_deviation(calc_infile); str_Std = str(Std)

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
#    print(X_AXIS[0]); print(X_AXIS[BinN-1])
    
    WEIGHT = 1
    if(norm==1):
        WEIGHT = float(Total_Entry)
    for i in range(len(Y_VALUE)):
        Y_VALUE[i] = float(Y_VALUE[i])/WEIGHT

    fig = plt.figure(1)
#    barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0])
    barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0],fill=False)
#    print(len(barlist))
    for i in range(len(barlist)):
        barlist[i].set_color('b')
    plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,Mode[2]*10/9/WEIGHT])
    TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "Mean : " + str_Mean + "\n" + "Std : " + str_Std
    plt.text(Range[1]-(Range[1]-Range[0])*0.05, Mode[2]*21/20/WEIGHT, TEXT, fontsize=16, ha='right', va='top', rotation=0)
#    print(plt.ylim()); print(type(plt.ylim()))
    plt.ylabel("Entry Number")
    if(Xaxis_Name == ''):
        XLABEL = filename_No_Txt.replace("_hist",'')
    else:
        XLABEL = Xaxis_Name
    plt.xlabel(XLABEL)
    plt.title(filename_No_Txt)
    SaveName = filename_No_Txt + ".pdf"
    plt.grid(True)
    plt.savefig(SaveName)
#    plt.show()
    plt.close('all')
    f.close()


def looping_Basic_histo(filenameList, Xaxis_Name=''):
    for filename in filenameList:
        Basic_histo(filename, Xaxis_Name='')


def main():
    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/concrete_tree_cut_concrete_f_fineagg_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/"

#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/root2_tree_cut_tree1_f_py_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/root2_tree_cut_tree1_f_px_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/root2_tree_cut_tree2_f_pz_hist.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/TESTs/project_180324/data_txt/concrete_tree_cut_concrete_f_strength_hist.txt" 
#    inputfile = "../root1_project.txt" 
    Basic_histo(inputfile, ".X-axis.", norm=0)
#    Basic_histo(inputfile, ".X-axis.", norm=True)


if __name__ == "__main__":
    main()

