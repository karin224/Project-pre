import sys
import os
from d0_counting_in_specific_range import Counting
from d0_makelist_column import MakeList_column
from d0_min_max_except_index0 import min_max_range

def Converting(filename, NBINS=100):
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

    OUPUT_TXT_LIST = []
    Col_List = MakeList_column(infile)
    for i in range(len(Col_List)):
        HIST_RANGE = min_max_range(Col_List[i])
        print(HIST_RANGE)
        SAVENAME = os.getcwd()+"/"+filename_No_Txt+"_"+Col_List[i][0]+"_py.txt"; #print(SAVENAME)
        ff = open(SAVENAME,"w+")
        OUPUT_TXT_LIST.append(SAVENAME)
        FLAG = (HIST_RANGE[3] - HIST_RANGE[2])/float(NBINS)
        for j in range(NBINS):
            COUNT_NUM = Counting(Col_List[i],[HIST_RANGE[2]+FLAG*(j),HIST_RANGE[2]+FLAG*(j+1)])
            ff.write("%i %f %f %f\n" %(j+1,HIST_RANGE[2]+FLAG*(j),HIST_RANGE[2]+FLAG*(j+1),COUNT_NUM))
 

        ff.close()


    return OUPUT_TXT_LIST

def main():
    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi_re.txt"
    List_name_of_files = Converting(inputfile,NBINS=20)
    print(List_name_of_files)


if __name__=="__main__":
    main()


