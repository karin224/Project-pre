import os, sys

class DATE_MAKER:
    def __init__(self):
        pass

    def DATE_MAKER(self,START_YEAR=2018,START_MONTH=5,START_DAY=7,INTERVAL=1):
        s_day = START_DAY
        s_month = START_MONTH
        s_year = START_YEAR
        e_day = START_DAY + INTERVAL
        e_month = START_MONTH
        e_year = START_YEAR
        if( (s_day >31 ) & ((START_MONTH ==1) | (START_MONTH ==3) | (START_MONTH ==5) | (START_MONTH ==7) | (START_MONTH ==8) | (START_MONTH ==10) | (START_MONTH ==12))):
            s_day = s_day-31
            s_month = s_month + 1
            if(s_month > 12):
                s_month = s_month - 12
                s_year = s_year + 1
        elif( (s_day >30 ) & ((START_MONTH ==4)|(START_MONTH ==6)|(START_MONTH ==9)|(START_MONTH ==11))):
            s_day = s_day-30
            s_month = s_month + 1
            if(s_month > 12):
                s_month = s_month - 12
                s_year = s_year + 1
        elif( (s_day >29) & (START_MONTH ==2) & (START_YEAR%4 == 0)   ):
            s_day = s_day-29
            s_month = s_month + 1
#            print("***********************************************")
        elif((s_day >28) & (START_MONTH ==2) & (START_YEAR%4 != 0) ):
            s_day = s_day-28
            s_month = s_month + 1
#            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"); print(START_YEAR%4)
        else:
            pass
        if( (e_day >31 ) & ((START_MONTH ==1) | (START_MONTH ==3) | (START_MONTH ==5) | (START_MONTH ==7) | (START_MONTH ==8) | (START_MONTH ==10) | (START_MONTH ==12))):
            e_day = e_day -31
            e_month = e_month + 1
            if(e_month > 12):
                e_month = e_month -12
                e_year = e_year + 1
        elif((e_day >30 ) & ((START_MONTH ==4)|(START_MONTH ==6)|(START_MONTH ==9)|(START_MONTH ==11))):
            e_day = e_day -30
            e_month = e_month + 1
        elif((e_day >29 ) & (START_MONTH ==2) & (START_YEAR%4 == 0)   ):
            e_day = e_day -29
            e_month = e_month + 1
        elif((e_day >28) & (START_MONTH ==2) & (START_YEAR%4 != 0)):
            e_day = e_day -28
            e_month = e_month + 1
        else:
            pass
        self.datelist = [s_year, s_month, s_day, e_year, e_month, e_day]
        return [s_year, s_month, s_day, e_year, e_month, e_day]

    def MAKE_DATE_STR(self,DATE_LIST_INPUT):
        DATE_LIST = DATE_LIST_INPUT
        str_s_year = str(DATE_LIST[0]); str_e_year = str(DATE_LIST[3]);
        if(DATE_LIST[1] <=9):
            str_s_month = str(0) + str(DATE_LIST[1])
        else:
            str_s_month = str(DATE_LIST[1])
        if(DATE_LIST[2] <=9):
            str_s_day = str(0) + str(DATE_LIST[2])
        else:
            str_s_day = str(DATE_LIST[2])
        if(DATE_LIST[4] <=9):
            str_e_month = str(0) + str(DATE_LIST[4])
        else:
            str_e_month = str(DATE_LIST[4])
        if(DATE_LIST[5] <=9):
            str_e_day = str(0) + str(DATE_LIST[5])
        else:
            str_e_day = str(DATE_LIST[5])
        startDATE = str_s_year + "-" + str_s_month + "-" + str_s_day
        endDATE   = str_e_year + "-" + str_e_month + "-" + str_e_day
        RE_DATE = startDATE + ":" + startDATE
        END_DATE_FOR_TXT = str_s_year + str_s_month + str_s_day
        END_DATE_FOR_TXT2 = str_e_year + str_e_month + str_e_day
        return [startDATE,endDATE,RE_DATE,END_DATE_FOR_TXT,END_DATE_FOR_TXT2]


