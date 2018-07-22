# -*- coding: UTF-8 -*-
import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
#from urllib2 import Request, urlopen, URLError,HTTPError
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import re


class TWITTER_SCRAP:

    def __init__(self):
        pass

    def AWAKE_BROWSER(self, filename="test_remove.txt"):
        self.FILENAME = filename
#        self.driver1 = webdriver.PhantomJS()
#        self.driver1  = webdriver.Chrome()
        self.driver1 = webdriver.Firefox()
        self.driver1.set_page_load_timeout(15)
        self.driver1.implicitly_wait(20)
        time.sleep(3)
        print("======================================================================")
        print("NEW Web Browser is Opened")
        print("======================================================================")

    def DATE_MAKER(self,START_YEAR,START_MONTH,START_DAY,INTERVAL=1):
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
        elif( (s_day >29) & ((START_MONTH ==2) & (START_YEAR%4==0))   ):
            s_day = s_day-29
            s_month = s_month + 1
        elif((s_day >28) & (START_MONTH ==2) & (START_YEAR%4!=0)):
            s_day = s_day-28
            s_month = s_month + 1
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
        elif((e_day >29 ) & ((START_MONTH ==2) & (START_YEAR%4==0))   ):
            e_day = e_day -29
            e_month = e_month + 1
        elif((e_day >28) & (START_MONTH ==2) & (START_YEAR%4!=0) ):
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
        return [startDATE,endDATE,RE_DATE,END_DATE_FOR_TXT]

    def MAKE_LA_URL(self,DATE_LIST_INPUT,KEYWORD="drink%20water",LOCATION="Los%20Angeles", RANGE=125):
        COMMON_URL = "https://twitter.com/search?l=en&q="
        F_LOCATION = "%20near%3A%22"
        LA_RANGE = "%2C%20CA%22%20within%3A"
        RANGE_IN = str(RANGE) + "mi%20"
        SINCE_DATE = "since%3A"
        DATE_S = DATE_LIST_INPUT[0] + "%20until%3A"
        END_DATE = DATE_LIST_INPUT[1]
        END_URL = "&src=typd"
        MADE_URL = COMMON_URL + KEYWORD + F_LOCATION + LOCATION + LA_RANGE + RANGE_IN + SINCE_DATE + DATE_S + END_DATE + END_URL
        return MADE_URL



    def MAKE_NY_URL(self,DATE_LIST_INPUT,KEYWORD="drink%20water",LOCATION="time%20square", RANGE=125):
        COMMON_URL = "https://twitter.com/search?l=en&q="
        F_LOCATION = "%20near%3A%22" 
        LA_RANGE = "%22%20within%3A"
        RANGE_IN = str(RANGE) + "mi%20"
        SINCE_DATE = "since%3A"
        DATE_S = DATE_LIST_INPUT[0] + "%20until%3A"
        END_DATE = DATE_LIST_INPUT[1]
        END_URL = "&src=typd"
        MADE_URL = COMMON_URL + KEYWORD + F_LOCATION + LOCATION + LA_RANGE + RANGE_IN + SINCE_DATE + DATE_S + END_DATE + END_URL
        return MADE_URL

#https://twitter.com/search?l=en&q=drink%20water%20near%3A%22Los%20Angeles%2C%20CA%22%20within%3A15mi%20since%3A2018-05-19%20until%3A2018-05-20&src=typd
#https://twitter.com/search?l=en&q=drink%20water%20near%3A%22time%20square%22%20within%3A125mi%20since%3A2018-01-01%20until%3A2018-01-02&src=typd
#https://twitter.com/search?l=en&q=drink%20beer%20near%3A%22time%20square%22%20within%3A125mi%20since%3A2018-01-01%20until%3A2018-01-02&src=typd

    def ACCESS_URL(self,URL):
        url_finish=0
        TT = -1
        while url_finish==0:
            TT = TT + 1
            print("    Now I am accessing to given URL. A second please...")
            try:
                if(TT<=1):
                    self.driver1.get(URL)
                    time.sleep(2)
                    try:
                        element = WebDriverWait(self.driver1,5+3*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"js-stream-item.stream-item.stream-item")))
                        url_finish = 1
                    except:
                        print("!@#!!$!@")
                else:
                    self.driver1.refresh()
                    time.sleep(2)
                    element = WebDriverWait(self.driver1,5+2*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"js-stream-item.stream-item.stream-item")))
                    print("    Refreshing WEB page...")
                    time.sleep(2)

            except:
                print("    Accessing URL failed.. Let's try again!")
        print("    Successfully accessed to given URL, Let's wait until all of the tweets are fully loaded...")
        time.sleep(1.5)



    def SCROLL_BOTTOM(self):
        self.driver1.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def FIND_TWEET_NUMBER(self):
        url_finish=0
        TT = -1
        while url_finish==0:
            TT = TT + 1
            time.sleep(2)
            try:    
                ELEMENT = self.driver1.find_elements_by_class_name("js-stream-item.stream-item.stream-item")
                #print(len(ELEMENT))
                url_finish = 1
            except:
                pass        
        return len(ELEMENT)


    def GET_RAW_TEXT(self):
        url_finish=0
        TT = -1
        while url_finish==0:
            TT = TT + 1
            time.sleep(0.2)
            try:   
                ELEMENT = self.driver1.find_elements_by_class_name("js-stream-item.stream-item.stream-item")
                #print(len(ELEMENT))
                url_finish = 1
            except:
                pass 
        return ELEMENT

    def GET_TEXT_LIST(self):
        text_list = []
        element = self.GET_RAW_TEXT()
        for ele in element:
            text_container = ele.find_element_by_class_name("TweetTextSize.js-tweet-text.tweet-text")
            temp_text = text_container.text; temp_text = temp_text.replace('\n',' '); 
            temp_text = temp_text.replace('\r',' '); temp_text = temp_text.replace('  ',' '); 
            text_list.append(temp_text)
        return text_list
 
    def OUTFILE_NAME_MAKER(self,LOCATION ,KEYWORD, DATE):
        ONAME = LOCATION+"_" + KEYWORD + "_" + DATE + ".txt"
        return ONAME

    def CREATE_n_WRITE_INTO_TXT(self, outfileName, Write_LIST):
        filename = outfileName
        if(filename[0]=="/"):
            filename = filename
        elif((filename[0]=="C")&(filename[1]==":")):
            filename = filename
        else:
            filename = os.getcwd() + "/" + filename   # get the path included filename
        loca=len(filename)
        for i in range (1,len(filename)+1):       # find the "/" location
            if(filename[-i] == "/"):
                loca = i-1
                break
        FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten filename
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

