import sys
import os

from d0_makelist import MakeList

def MakeList_column(filename):
    Row_List = MakeList(filename)
#    print(Row_List)
    Col_List = []
    for j in range(len(Row_List[0])):
        Temp_List=[]
        for i in range(len(Row_List)):
#            print(i)
            Temp_List.append(Row_List[i][j])
        Col_List.append(Temp_List)
#        print(Col_List)
    return Col_List

def main():
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi_re.txt"
    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/ALL_DATA/FORMAT/WIND.txt"
    col_list = MakeList_column(inputfile)
    print(col_list)

if __name__=="__main__":
    main()


