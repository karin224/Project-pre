import sys
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from d0_makelist import MakeList

#infile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_day.txt"
infile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/carbon_copied_data/Aqi_Beijing_HOLI_byej.txt"

CLIST = MakeList(infile)
LEN = len(CLIST)
clen = len(CLIST[0])
print(CLIST)
print("Total Line Number of input file :",LEN)
print ("For each line, should be ",clen, "lines.")



for i in range(len(CLIST)):
    if(clen != len(CLIST[i])):
        print("!!! On", i, "th line number, NOT EQUAL COLUMNS, ERROR !!!")
        break
    else:
        if(i==0):
            continue
        else:
            for j in range(len(CLIST[i])):
                try:
                    temp = float(CLIST[i][j])
                except:
                    ValueError
                    print(i)
                    break


print("...end of the process...")



