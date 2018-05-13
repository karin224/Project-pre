import sys, os
sys.path.append("../../../func/")
from d0_makelist_column import MakeList_column

infile = "../Aqi_Beijing_Weather.txt"
#infile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/carbon_copied_data/n0_basic_day/Aqi_Beijing_Holi_re.txt"
COL_List = MakeList_column(infile)
Of = open("FORMAT.txt","w+")
for i in range(len(COL_List[0])):
    Of.write("%s\n" %COL_List[0][i])
    
Of.close()
