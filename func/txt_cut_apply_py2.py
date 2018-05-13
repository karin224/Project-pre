import sys
import os
from d0_makelist_column import *
from d0_makelist import *
import numpy as np

def cut_apply(filename):
    path = '../data_txt/BEIJING_Aqi'
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
    list_a = MakeList(infile)
    elements = list_a[0]
    ele_name = "Elements :"
    for i in range(len(elements)):
        ele_name += elements[i]+"="+str(i)+" "
    print(ele_name)
    x_list = []
    del_list = []
    for i in range(len(list_a)):
        del_list.append(0)
    #print(len(del_list))
    while 1:

        index = raw_input("what element do you want to cut?(if you don't want cut the raw data, please enter '-')")
       # print(index)
        if index =='-':
            print("end!")
            break
           # print("wrong input!,please select number 0~9")
        x_list = list_c[int(index)]
        min = raw_input("input min-value of cut range (if you don't want to set the cutting min-value, please enter '-')")
        try:
            min = float(min)
        except:
            min = -100000000
        max = raw_input("input max-value of cut range (if you don't want to set the cutting max-value, please enter '-')")
        try:
            max = float(max)
        except:
            max = 100000000
        one = raw_input("input one exect value you want to cut (if you don't want, please enter '-')")
        try:
            one = float(one)
        except:
            one = 100000000
#        del(list_a[0])
 #       print(list_a)
       # print(len(list_a))
        j = 1

        while 1:
            if j >= len(x_list):
                break
            if float(x_list[j])<= min or float(x_list[j]) >= max or float(x_list[j])==one:
                #print(j)
                del_list[j] = 1
                j +=1
             #   del(x_list[j])
              #  del(list_a[j])
            else:
                j += 1

    #print(len(del_list),len(list_a))
    i = 1
    while i<len(del_list):
        if del_list[i] == 1:
            #print(i)
            del(list_a[i])
            del(del_list[i])
        else:
            i+=1
    FN = filename.replace(".txt", "C.txt")
   # FN = path + FN
   # print(FN)
    Of = open(FN, "w+")
    for i in range(len(list_a)):
        for j in range(len(list_a[i])):
            Of.write(str(list_a[i][j]))
            if(j != len(list_a[i])-1):
                Of.write(" ")
        Of.write("\n")
    Of.close()
   # os.system("move *_cutted.pdf "+ path)
    return FN


    #print(type(index),type(min),max)

def main():
    file1 = "../data_txt/BEIJING_Aqi/Aqi_Beijing_Holi.txt"
    path =cut_apply(file1)
    print(path)
    # print("over!",i,j,x,x_len)

if __name__ == "__main__":
    main()

