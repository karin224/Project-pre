#Author Junho Lee
#This is for removing "outliers"
import os, sys, math
from d0_makelist import MakeList
from d0_makelist_column import MakeList_column
from d0_basic_statistic import d0_exclude_1_mean, d0_exclude_1_STD, d0_exclude_1_variance

def N_sigma_skimming(filename, N_Of_Sigma=5):
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

    ROW_list = MakeList(infile)
    COL_list = MakeList_column(infile)
 
    Mean_list = list()
    Std_list = list()
#    VAR_list = list()
    Name_list = list()
    for i in range(len(COL_list)):
        Name_list.append(COL_list[i][0])
        Mean_list.append(d0_exclude_1_mean((COL_list[i])))    
#        VAR_list.append(d0_exclude_1_variance((COL_list[i])))
        Std_list.append(d0_exclude_1_STD((COL_list[i])))
#    print(Name_list)
#    print(Mean_list)
    '''
    RE_COL_LIST = []
    for i in range(len(COL_list)): 
        if((COL_list[i][0] == DATE) | (COL_list[i][0] == HOLI) | (COL_list[i][0] == DAYS)): 
            continue
        L_NSIGMA = Mean_list[i] - N_Of_Sigma*Std_list[i]
        H_NSIGMA = Mean_list[i] + N_Of_Sigma*Std_list[i]
        
        for j in range(len(COL_list[i])):
    '''            
    ttt=0
    RE_ROW_LIST = []
    for i in range(len(ROW_list)):
        if(i==0):
            RE_ROW_LIST.append(ROW_list[i])
            continue
        for j in range(len(ROW_list[i])):
            if(((Name_list[j]=="DATE") | (Name_list[j]=="HOLI") | (Name_list[j]=="DAYS")) & (j!=(len(ROW_list[i])-1)) ):
                continue
            L_NSIGMA = Mean_list[j] - N_Of_Sigma*Std_list[j]
            H_NSIGMA = Mean_list[j] + N_Of_Sigma*Std_list[j]
#            print(L_NSIGMA, H_NSIGMA)
            if((j==(len(ROW_list[i])-1)) & ((Name_list[j]=="DATE") | (Name_list[j]=="HOLI") | (Name_list[j]=="DAYS")) ):
                RE_ROW_LIST.append(ROW_list[i])
            elif( (float(ROW_list[i][j])>L_NSIGMA) & (float(ROW_list[i][j])<H_NSIGMA)):
                if(j==(len(ROW_list[i])-1)):
                    RE_ROW_LIST.append(ROW_list[i])
                else:
                    continue
            else:
                ttt = ttt+1
                break
#    print(ttt)
#    print(RE_ROW_LIST)

    FN = infile.replace(".txt","S.txt")
    Of = open(FN,"w+")
    for i in range(len(RE_ROW_LIST)):
        for j in range(len(RE_ROW_LIST[i])):
            Of.write("%s" %RE_ROW_LIST[i][j])
            if(j!=len(RE_ROW_LIST[i])-1):
                Of.write(" ")
            if(j==len(RE_ROW_LIST[i])-1):
                Of.write("\n")
    Of.close()
#    print(FN)
    return FN


def main():
    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/carbon_copied_data/Aqi_Beijing_day_re.txt"
    Skim_txt = N_sigma_skimming(inputfile,N_Of_Sigma=5)
    print(Skim_txt)

if __name__=="__main__":
    main()

