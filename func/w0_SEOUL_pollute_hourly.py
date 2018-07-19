# -*- coding: UTF-8 -*-
import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from w0_date_maker import DATE_MAKER

class SEOUL_AIR:

    def __init__(self):
        self.List_Write = []
        pass

    def AWAKE_BROWSER(self):
        self.driver1 = webdriver.Firefox()
        self.driver1.set_page_load_timeout(15)
        self.driver1.implicitly_wait(20)
        time.sleep(3)
        print("======================================================================")
        print("NEW Web Browser is Opened")
        print("======================================================================")

    def Try_BAIDU(self):
        try:
            self.driver1.get("https://www.baidu.com")
            time.sleep(1.5)
        except:
            print("BAIDU access failed")

    def Access_URL(self, URL):
        url_finish = 0
        TT = -1
        while url_finish == 0:
            TT = TT + 1
            #print(TT)
            print("            Now I am accessing to given URL, a second please...")
            try:
                if(TT<=3):
                    self.driver1.get(URL)
                    time.sleep(2)
                    try:
                        element = WebDriverWait(self.driver1,5+3*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"w120")))
                        url_finish = 1
                    except:
                        print("!@#!@#!")
                else:
                    self.driver1.refresh()
                    time.sleep(2)
                    element = WebDriverWait(self.driver1,5+2*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"w120")))
                    print("            Refreshing WEB page...")
                    time.sleep(2)
            except:
                print("            Accessing URL failed... Let's try again!")
        print("        Successfully accessed to given URL, Let's make DATA into given shape!")
        time.sleep(1.5)


    def Day_Date_maker(self,Month):
        if(Month<=9):
            return_value = "0" + str(Month)
            return return_value
        else:
            return str(Month)

    def Day_maker(self,Day):
        if(Day<=9):
            return_value = "0" + str(Day)
            return return_value
        else:
            return str(Day)

    def Hour_maker(self,Hour):
        if(Hour <= 9):
            return_value = "0" + str(Hour)
            return return_value
        else:
            return str(Hour)

    def Click_for_DATE(self, Init_year=2018, Init_Month=3, Init_Day=1):
        Need_LOADED = 0
        #DATE_class = DATE_MAKER()
        #DateList = DATE_class.DATE_MAKER(START_YEAR=Init_year,START_MONTH=Init_Month,START_DAY=Init_Day)
        
        while(Need_LOADED==0):
            try:
                Init_Month = self.Day_Date_maker(Init_Month)
                Init_Day = self.Day_Date_maker(Init_Day)
                #Time_Range_set = "//select[@name='sGroup']/option[@value='"+"TIME" + "']"
                #self.driver1.find_element_by_xpath(Time_Range_set).click()
                self.driver1.find_element_by_id("measure_cal2").clear()
                self.driver1.find_element_by_id("measure_cal2").send_keys(str(Init_year))
                self.driver1.find_element_by_id("measure_cal2Month").clear()
                self.driver1.find_element_by_id("measure_cal2Month").send_keys(str(Init_Month))
                self.driver1.find_element_by_id("measure_cal2Day").clear()
                self.driver1.find_element_by_id("measure_cal2Day").send_keys(str(Init_Day))
                self.driver1.find_element_by_class_name("schBtn1").click()
                Need_LOADED = 1
            except:
                TTT = input("[Need your help] Please make sure the page is successfully loaded... press 'Enter' to continue")
        print("    *Successfully searched the date!")
        print(" The Date is :", Init_year, Init_Month,Init_Day)
        time.sleep(1)

    def Click_for_Hour_n_write(self,Date):
        flag1 = 0
        rotation_flag = 1
        while True:
            if rotation_flag == 25:
                break
            try:
                Hour = self.Hour_maker(rotation_flag)
                Time_Range_set = "//select[@class='w70']/option[@value='"+Hour+"']"
                #print(Time_Range_set)
                message = "Crawling ON " + Hour + " O'Clock **"
                print(message) 
                self.driver1.find_element_by_xpath(Time_Range_set).click() 
                self.driver1.find_element_by_class_name("schBtn1").click(); time.sleep(0.2)
                Date_write = Date + Hour
                try:
                    element = WebDriverWait(self.driver1,5).until(EC.presence_of_element_located((By.CLASS_NAME,"w70")))
                    rotation_flag = rotation_flag + 1
                except:
                    print("!@#!@#!@#"); continue
#                self.Take_data_n_Write(DATE=Date_write,filename=outfilename) 
                self.List_Write.append(self.Take_data_n_Write(DATE=Date_write))
            except:
                flag1 = flag1 + 1
                if(flag1>10):
                    TTT = input("[Need your help] on Hour, Please make sure the page is successfully loaded... press 'Enter' to continue")
            print("    *Successfully searched the Hour!")
            time.sleep(0.2)
        return self.List_Write


    def CREATE_n_WRITE_INTO_TXT(self, outfileName, Write_LIST):
        filename = outfileName
        if(filename[0]=="/"):
            filename = filename
        elif((filename[0]=="C")&(filename[1]==":")):
            filename = filename
        elif(filename[0] == '~'):
            filename = filename.replace("~",os.environ['HOME'])
        else:
            filename = os.getcwd() + "/" + filename
        loca = len(filename)
        for i in range(1, len(filename)+1):
            if(filename[-i] == "/"):
                loca = i-1
                break
        FILENAME = filename.replace(filename[:-loca],"")
        filename_No_Txt = FILENAME.replace(".txt","")
        ofile = filename
        OF = open(ofile,"a+")
        for i in range(len(Write_LIST)):
            for j in range(len(Write_LIST[i])):
                if j==len(Write_LIST[i])-1:
                    OF.write("%s" %Write_LIST[i][j])
                    OF.write("\n")
                else:
                    OF.write("%s " %Write_LIST[i][j])
        OF.close()

    def Take_data_n_Write(self,DATE):
        DATA_LIST = []
        DATA_LIST.append(str(DATE))
        data = "//*[contains(@class,'num_color_')]"
        DATA = self.driver1.find_elements_by_xpath(data)
        for i in range(6):
            DATA_LIST.append(DATA[i].text)
        print(DATA_LIST)
        return DATA_LIST


    def QUIT(self):
        print("======================================================================")
        print("Closing Current Web Browser")
        print("======================================================================")
        print("\n")
        self.driver1.quit()

def main():
    air_seoul = SEOUL_AIR()
    air_seoul.AWAKE_BROWSER(); time.sleep(2)
    air_seoul.Access_URL("http://cleanair.seoul.go.kr/air_city.htm?method=measure&citySection=CITY"); time.sleep(2)
    DATE_class = DATE_MAKER()
    year = 2015
    month = 1
    day = 1
    refresh_flag = 0
    while(year<2016):  ## this might make one more additional day
        DateList = DATE_class.DATE_MAKER(START_YEAR=year,START_MONTH=month,START_DAY=day)
        air_seoul.Click_for_DATE(DateList[0],DateList[1],DateList[2]); time.sleep(1);
        #air_seoul.Take_data_n_Write(filename="/Users/leejunho/Desktop/git/python3Env/group_study/ko_stats/data/crawling/180101_Air_index.txt")
#        air_seoul.Take_data_n_Write(filename="Test1.txt")
        Date_info = str(DateList[0]) + air_seoul.Day_Date_maker(DateList[1]) + air_seoul.Day_maker(DateList[2])
        #print(Date_info)
        List_to_write = air_seoul.Click_for_Hour_n_write(Date = Date_info)#,outfilename="2008start_hourly.txt")
        print(List_to_write)
        year = DateList[0]
        month = DateList[1]
        day = DateList[2] + 1
        if(refresh_flag >=1):
            air_seoul.CREATE_n_WRITE_INTO_TXT(outfileName="2015start_hourly.txt", Write_LIST=List_to_write)
            air_seoul.List_Write=[]
            air_seoul.Try_BAIDU()
            air_seoul.Access_URL("http://cleanair.seoul.go.kr/air_city.htm?method=measure&citySection=CITY"); time.sleep(2)
            refresh_flag = 0
        refresh_flag = refresh_flag + 1

 
    #air_seoul.Click_for_DATE(); time.sleep(1); 
    #air_seoul.Take_data_n_Write()

    air_seoul.QUIT()

if __name__=="__main__":
    main()

