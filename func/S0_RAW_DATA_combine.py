import sys
sys.path.append("/home/soomin/Desktop/group_study/Project-pre/func")

from d0_makelist_column import MakeList_column

#infile1 = "test1.txt"
#infile2 = "test2.txt"

def ROW_COL(filename1, filename2):
    
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



    COL_LIST1 = MakeList_column(infile1)
    COL_LIST2 = MakeList_column(infile2)
    COL_LIST1.append(COL_LIST2[1])
    COL_LIST3=COL_LIST1

#    print(COL_LIST3)

    ROW_LIST4=[]

    for k in range(len(COL_LIST3[0])):
        gg=[]
        for m in range(len(COL_LIST3)):
            gg.append(COL_LIST3[m][k])

        ROW_LIST4.append(gg)
#    print(ROW_LIST4)

    NEWNAME = infile1.replace(".txt","_"+filename2_No_Txt)
    FN = NEWNAME+".txt"
    Of = open(FN,"w+")
    for i in range(len(ROW_LIST4)):
        for j in range(len(ROW_LIST4[i])):
            Of.write("%s" %ROW_LIST4[i][j])
            if(j!=len(ROW_LIST4[i])-1):
                Of.write(" ")
            if(j==len(ROW_LIST4[i])-1):
                Of.write("\n")
    Of.close()


    return FN


def main():
#    INFILE1 = "test1.txt"
#    INFILE2 = "test2.txt"
    INFILE1 = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/ALL_DATA/OLD_180420_Aqi_Beijing_Weather.txt"
    INFILE2 = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/ALL_DATA/FORMAT/WIND.txt"
    output = ROW_COL(INFILE1, INFILE2)
    print(output)

if __name__=="__main__":
    main()


