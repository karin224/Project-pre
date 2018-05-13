import sys
import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
from scipy import stats

def man_py_scatter(filename):
  #  sys.path.append("../../func")
    from d0_makelist_column import MakeList_column
    path = '../data_txt/BEIJING_Aqi/'
    if (filename[0] == "/"):
        filename = filename
    elif ((filename[0] == "C") & (filename[1] == ":")):
        filename = filename
    else:
        filename = os.getcwd() + "/" + filename  # get the path included filename
    loca = len(filename)
    for i in range(1, len(filename) + 1):  # find the "/" location
        if (filename[-i] == "/"):
            loca = i - 1
            break

    FILENAME = filename.replace(filename[:-loca], "")  # this is the shorten filename
    filename_No_Txt = FILENAME.replace(".txt", "")
    infile = filename

    list_c = MakeList_column(infile)
#date_list = list_c.pop(0)
#print(len(list_c))

    x = len(list_c)
    size = 150/len(list_c[0])
#print(len(list_c[0]),len(list_c[1]),len(list_c[2]))
    for i in range(x):
        y_list_int = []
        y_list = []
        y_list = list_c[i]
   #     print(list_c)
 #   print(y_list)
   # print(i)
    #print(y_list)
        y_label =  y_list[0]

        x_len = len(list_c)
        for k in range(1,len(y_list)):
      #  print(k)
            y_list_int.append(float(y_list[k]))

    #print(len(y_list_int))
        plt.figure(10)
        #print(x_len)
        file_num = math.ceil(x_len/6)
        for l in range(file_num):
            posi = 0
            if (l+1)*6 >= x_len:
                max_num = x_len
            else:
                max_num = (l+1)*6
            for j in range(l*6,max_num):
                posi += 1
                x_list_int = []
                x_list = []
                x_list = list_c[j]
                x_label = x_list[0]
                for k in range(1,len(x_list)):
                    x_list_int.append(float(x_list[k]))
            #num = row_n*100+row_n*10+1+j
            #print(num)
                r,p = stats.pearsonr(x_list_int,y_list_int)
                r = float("%0.2f"%(r))
                p = float("%0.3f" % (p))
                a = plt.subplot(3,2,posi)
                plt.scatter(x_list_int, y_list_int, s=size, c='black', marker='o', alpha=0.5, label='C1')

            #plt.xlabel(x_label)
                plt.text(0.5,0.9,x_label, ha='center', va='center',transform = a.transAxes,fontsize = 8)
                plt.text(0.8, 0.2, 'r='+ str(r), ha='left', va='center',color = 'red', transform=a.transAxes,fontsize = 8)
                plt.text(0.8, 0.1, 'p='+ str(p), ha='left', va='center',color = 'red', transform=a.transAxes,fontsize = 8)
            #plt.ylabel(y_label)
        #plt.title('y = '+y_label+'_'+'x_others')
            plt.savefig(y_label+'_'+'others'+'('+str(l+1)+')'+'.pdf')
            plt.close('all')
  #      x_list_int.clear()
   #     x_list.clear()
   # y_list_int.clear()
   # y_list.clear()


def main():
    file1 = "../data_txt/BEIJING_Aqi/Aqi_Beijing_Holi.txt"
    man_py_scatter(file1)
            # print("over!",i,j,x,x_len)


if __name__=="__main__":
    main()
