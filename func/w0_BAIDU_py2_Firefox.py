# -*- coding: UTF-8 -*-
import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from urllib2 import Request, urlopen, URLError,HTTPError
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import re
#import Image, pytesseract


class BAIDU_INDEX:

    def __init__(self):
        self.COUNT = 0
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


    def SEARCH_test(self, KEYWORD="TEST"):
        finished = 0

        while finished == 0:
            print("    ======================================================================")
            print("    Try to ACCESS to BAIDU INDEX Page...")
            try:
                self.driver1.get("http://index.baidu.com/?from=pinzhuan#/")
#                WebDriverWait(self.driver1, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".loginname")))
                time.sleep(3.5)
                finished = 1
                pass
            except HTTPError:
                print("        **ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**")
                print("        HTTP ERROR, RETRYING...")
                print("        **ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**")
                pass
            except:
                print("        ....RELOADING.... ....RELOADING.... ....RELOADING.... ....RELOADING....")
                print("        Page to BAIDU INDEX, Need to be reloaded, RELOADING...")
                print("        ....RELOADING.... ....RELOADING.... ....RELOADING.... ....RELOADING....")
                time.sleep(5)
                pass
            print("    Accessed BAIDU index Page!")
            print("    ======================================================================")

            if(finished == 1):
                WRITE_NAME = 0
                while WRITE_NAME == 0:
                    try:
                        self.driver1.find_element_by_class_name("search-input").clear()
                        print("    cleaning search input...")
                        self.driver1.find_element_by_class_name("search-input").send_keys(KEYWORD) 
                        self.driver1.find_element_by_class_name("search-input-cancle").click() 
                        WRITE_NAME = 1
                        time.sleep(5)
                    except:
                        print("    Something went wrong.. I will retry..")

            print "        Waiting for BAIDU INDEX Page Loading..."
        print("    ======================================================================")
#        print("    Succeed with LOGIN!")
#        print("    **** !! Please Make sure you are successfully logged in !! ****")
        print("    ======================================================================")
        if(WRITE_NAME==1):
            return 1
        else:
            return 0

    def LOGIN_BAIDU(self, ID, PASSWD):
        Login = 0
        time.sleep(3)
        FIND_login = 0
        login_flag = 0
        while FIND_login==0:
            try:
                WebDriverWait(self.driver1, 10).until(EC.presence_of_element_located((By.ID,"TANGRAM__PSP_4__userName")))
                FIND_login=1
                print("        Successfully find login box!")
            except:
                if(login_flag>=3):
                    return 0
                login_flag = login_flag + 1
                print("        This is Login problem to BAIDU... Let's try until 4th time...") 


        while Login==0:
            try:
                self.driver1.find_element_by_id("TANGRAM__PSP_4__userName").clear() 
                self.driver1.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(ID)
                self.driver1.find_element_by_id("TANGRAM__PSP_4__password").clear()
                self.driver1.find_element_by_id("TANGRAM__PSP_4__password").send_keys(PASSWD)
                self.driver1.find_element_by_id("TANGRAM__PSP_4__submit").click()
                print("        I am logging in... please wait")
                time.sleep(1)
                Login=1
            except:
                print("        I need some time to be logged in... Let's me try again...")
                self.driver1.find_element_by_id("TANGRAM__PSP_4__userName").clear()
                self.driver1.find_element_by_id("TANGRAM__PSP_4__password").clear()
                time.sleep(3)
        print("        Log in Successful!")
        time.sleep(3)


    def ACCESS_URL(self, URL="http://index.baidu.com/?tpl=trend&word=%CE%ED%F6%B2"):
        url_finish=0
        TT = -1
        while url_finish==0:
            TT = TT + 1
            print("            Now I am accessing to given URL. A second please...")
            try:
                if(TT<=1):
                    self.driver1.get(URL)
                    time.sleep(2)
                    try:
                        element = WebDriverWait(self.driver1,5+3*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"chartselectdiy")))
                        url_finish = 1
                    except:
                        print("!@#!!$!@")
                else:
                    self.driver1.refresh()
                    time.sleep(2)
                    element = WebDriverWait(self.driver1,5+2*TT).until(EC.presence_of_element_located((By.CLASS_NAME,"chartselectdiy")))
                    print("            Refreshing WEB page...")
                    time.sleep(2)

            except:
                print("            Accessing URL failed.. Let's try again!")
        print("        Successfully accessed to given URL, Lets make DATA into given shape!")
        time.sleep(1.5)
        self.Click_for_Month()
        time.sleep(1.5)
        self.VIEW_BOX()


    def Click_for_Month(self, START_YEAR="2014",START_MONTH="01", END_MONTH="04"):
        self.driver1.find_element_by_class_name("chartselectdiy").click()

        SY_R = self.driver1.find_element_by_class_name("selectA.yearA")
        SY_R.find_element_by_class_name("sltTxt").click()
        S_SY = SY_R.find_element_by_class_name("sltOpt")
        SSY = self.driver1.find_element_by_class_name("selectA.yearA.slided")
        SSY.find_element_by_partial_link_text(START_YEAR+"年").click()

        SM_R = self.driver1.find_element_by_class_name("selectA.monthA")
        SM_R.find_element_by_class_name("sltTxt").click()
        S_SM = SM_R.find_element_by_class_name("sltOpt")
        SSM = self.driver1.find_element_by_class_name("selectA.monthA.slided")
        SSM.find_element_by_partial_link_text(START_MONTH).click()

        FIND_E = self.driver1.find_elements_by_class_name("ptb05")
        END_P = FIND_E[1]
        EY_R = END_P.find_element_by_class_name("selectA.yearA")
        EY_R.find_element_by_class_name("sltTxt").click()
        S_EY = EY_R.find_element_by_class_name("sltOpt")
        SEY = END_P.find_element_by_class_name("selectA.yearA.slided")
        SEY.find_element_by_partial_link_text(START_YEAR+"年").click()

        EM_R = END_P.find_element_by_class_name("selectA.monthA")
        EM_R.find_element_by_class_name("sltTxt").click()
        S_EM = EM_R.find_element_by_class_name("sltOpt")
        SEM = END_P.find_element_by_class_name("selectA.monthA.slided")
        SEM.find_element_by_partial_link_text(END_MONTH).click()

        self.driver1.find_element_by_class_name("button.ml20").click()





    def VIEW_BOX(self):
        el = self.driver1.find_element_by_tag_name("path")
        location = el.location; print(location)
        action = ActionChains(self.driver1)
        action.move_to_element_with_offset(el, 5, 5)
        action.click()
        action.perform()
        time.sleep(0.5)
        action.click();
        action.perform();
        time.sleep(0.5)
#        self.driver1.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
#        Position = "window.scrollTo(" + str(location['x']) + "," + str(location['y']) + ")";
#        print(Position)
#        self.driver1.execute_script(Position)
      
        time.sleep(3) 
        VBOX = self.driver1.find_element_by_id("viewbox") 
        View_label = VBOX.find_element_by_class_name("view-label")
        location = View_label.location; print(location)
        Position = "window.scrollTo(" + str(location['x']) + "," + str(location['y']) + ")";
        print(Position)
        self.driver1.execute_script(Position)

        FOR_DATE = VBOX.find_element_by_class_name("view-table-wrap")
        print(FOR_DATE.text)        
        FOR_VALUE = VBOX.get_attribute('value')
        print(VBOX.text)

        locations = VBOX.location
        rangle = (int(int(locations['x'])), int(int(locations['y'])),
              int(int(locations['x'])+100) ,
              int(int(locations['y'])) + 80)
        print(rangle)
        self.driver1.save_screenshot(str("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/BAIDU1.png"))

#        vIMG = VBOX.find_element_by_class_name("imgval")
#        vIMG.save_screenshot(str("BAIDU2.png"))

#        img = Image.open(str("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/BAIDU1.png"))
#        jpg = img.crop(rangle)


    def QUIT(self):
        print("======================================================================")
        print("Closing Current Web Browser")
        print("======================================================================")
        print("\n")
        self.driver1.quit()






