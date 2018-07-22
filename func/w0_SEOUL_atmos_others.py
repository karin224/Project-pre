# -*- coding: UTF-8 -*-
import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from w0_date_maker import DATE_MAKER


### Humidity, wind_speed
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
                if(TT<=5):
                    self.driver1.get(URL)
                    time.sleep(2+TT)
                    try:
                        element = WebDriverWait(self.driver1,5+3*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"table_develop")))
                        url_finish = 1
                    except:
                        print("!@#!@#!")
                else:
                    self.driver1.refresh()
                    time.sleep(0.5)
                    #element = WebDriverWait(self.driver1,5+2*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"table_develop")))
                    print("            Refreshing WEB page...")
                    time.sleep(3)
            except:
                print("            Accessing URL failed... Let's try again!")
        print("        Successfully accessed to given URL, Let's make DATA into given shape!")
        time.sleep(1.5)

    def Click_for_DATE(self, Init_year=1996):
        Need_LOADED = 0
        while(Need_LOADED==0):
            try:
                init_year = "//select[@name='yy']/option[@value='"+str(Init_year) + "']"
                self.driver1.find_element_by_xpath(init_year).click()
                self.driver1.find_element_by_class_name("btn").click()
                Need_LOADED = 1
            except:
                TTT = input("[Nedd your help] Please make sure the page is successfully loaded... press 'Enter' to continue")
        print("    *Successfully searched the date!")
        print(" The Date is :", Init_year)
        time.sleep(2)

    def Take_data_n_Write(self, filename="test.txt"):
        #data = "//*[contains(@class,'table_develop')]"
        #DATA = self.driver1.find_elements_by_xpath(data)
        #print(DATA)
        #print(DATA[0].text)
        url_finish = 0
        TT = -1
        while url_finish == 0:
            TT = TT + 1
            #print(TT)
            print("    Now I am accessing to given URL, a second please...")
            try:
                if(TT<=5):
                    time.sleep(2+TT)
                    try:
                        element = WebDriverWait(self.driver1,5+3*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"table_develop")))
                        url_finish = 1
                        data = self.driver1.find_element_by_class_name("table_develop")
                    except:
                        print("!@#!@#!")
                else:
                    self.driver1.refresh()
                    time.sleep(0.5)
                    #element = WebDriverWait(self.driver1,5+2*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"table_develop")))
                    print("            Refreshing WEB page...")
                    time.sleep(3)
            except:
                print("            Accessing URL failed... Let's try again!")
        print("    Successfully accessed to given URL, Let's make DATA into given shape!")

        DATA = data.text
        raw_data_list = self.DATA_inShape(DATA_LIST=DATA)
        DATA_LIST = self.Data_make_into_order(data_list=raw_data_list)
        print(DATA_LIST); print(len(DATA_LIST))
        self.CREATE_n_WRITE_INTO_TXT(outfileName=filename, Write_LIST=DATA_LIST)



    def DATA_inShape(self,DATA_LIST):
        test = 0; test1 = 0
        First_list = list()
        Day_flag = 0
        Day_date = 0
        for i in range(len(DATA_LIST)):
            if(i<39):
                continue
            #print(DATA_LIST[i])
            if(DATA_LIST[i]=='일'):
                Day_date = Day_date+1
                str_Day_date = str(Day_date)
                temp_list = list()
                location = i
                while(DATA_LIST[location]!='\n'):
                    if(DATA_LIST[location]=='일'):
                        location = location + 1
                        continue
                    if(DATA_LIST[location] == " "):
                        if((DATA_LIST[location-1] == " ")&(DATA_LIST[location+1] == " ")):
                            temp_list.append(" ")
                        location = location + 1
                        continue
                    else:
                        test_location1 = location; rota = 1
                        temp_str = str(DATA_LIST[test_location1])
                        while((DATA_LIST[test_location1+1] != " ") & (DATA_LIST[test_location1+1] != "\n")):
                            test_location1 = test_location1 + 1
                            rota = rota + 1
                            temp_str = temp_str + DATA_LIST[test_location1]
                        temp_list.append(temp_str)
                        location = location + rota
                First_list.append(temp_list)
        #print(First_list); print(len(First_list))
        return First_list

    def Data_make_into_order(self,data_list):
        test_list = []
        for i in range(len(data_list[0])):
            temp_list = []
            for j in range(len(data_list)):
                temp_list.append(data_list[j][i])
            test_list.append(temp_list)
        #print(test_list)
        return_list = []
        for i in range(len(test_list)):
            for j in range(len(test_list[i])):
                if(test_list[i][j] == " "):
                    continue
                return_list.append(test_list[i][j])
        #print(return_list); print(len(return_list))
        return return_list

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



    def QUIT(self):
        print("======================================================================")
        print("Closing Current Web Browser")
        print("======================================================================")
        print("\n")
        self.driver1.quit()


def main():
    air_seoul = SEOUL_AIR()
    air_seoul.AWAKE_BROWSER(); time.sleep(2)
    #air_seoul.Access_URL("http://www.weather.go.kr/weather/climate/past_table.jsp?stn=108&x=10&y=14&yy=1997&obs=06"); time.sleep(2)
    air_seoul.Access_URL("http://www.weather.go.kr/weather/climate/past_table.jsp?stn=108&yy=2011&x=26&y=12&obs=12")
    year = 2014
    while(year<=2018):
        air_seoul.Click_for_DATE(Init_year=year)
        air_seoul.Take_data_n_Write(filename="/Users/leejunho/Desktop/git/python3Env/group_study/ko_stats/data/crawling/R_Humidity_2014_2018.txt")
        year = year + 1
    air_seoul.QUIT()

if __name__=="__main__":
    main()
