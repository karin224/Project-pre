#Author : Soomin Lee
import sys
sys.path.append("/home/soomin/Desktop/group_study/Project-pre/func")
from c0_READ_PATH_FILE import read_file_name
from d0_makelist_column import MakeList_column

def Month_divide(filename):
    FILE = read_file_name(filename)
    infile1 = FILE[2]
    OUTPUT_PATH = FILE[3]+FILE[0]
    COL_LIST1 = MakeList_column(infile1)

    #print(COL_LIST1)

    M_LIST=[]

    for k in range(len(COL_LIST1[0])):
        gg = []
        for m in range(len(COL_LIST1)):
            gg.append(COL_LIST1[m][k])
    
        M_LIST.append(gg)
    #    if k==0:
    #        continue

    #print(M_LIST)

    RETURN_LIST = []
    bb = []
    for a in range(len(M_LIST)):
    #    aa=[]
    #    aa.append(M_LIST[a])
        if a>1 and (float(M_LIST[a][0])-float(M_LIST[a-1][0]))>1:
            #print(bb)
            FN="M"+str(int(M_LIST[a-1][0])//100)+".txt"
            FN = OUTPUT_PATH+"_"+FN
            RETURN_LIST.append(FN)
            Of = open(FN,"w+")
            for i in range(len(bb)):
                for j in range(len(bb[i])):
                    Of.write("%s" %bb[i][j])
                    if(j!=len(bb[i])-1):
                        Of.write(" ")
                    if(j==len(bb[i])-1):
                        Of.write("\n")
            Of.close()
            bb = []
            bb.append(M_LIST[0])
            cc = bb
        bb.append(M_LIST[a])
    #    print(bb)
    #print(bb)    
    #print(cc)
    FN="M"+str(int(cc[1][0])//100)+".txt"
    FN = OUTPUT_PATH+"_"+FN
    Of = open(FN,"w+")
    for i in range(len(cc)):
        for j in range(len(cc[i])):
            Of.write("%s" %cc[i][j])
            if(j!=len(cc[i])-1):
                Of.write(" ")
            if(j==len(cc[i])-1):
                Of.write("\n")
    Of.close()
    RETURN_LIST.append(FN)
    return RETURN_LIST


def main():
    inputfile = "../data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi.txt"
    FileNameList = Month_divide(inputfile)
    print(FileNameList)

if __name__ =="__main__":
    main()
