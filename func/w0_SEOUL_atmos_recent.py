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

    def Click_for_DATE(self, Init_year=2018, Init_Month=3, Init_Day=1,KEY_WORD="CO"):
        self.keyword = KEY_WORD
        Need_LOADED = 0
        while(Need_LOADED==0):
            try:
                Init_Month = self.Day_Date_maker(Init_Month)
                Time_Range_set = "//select[@name='sGroup']/option[@value='"+"DAY" + "']"
                self.driver1.find_element_by_xpath(Time_Range_set).click()
                self.driver1.find_element_by_id("measure_cal2").clear()
                self.driver1.find_element_by_id("measure_cal2").send_keys(str(Init_year))
                self.driver1.find_element_by_id("measure_cal2Month").clear()
                self.driver1.find_element_by_id("measure_cal2Month").send_keys(str(Init_Month))
                self.driver1.find_element_by_class_name("schBtn1").click()
                Need_LOADED = 1
            except:
                TTT = input("[Nedd your help] Please make sure the page is successfully loaded... press 'Enter' to continue")
        print("    *Successfully searched the date!")
        print(" The Date is :", Init_year, Init_Month)
        time.sleep(2)


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
    air_seoul.Click_for_DATE(); time.sleep(3)
    air_seoul.QUIT()

if __name__=="__main__":
    main()

