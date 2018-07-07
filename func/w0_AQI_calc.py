# -*- coding: UTF-8 -*-
import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from d0_makelist_column import MakeList_column

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
                        element = WebDriverWait(self.driver1,5+3*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"polselectiontr")))
                        url_finish = 1
                    except:
                        print("!@#!@#!")
                else:
                    self.driver1.refresh()
                    time.sleep(2)
                    element = WebDriverWait(self.driver1,5+2*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"polselectiontr")))
                    print("            Refreshing WEB page...")
                    time.sleep(2)
            except:
                print("            Accessing URL failed... Let's try again!")
        print("        Successfully accessed to given URL, Let's make DATA into given shape!")
        time.sleep(1.5)


    def Click_for_DATA(self):
        TTT = input("[Nedd your help] '111', after selecting a pollutant\n"); time.sleep(1)
#        ITEMs = self.driver1.find_elements_by_class_name('polselectiontr')
#        ITEMs =  self.driver1.find_element_by_xpath("//tr[td='Particulate <2.5 microns ']")
#        print(ITEMs); #print(len(ITEMs))
#        ITEMs.click()
        #tt = ITEMs[1].tr
        #for i in range(8):
        #    ITEMs[i].click()
        #    time.sleep(0.3)



    def Input_value(self,INPUT):
        self.driver1.find_element_by_class_name("polvalue").clear()
        self.driver1.find_element_by_class_name("polvalue").send_keys(INPUT)
        time.sleep(0.5)

    def Output_DATA(self):
        #outData = self.driver1.find_element_by_id("helptexteffect")
#        OutData = self.driver1.find_element_by_xpath("//div[@id='helptexteffect']/span[@id='aqival']")
        OutData = self.driver1.find_element_by_xpath("//div[@id='helptexteffect']")
        for i in range(len(OutData.text)):
            if(OutData.text[i] == '\n'):
                num = i
                break
        OUTDATA = (OutData.text)[5:num]
        #print(OUTDATA)
        return OUTDATA

    def CREATE_n_WRITE_INTO_TXT(self,outfileName, Write_LIST):
        ofile = outfileName
        OF = open(ofile,"w+")
        for i in range(len(Write_LIST[0])):
            for j in range(len(Write_LIST)):
                if j == (len(Write_LIST)-1):
                    OF.write("%s\n" %str(int(Write_LIST[j][i])))
                OF.write("%s " %str(int(Write_LIST[j][i])))

#            for j in range(len(Write_LIST[i])):
#                if j==(len(Write_LIST[i])-1):
#                    OF.write("%s\n" %str(int(Write_LIST[i][j])))
#                OF.write("%s " %str(int(Write_LIST[i][j])))
        OF.close()



    def QUIT(self):
        print("======================================================================")
        print("Closing Current Web Browser")
        print("======================================================================")
        print("\n")
        self.driver1.quit()


def main():
    AQI = AQI_CALC()
    AQI.AWAKE_BROWSER()
    AQI.Access_URL(URL="http://aqicn.org/calculator/kr/")
    #AQI.Click_for_DATA()
    col_list = MakeList_column("/Users/leejunho/Desktop/git/python3Env/group_study/NOT_USUALLY_VISIT/statistic_group_study/R_language/test/SEOUL_Day_R_P.txt")
    Write_list = []
    for i in range(1,2): 
        if i==0:
            print("choose PM2.5") 
            OUT_NAME = "PM2p5"
        elif i==1:
            print("choose PM10")
            OUT_NAME = "PM10"
        elif i==2:
            print("choose O3(8hr)")
            OUT_NAME = "O3"
        elif i==3:
            print("choose SO2(1hr)")
            OUT_NAME = "SO2"
        elif i==4:
            print("choose NO2")
            OUT_NAME = "NO2"
        elif i==5:
            print("choose CO")
            OUT_NAME = "CO"

        AQI.Click_for_DATA()
        temp_list = []
        for j in range(len(col_list[i])):
#        for j in range(10):
            if(j==0):
                continue
            AQI.Input_value(col_list[i][j])
            DATA_out = AQI.Output_DATA()
            DATA_out = float(DATA_out)
            print(j, DATA_out)
            temp_list.append(DATA_out)
        Write_list.append(temp_list)

    outfile = "/Users/leejunho/Desktop/git/python3Env/group_study/NOT_USUALLY_VISIT/statistic_group_study/R_language/test/AQI_PM10.txt" 
    AQI.CREATE_n_WRITE_INTO_TXT(outfileName=outfile,Write_LIST=Write_list)
#    AQI.Input_value('100') 
    AQI.Output_DATA() 


if __name__=="__main__":
    main()



