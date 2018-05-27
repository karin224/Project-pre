import sys, os
from date_maker import DATE_MAKER
from c0_READ_PATH_FILE import read_file_name
from d0_makelist import MakeList
from c0_Make_txt_from_Raw_list import MAKE_TXT

def ADD_daily_date_FirstLine(START_YEAR=1996,START_MONTH=1,START_DAY=1, infilename="daily_test.txt"):
    filename_list = read_file_name(infilename)
    infile = filename_list[2]
    outfile = infile; outfile = outfile.replace(".txt","")
    outfile = outfile + "_Daily.txt"
    year = START_YEAR
    month = START_MONTH
    day = START_DAY
    DATE_class = DATE_MAKER()
    Daily_date_list = []; Daily_date_list.append("DATE")
    for i in range(8036):
        DATE_num = DATE_class.DATE_MAKER(year,month,day)
        DATE_str = DATE_class.MAKE_DATE_STR(DATE_num)
#        print(DATE_str[3])
        Daily_date_list.append(DATE_str[3])
        year= DATE_num[0]
        month = DATE_num[1]
        day = DATE_num[2]+1
    Origin_row_list = MakeList(infile)
#    print(Origin_row_list)
    return_list = []
    for i in range(len(Origin_row_list)):
        temp_list = []
        temp_list.append(Daily_date_list[i])
        for j in range(len(Origin_row_list[0])):
            temp_list.append(Origin_row_list[i][j])
        return_list.append(temp_list)
    MAKE_TXT(return_list,outfile)        
#    print(return_list)
    print("created file name : ", outfile)
    return outfile



def MakeMonthlyDate_BaseOnDailyDate(infilename = "test.txt"):
    filename_list = read_file_name(infilename)
    infile = filename_list[2]
    outfile = infile; outfile = outfile.replace(".txt","")
    outfile = outfile.replace("_Daily","")
    outfile = outfile + "_Monthly.txt"
#    print(outfile)
    row_list = MakeList(infile)
    return_list = []; return_list.append(row_list[0])
    refresh_date_flag=1
    for i in range(len(row_list)):
        temp_list = [] 
        if(i==0):
            continue
        if((i==1) | (refresh_date_flag==0)):
            first_list = []
            iterated_num = 1
            month_date = row_list[i][0][:6]
            refresh_date_flag=1
            temp_list.append(month_date)
            for j in range((len(row_list[0])-1)):
                temp_list.append(row_list[i][j+1])
            first_list = temp_list
#            print(first_list)    
            continue
             
        if(row_list[i][0][:6] == month_date):
            for j in range((len(row_list[0]))):
                if(j==0):
                    temp_list.append(row_list[i][0][:6])
                else:
                    calc = float(first_list[j])+float(row_list[i][j]); #calc = "%0.3f"%calc; str_calc = str(calc)
                    temp_list.append(calc)
            first_list = temp_list
            iterated_num = iterated_num+1
#            print(first_list)

        if((i==len(row_list)-1)):
            return_temp_list = []
            for k in range(len(first_list)):
                if k==0:
                    return_temp_list.append(first_list[0])
                else:
                    calc = float(first_list[k]) / float(iterated_num); calc = "%0.4f"%calc; str_calc = str(calc)
                    return_temp_list.append(str_calc)
            return_list.append(return_temp_list)
            break
 
        if(row_list[i+1][0][:6] != month_date):
            return_temp_list = []
            refresh_date_flag=0
            for k in range(len(first_list)):
                if k==0:
                    return_temp_list.append(first_list[0])
                else:
                    calc = float(first_list[k]) / float(iterated_num); calc = "%0.4f"%calc; str_calc = str(calc)
                    return_temp_list.append(str_calc)
            return_list.append(return_temp_list)
#    print(return_list)
    MAKE_TXT(return_list,outfile)
    print("created file name : ", outfile)
    return outfile




def main():
    inputfilename = "/Users/leejunho/Desktop/git/python3Env/group_study/ko_stats/data/SEOUL/ALL_DATA/Since96_17Y.txt"
    Outfile = ADD_daily_date_FirstLine(1996,1,1,inputfilename)
    Outfile = "/Users/leejunho/Desktop/git/python3Env/group_study/ko_stats/data/SEOUL/ALL_DATA/Since96_17Y_Daily.txt"
    MakeMonthlyDate_BaseOnDailyDate(Outfile)


if __name__=="__main__":
    main()
