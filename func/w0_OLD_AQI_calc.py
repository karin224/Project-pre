# -*- coding: UTF-8 -*-
import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

class AQI_CALC:

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
                        element = WebDriverWait(self.driver1,5+3*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"ui-state-default.ui-corner-top")))
                        url_finish = 1
                    except:
                        print("!@#!@#!")
                else:
                    self.driver1.refresh()
                    time.sleep(2)
                    element = WebDriverWait(self.driver1,5+2*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"ui-state-default.ui-corner-top")))
                    print("            Refreshing WEB page...")
                    time.sleep(2)
            except:
                print("            Accessing URL failed... Let's try again!")
        print("        Successfully accessed to given URL, Let's make DATA into given shape!")
        time.sleep(1.5)


    def Click_for_DATA(self):
        Try_multi = 0        
        Need_LOADED = 0
        while(Need_LOADED==0):
            try:
                Try_multi = Try_multi + 1
                self.driver1.find_element_by_id("conc").click(); time.sleep(0.8)
                TTT = input("[Nedd your help] '111', after selecting a pollutant\n")
                #self.driver1.find_element_by_name('pollutant').click()
                #select = Select(self.driver1.find_element_by_name('pollutant'))
                #print(select)
                #Temp_select = select.select_by_value('1'); #Select.click(); 
                #print(Temp_select)
                Need_LOADED = 1
            except:
                if(Try_multi > 2):
                    TTT = input("[Need your help] Please make sure the page is successfully loaded... press 'Enter' to continue")
                    Need_LOADED = 1
                else:
                    continue
        print("    *Successfully searched the date!")
        time.sleep(2)

    def Input_Data(self,DATA):
        self.driver1.find_elements_by_name("inputbox")[1].send_keys(DATA)
        self.driver1.find_elements_by_name("Calculate")[1].click()

    def Read_out_DATA(self):
        output = self.driver1.find_elements_by_name("outputbox1")[1]
        #print(output.value)


    def QUIT(self):
        print("======================================================================")
        print("Closing Current Web Browser")
        print("======================================================================")
        print("\n")
        self.driver1.quit()




def main():
    AQI = AQI_CALC()
    AQI.AWAKE_BROWSER(); time.sleep(2)
    AQI.Access_URL("https://www.airnow.gov/index.cfm?action=airnow.calculator")
    AQI.Click_for_DATA()
    AQI.Input_Data('100')
    AQI.Read_out_DATA()

    time.sleep(2)
    AQI.QUIT()

if __name__=="__main__":
    main()




