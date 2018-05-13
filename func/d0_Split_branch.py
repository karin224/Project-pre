import sys

from d0_makelist import *
from d0_makelist_column import *

def show_branch(filename1):
    if(filename1[0]=="/"):
        filename1 = filename1
    elif(filename1[0] == '~'):
        filename1 = filename1.replace("~",os.environ['HOME'])
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
    print(infile1)

    RawList = MakeList(infile1)
    RawList_c = MakeList_column(infile1)
    num = 1

    print("Which branch do you want to extract? (Press 'q' to stop slecting)")
    for j in RawList[0]:
        print(num,":",j,"",end="\n")
        num = num + 1

    #print("Please input branch name you want to extract")
    List_c = []

    print("Please input Branch Name(not branch number)!")
    for i in range(len(RawList[0])):
        print("Branch Name (Press 'q' to stop slecting): ", end='')
        Branch_name = input()
        if Branch_name in RawList[0]:
            index_num = 0
            for j in RawList[0]:
                if j == Branch_name:
                    List_c.append(RawList_c[index_num])
                    #print(List_c)
                    break
                else:
                    index_num = index_num + 1
                    #print(index_num)
        elif Branch_name not in RawList[0] and Branch_name != "q":
            print("There are no such branches!")
        elif Branch_name == "q":
            break

    FN = infile1.replace(".txt", "_P.txt")
    Of = open(FN, "w+")
    for i in range(len(RawList)):
        for j in range(len(List_c)):
            Of.write("%s" %List_c[j][i])
            if(j!=len(List_c)-1):
                Of.write(" ")
            if(j==len(List_c)-1):
                Of.write("\n")
    Of.close()
    return FN

def main():
    infile = "../data_txt/BEIJING_Aqi/Aqi_Beijing_Holi.txt"
    outfile = show_branch(infile)
    print(outfile)

if __name__=="__main__":
    main()
#show_branch("../data_txt/BEIJING_Aqi/Aqi_Beijing.txt")
