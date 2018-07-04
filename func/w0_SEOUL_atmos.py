# -*- coding: UTF-8 -*-
import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SEOUL_AIR:
 
    def __init__(self):
        pass

    def AWAKE_BROWSER(self):
        self.driver1 = webdriver.Firefox()
        self.driver1.set_page_load_timeout(15)
        self.driver1.implicitly_wait(20)
        time.sleep(3)
        print("======================================================================")
        print("NEW Web Browser is Opened")
        print("======================================================================")

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
                        element = WebDriverWait(self.driver1,5+3*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"w60")))
                        url_finish = 1 
                    except:
                        print("!@#!@#!")
                else:
                    self.driver1.refresh()
                    time.sleep(2)
                    element = WebDriverWait(self.driver1,5+2*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"w60")))
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

    def Click_for_DATE(self, Init_year=1996, Init_Month=1, KEY_WORD="CO"):
        self.keyword = KEY_WORD
        Need_LOADED = 0
        while(Need_LOADED==0):
            try:
                Init_Month = self.Day_Date_maker(Init_Month)
                init_year = "//select[@name='lGroup']/option[@value='"+str(Init_year) + "']"
                self.driver1.find_element_by_xpath(init_year).click()
                init_month = "//select[@name='ssGroup']/option[@value='"+str(Init_Month)+"']"
                self.driver1.find_element_by_xpath(init_month).click()
                key_word = "//select[@name='mGroup']/option[@value='"+KEY_WORD+"']"
                self.driver1.find_element_by_xpath(key_word).click()
                self.driver1.find_element_by_class_name("schBtn1").click()
                Need_LOADED = 1
            except:
                TTT = input("[Nedd your help] Please make sure the page is successfully loaded... press 'Enter' to continue")
        print("    *Successfully searched the date!")
        print(" The Date is :", Init_year, Init_Month)
        time.sleep(2)

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
            OF.write("%s\n" %Write_LIST[i])
        OF.close()

    def Take_data_n_Write(self, filename="test.txt"):
        data = self.driver1.find_element_by_class_name("ft_b.ft_point8")
        DATA = data.text
        DATA = DATA[7:]
        temp_list = DATA.split()
        TEMP_list = []; DATA_list = []
        for i in range(len(temp_list)):
            TEMP_list.append(float(temp_list[i]))
        for i in range(len(TEMP_list)):
            DATA_list.append(str(TEMP_list[i]))
        print("    *Days included of this month :", len(DATA_list))
        self.CREATE_n_WRITE_INTO_TXT(outfileName=filename, Write_LIST=DATA_list)


    def QUIT(self):
        print("======================================================================")
        print("Closing Current Web Browser")
        print("======================================================================")
        print("\n")
        self.driver1.quit()


def main():
    air_seoul = SEOUL_AIR()
    air_seoul.AWAKE_BROWSER(); time.sleep(2)
    air_seoul.Access_URL("http://cleanair.seoul.go.kr/air_pollution.htm?method=daily"); time.sleep(2)

    year = 2010
    month= 1
    keyword = "O3"  # O3, PM10, PM25, NO2, CO, SO2
    while(year<2018):
        air_seoul.Click_for_DATE(year,month,keyword)
        air_seoul.Take_data_n_Write(filename="/Users/leejunho/Desktop/SSS_test.txt")
        month = month + 1
        if(month>12):
            month = 1
            year = year + 1
    air_seoul.QUIT()

if __name__=="__main__":
    main()

