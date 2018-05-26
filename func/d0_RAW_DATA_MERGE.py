#Author : JUNHO LEE
#This code is for Merge files. filename1 : DATA one column file, filename2 : Multi column DATA file
from d0_makelist_column import MakeList_column
import numpy as np

def Merge(filename1, filename2):

    if(filename1[0]=="/"):
        filename1 = filename1
    elif((filename1[0]=="C")&(filename1[1]==":")):
        filename1 = filename1
    else:
        filename1 = os.getcwd() + "/" + filename1   # get the path included filename
    loca1=len(filename1)
    for i in range (1,len(filename1)+1):       # find the "/" location
        if(filename1[-i] == "/"):
            loca1 = i-1
            break
    FILENAME1 = filename1.replace(filename1[:-loca1],"")   # this is the shorten filename
    filename1_No_Txt = FILENAME1.replace(".txt","")
    infile1 = filename1

    if(filename2[0]=="/"):
        filename2 = filename2
    elif((filename2[0]=="C")&(filename2[1]==":")):
        filename2 = filename2
    else:
        filename2 = os.getcwd() + "/" + filename2   # get the path included filename
    loca2=len(filename2)
    for i in range (1,len(filename2)+1):       # find the "/" location
        if(filename2[-i] == "/"):
            loca2 = i-1
            break
    FILENAME2 = filename2.replace(filename2[:-loca2],"")   # this is the shorten filename
    filename2_No_Txt = FILENAME2.replace(".txt","")
    infile2 = filename2

    DATE_ROW = MakeList_column(infile1)
    DATA_ROW = MakeList_column(infile2)
#    DATE_ROW.append(DATA_ROW[0])
    for i in range(len(DATA_ROW)):
        DATE_ROW.append(DATA_ROW[i])
#    print(DATE_ROW)
#    print(len(DATE_ROW[0]))
#    print(len(DATE_ROW[1]))

    NEWNAME = infile1.replace(".txt","_MERGE_"+filename2_No_Txt)
    FN = NEWNAME+".txt"
    Of = open(FN,"w+")
    for j in range(len(DATE_ROW[0])):
        for i in range(len(DATE_ROW)):
            if DATE_ROW[i][j] is None:
                continue
            else:
                Of.write("%s" %DATE_ROW[i][j])
                if(i != len(DATE_ROW)-1):
                    Of.write(" ")
                else:
                    Of.write("\n")

#        Of.write("%s " %DATE_ROW[0][j])
#        Of.write("%s\n" %DATE_ROW[1][j])
    Of.close()
    return FN

def formation(filename1,filename2): # it's the function which make file2 same format of file1

    if (filename1[0] == "/"):
        filename1 = filename1
    elif ((filename1[0] == "C") & (filename1[1] == ":")):
        filename1 = filename1
    else:
        filename1 = os.getcwd() + "/" + filename1  # get the path included filename
    loca1 = len(filename1)
    for i in range(1, len(filename1) + 1):  # find the "/" location
        if (filename1[-i] == "/"):
            loca1 = i - 1
            break
    FILENAME1 = filename1.replace(filename1[:-loca1], "")  # this is the shorten filename
    filename1_No_Txt = FILENAME1.replace(".txt", "")
    infile1 = filename1

    if (filename2[0] == "/"):
        filename2 = filename2
    elif ((filename2[0] == "C") & (filename2[1] == ":")):
        filename2 = filename2
    else:
        filename2 = os.getcwd() + "/" + filename2  # get the path included filename
    loca2 = len(filename2)
    for i in range(1, len(filename2) + 1):  # find the "/" location
        if (filename2[-i] == "/"):
            loca2 = i - 1
            break
    FILENAME2 = filename2.replace(filename2[:-loca2], "")  # this is the shorten filename
    filename2_No_Txt = FILENAME2.replace(".txt", "")
    infile2 = filename2

    DATE_ROW = MakeList_column(infile1)
    DATA_ROW = MakeList_column(infile2)

    form_date = DATE_ROW[0]
    data_date = DATA_ROW[0]
    list_amount = DATA_ROW[8]
    list_volume = DATA_ROW[7]
    ch_amount = []
    ch_volume = []
    j=1
    nones = 0
    for i in range(len(form_date)):
        if i == 0:
            ch_amount.append(list_amount[i])
            ch_volume.append(list_volume[i])
            continue
        else:
            while 1:
                if j>=(len(data_date)-1):
                    ch_amount.append(None)
                    ch_volume.append(None)
                    nones+=1
                    j = 1
                    break
                elif form_date[i] == data_date[j]:
                    a = list_amount[j].replace(',','')
                    b = list_volume[j].replace(',','')
                    ch_amount.append(a)
                    ch_volume.append(b)
                    break
                else:
                    j += 1
    NEWNAME = infile1.replace(".txt", "_Changed_" + filename2_No_Txt)
    FN = NEWNAME + ".txt"
    Of = open(FN, "w+")
    for j in range(len(ch_amount)):
        Of.write(str(ch_amount[j])+" "+str(ch_volume[j])+"\n")

    Of.close()
    return FN

def missing_value(filename1):
    if (filename1[0] == "/"):
        filename1 = filename1
    elif ((filename1[0] == "C") & (filename1[1] == ":")):
        filename1 = filename1
    else:
        filename1 = os.getcwd() + "/" + filename1  # get the path included filename
    loca1 = len(filename1)
    for i in range(1, len(filename1) + 1):  # find the "/" location
        if (filename1[-i] == "/"):
            loca1 = i - 1
            break
    FILENAME1 = filename1.replace(filename1[:-loca1], "")  # this is the shorten filename
    filename1_No_Txt = FILENAME1.replace(".txt", "")
    infile1 = filename1
    DATA_ROW = MakeList_column(infile1)
    arr_row = np.array(DATA_ROW)
    i,j=0,0
    print(len(arr_row),len(arr_row[0]))
    while i<=(len(arr_row)-1):
        while j<=(len(arr_row[0])-1):
            if arr_row[i][j] == 'None':
               # print(1)
                arr_row=np.delete(arr_row,j,axis=1)
            else:
                j += 1
        i += 1
        j = 0
    NEWNAME = infile1.replace(filename1_No_Txt+".txt", "missing_deleted_" + filename1_No_Txt)
    FN = NEWNAME + ".txt"
    Of = open(FN, "w+")
    for j in range(len(arr_row[0])):
        for i in range(len(arr_row)):
            if i == (len(arr_row)-1):
                Of.write(arr_row[i][j]+"\n")
            else:
                Of.write(arr_row[i][j]+" ")

    Of.close()
    return FN

    #arr_row[0]


#    print(data)


def main():
    INF1 = "C:/Users/manggny/PycharmProjects/Project-pre/data_txt/BEIJING_Aqi/carbon_copied_data/Aqi_Beijing.txt"
    dummy_INF2 = "C:/Users/manggny/PycharmProjects/Project-pre/func/300187.txt"
    INF2 = formation(INF1,dummy_INF2)
    OUTF = Merge(INF1,INF2)
    missing_value(OUTF)
    print(OUTF)

if __name__=="__main__":
    main()
