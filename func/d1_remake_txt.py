import os, sys

# Need to input RAW DATA!!!
def MakeTXT(filename):
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
    infile = filename


    ff = open(infile,"r")
    FILE_LIST = []
    for line in ff:
        FILE_LIST.append(line.split())
    ff.close()
    '''    
    for i in range(FILE_LIST):
        for j in range(FILE_LIST[i]):
            FILE_LIST[i][j] =  
    '''
    LEN = len(FILE_LIST)
    clen = len(FILE_LIST[0])
    KLIST = []
    for i in range(LEN):
        if((len(FILE_LIST[i])==1) & (FILE_LIST[i][0]=='\x00')):
            pass
        else:
            KLIST.append(FILE_LIST[i])

    LEN = len(KLIST)
    KKLIST = []
    for i in range(LEN):
        for j in range(len(KLIST[i])):
            KLIST[i][j] = KLIST[i][j].replace('\x00',"")
            KLIST[i][j] = KLIST[i][j].replace('\xff\xfe','')
        KKLIST.append(KLIST[i])

    for i in range(len(KKLIST)):
        KKLIST[i] = list(filter(None,KKLIST[i]))

    FN = infile.replace(".txt","R.txt")
    Of = open(FN,"w+")
    for i in range(len(KKLIST)):
        for j in range(len(KKLIST[i])):
            Of.write("%s" %KKLIST[i][j])
            if(j!=len(KKLIST[i])-1):
                Of.write(" ")
            if(j==len(KKLIST[i])-1):
                Of.write("\n")
    Of.close()
 

    return FN
    

def main():
    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_day.txt"
    con_list = MakeTXT(inputfile)
    print(con_list)

if __name__=="__main__":
    main()






