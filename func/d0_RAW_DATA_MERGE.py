#Author : JUNHO LEE
#This code is for Merge files. filename1 : DATA one column file, filename2 : Multi column DATA file
from d0_makelist_column import MakeList_column

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
            Of.write("%s" %DATE_ROW[i][j])
            if(i != len(DATE_ROW)-1):
                Of.write(" ")
            else:
                Of.write("\n")

#        Of.write("%s " %DATE_ROW[0][j])
#        Of.write("%s\n" %DATE_ROW[1][j])
    Of.close()
    return FN

def main():
    INF1 = "/Users/leejunho/Desktop/git/python3Env/group_study/ko_stats/data/SEOUL/ALL_DATA/FORMAT/NEW.txt"
    INF2 = "/Users/leejunho/Desktop/git/python3Env/group_study/ko_stats/data/SEOUL/ALL_DATA/FORMAT/WEATHER_new.txt"
    OUTF = Merge(INF1,INF2)
    print(OUTF)

if __name__=="__main__":
    main()
