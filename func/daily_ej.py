import matplotlib
matplotlib.use('TkAgg')
import sys,os

sys.path.append("C:/Users/eunjin/PycharmProjects/Project-pre/func")
from c0_READ_PATH_FILE import read_file_name
from d0_makelist_column import MakeList_column
from matplotlib import pyplot as plt


def Daily_data(filename):
    FILE = read_file_name(filename)
    infile1 = FILE[2]
    COL_LIST1 = MakeList_column(infile1)

#    print(COL_LIST1)
    for s in range(len(COL_LIST1)-1):
#        print(COL_LIST1[s][0])
        x= [COL_LIST1[0][i+1] for i in range(len(COL_LIST1[0])-1)]
        y = [float(COL_LIST1[s+1][j+1]) for j in range(len(COL_LIST1[0])-1)]
        plt.xlabel(COL_LIST1[0][0])
        plt.ylabel(COL_LIST1[s+1][0])
#        print(x,y)
        plt.plot(x,y,color='green',marker='o',linestyle='solid')
        plt.grid(True)
        SavefileName = FILE[0] + "_" + COL_LIST1[s][0] + "_month_plot.pdf"
        print(SavefileName)
#        plt.show()
        plt.savefig(SavefileName)
        plt.close('all')        


def main():
#    inputfile = "../data_txt/BEIJING_Aqi/python_Months_txt/Aqi_Beijing_HoliRCS_M201404.txt"
    inputfile = "../data_txt/BEIJING_Aqi/month201404.txt"
    FileNameList = Daily_data(inputfile)
    print(FileNameList)


if __name__ == "__main__":
    main()
