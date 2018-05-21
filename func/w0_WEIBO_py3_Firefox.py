# -*- coding: UTF-8 -*-
import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
#from urllib3 import URLError,HTTPError
from selenium.common.exceptions import TimeoutException


class WEIBO:

    def __init__(self):
        self.COUNT = 0
        pass

    def AWAKE_BROWSER(self, filename):
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

    def LOGIN(self,ID,PASSWD):
        login_flag = 0
        finished = 0
        self.Id = ID
        while finished == 0:
            print("    ======================================================================")
            print("    Try to ACCESS to WEIBO LOGIN Page...")
            try:
                self.driver1.get("https://www.weibo.com/login.php")
#                WebDriverWait(self.driver1, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".loginname")))
                time.sleep(2.5)
                finished = 1
                pass
#            except HTTPError:
#                print("        **ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**")
#                print("        HTTP ERROR, RETRYING...")
#                print("        **ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**")
#                pass
            except:
                print("        ....RELOADING.... ....RELOADING.... ....RELOADING.... ....RELOADING....")
                print("        ID login, Need to be reloaded, RELOADING...")
                print("        ....RELOADING.... ....RELOADING.... ....RELOADING.... ....RELOADING....")
                time.sleep(5)
                pass
            print("    Accessed LOGIN Page!")
            print("    ======================================================================")

            WRITE_NAME = 0
            EJ_WAIT = 0
            while WRITE_NAME == 0:
                self.driver1.set_page_load_timeout(15+EJ_WAIT*10)
                self.driver1.implicitly_wait(15+EJ_WAIT*10)
                try:
                    self.driver1.find_element_by_id("loginname").clear()
                    self.driver1.find_element_by_id("loginname").send_keys(ID)
                    self.driver1.find_element_by_name("password").send_keys(PASSWD)
                    time.sleep(2+ EJ_WAIT*5)
                    self.driver1.find_element_by_css_selector(".W_btn_a.btn_32px").click()
                    time.sleep(2+ EJ_WAIT*5)
                    WRITE_NAME = 1
                    time.sleep(5+ EJ_WAIT*5)
                except:
                    print("    Something went wrong.. I will retry..")
                    try:
                        if(EJ_WAIT<3):
                            self.driver1.refresh()
                        else:
                            self.driver1.get("https://www.weibo.com/login.php")
                        time.sleep(2 + EJ_WAIT*5)
                        EJ_WAIT = EJ_WAIT + 1
                    except:
                        pass

            print ("        Waiting for LOGIN Page Loading...")
#            time.sleep(2)
            if "login" in (self.driver1.current_url):
#                print "        ",self.driver1.current_url
                print("        LOGIN Problem ...  LOGIN Problem ...  LOGIN Problem ...  LOGIN Problem ...  ")
                print("        Possible LOGIN ERROR.")
                print("        LOGIN Problem ...  LOGIN Problem ...  LOGIN Problem ...  LOGIN Problem ...  ")
                if(login_flag>5):
                    self.driver1.quit()
                    break
                if(login_flag>2):
#                    ID = input("PLEASE, input ID : \n")
#                    PASSWD = input("PLEASE, input Password : \n")
                    for sounds in range(7):
                        sys.stdout.write('\a')
                        sys.stdout.flush()
                    QWER = input("Login problem... Please login on webpage by yourself! (press anykey to be continue!) \n")
                    return
                login_flag = login_flag + 1 
                finished = 0
        print("    ======================================================================")
        print("    Succeed with LOGIN!")
        print("    **** !! Please Make sure you are successfully logged in !! ****")
        print("    ======================================================================")
        return

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
        elif( (s_day >29) & ((START_MONTH ==2) & START_YEAR==2016)   ):
            s_day = s_day-29
            s_month = s_month + 1
        elif((s_day >28) & (START_MONTH ==2) ):    
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
        elif((e_day >29 ) & ((START_MONTH ==2) & START_YEAR==2016)   ):
            e_day = e_day -29
            e_month = e_month + 1
        elif((e_day >28) & (START_MONTH ==2) ):
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


    def MAKE_WEIBO_URL(self, DATE_LIST_INPUT, KEYWORD = "%25E9%259B%25BE%25E9%259C%25BE", LOCAL_NUM=1, PAGE =1):
        DATE = self.MAKE_DATE_STR(DATE_LIST_INPUT)[2]
        Add_str_weibo = "https://s.weibo.com/weibo/"
        Add_some_info = "&region=custom:11:"+ str(LOCAL_NUM) + "&typeall=1&suball=1&timescope=custom:"
        Add_page_info = "&page="
        WEB_PAGE = Add_str_weibo + KEYWORD + Add_some_info + DATE + Add_page_info + str(PAGE)
        self.keyword = KEYWORD
        self.webpage = WEB_PAGE
        return WEB_PAGE

    

    def ACCESS_URL(self, WEB_PAGE):
        filename = self.FILENAME
        TEMP1 = 0
        TEMP2 = 0
        finished =0
        timeoutwait = 0
        print("        ======================================================================")
        print("        ACCESSING Web page: ", self.webpage)
        TT = -1
        while finished == 0:
            self.ROBOT()
            TT = TT + 1
            self.driver1.set_page_load_timeout(45+TT*10)
            self.driver1.implicitly_wait(45+TT*10)
            try:
#                time.sleep(3)
                if(TT<=1):
                    self.driver1.get(self.webpage)
                    if((TT==0)|(timeoutwait != 1)):
                        timeoutwait = 0
                        10/0
                else:
                    self.driver1.refresh()
#                    element = WebDriverWait(self.driver1, 20+TT*30).until(EC.presence_of_element_located((By.CSS_SELECTOR,".red")))
                    element = WebDriverWait(self.driver1, 45+TT*10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".face")))
#                else:
#                    print(" [Take a look] WEIBO without keyword mentioned...")
#                    TEMP2 = 1
#                    break
#                element = WebDriverWait(self.driver1, 20+TT*10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".red")))   #|(By.CSS_SELECTOR,".W_btn_a.btn_32px"))) 
                element = WebDriverWait(self.driver1, 45+TT*10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".face")))
#                time.sleep(1)
                WebWait=0
                while WebWait==0:
#            finished = 1
                    try:
                        print("        Successfully Access to webpage. Locating keywords...")
#                        WebDriverWait(self.driver1, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".red")))   # (By.ID, ".red")))
                        print("        Succeed on accessing web page")
                        WebWait = 1
                        finished = 1
#            finally:
#                print("        Succeed on accessing web page")
#                finished = 1
#                print("WebDriverWait doesn't match with anything...")
#                time.sleep(10)
#                finished = 1
                    except:
                        print("        Seleninum WebDriver 'get' not returing... Refreshing on every 4rd time...")
                        TEMP1 = TEMP1+1
                        if(TEMP1%4==0):
                            print("        Refreshing the webpage...")
                            self.driver1.refresh()
                            time.sleep(3)
            except ZeroDivisionError:
                print("        If there is no WEIBO message, I will skip this page...")
                try:
                    if WebDriverWait(self.driver1, 5+TT*10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".noresult_tit"))):
                        print("        There is no such website... Moving to another district");
                        TEMP2 = 1
                        break
                except TimeoutException:
                    timeoutwait = 0
                    pass
                except:
                    timeoutwait = 1
            except TimeoutException:
                print("        TimeOut Exception... let's do it again... (Check internet connection/status)")
                if(TT >2):
                    print(" Breaking out this Webpage Due to webpage is not responding... (MAYBE loss of Internet Connection) ")
                    print(" [NEED YOUR HELP] - Input the WEIBO message number by yourself! (It is taking too long to be loaded..) *****")
                    CONTINUE = 'test'
                    while ((CONTINUE != "c") & (CONTINUE != "C")):
                        for sounds in range(7):
                            sys.stdout.write('\a')
                            sys.stdout.flush()
#                            print('\a')
                        time.sleep(0.5)
                        count_yourself = input("input WEIBO message number : \n")
                        print(count_yourself, "input as WEIBO message number of this page! \n")
                        CONTINUE = input("input 'C' if right, press any other key to be re-input : \n")
                    self.COUNT = self.COUNT + int(count_yourself)
                    TEMP2 = 1
                    break;
                try:
                    if WebDriverWait(self.driver1, 45+TT*10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".noresult_tit"))):
                        print("        There is no such website... Moving to another district");
                        TEMP2 = 1
                        break
                except:
                    pass
#            except:
#                print("        There is no such website... Moving to another district")
#                break
#            finally:
#                print("        Seleninum WebDriver 'get' not returing... Let's do again")
#                time.sleep(5); TEMP1 = TEMP1+1
#                    try:
##                        self.driver1.refresh()
#                    except:
#                        print("            Refresh Error... let's try 'get' without refresh...")
#                if(TEMP1>10):
#                    self.ROBOT()
#                if(TEMP1 > 15):                    
#                    print("            Please REFRESH the web site by your self!!!")
#                    CONTINUE = "test"
#                    while ((CONTINUE != "c") & (CONTINUE != "C")):
#                        CONTINUE = raw_input("[NEED YOUR HELP] - After refresh website by yourself, input 'C' to continue : \n")
#        time.sleep(5)
        LOCAL_NUM_WORD=0
        if(TEMP2 != 1):
            LOCAL_NUM_WORD = self.GREP_WORD(filename)
            pass
        print("        ======================================================================")
        print("")
        if(LOCAL_NUM_WORD<4):
            return 0
        else:
            return 1

    def GERP_WORD_to_zero(self):
        self.COUNT = 0

    def GREP_WORD(self, filename):
        TEXT_FLAG = 0
        GET_TEXT=0
        print("            ======================================================================")
        print("            Let's EXTRACT number of keyword mentioned! I will help you get keyword number on this page")
        while GET_TEXT==0:
            #self.ROBOT()
            try:
                time.sleep(5)
#                tt1 = self.driver1.find_elements_by_css_selector('.red')
                tt1 = self.driver1.find_elements_by_css_selector('.face')
#                self.ROBOT()
                print("            Successful!")
                time.sleep(3)
                GET_TEXT=1
#                for iii in range(len(tt1)):
#                    print(tt1[iii].text)
                    #s1 = (tt1[iii].text).encode('unicode-escape').decode('string_escape')
                    #print(s1)
            except:
                print("                Something went wrong... I will try again..")
                TEXT_FLAG = TEXT_FLAG+1            
                if(TEXT_FLAG>5):
                    self.ROBOT()
                if(TEXT_FLAG>10):
                    self.ACCESS_URL(self.webpage)
#        print("WRITE INTO YOUR FILE!")
        self.COUNT = self.COUNT + len(tt1)
#        Write_LIST = [self.datelist[0]+self.datelist[1]+self.datelist[2], ] 
#        CREATE_n_WRITE_INTO_TXT(filename,Write_LIST)

        print("            ======================================================================") 
        return len(tt1)


    def CREATE_n_WRITE_INTO_TXT(self, Write_LIST):
        filename = self.FILENAME
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
        infile = filename
        OF = open(infile,"a+")
        for i in range(len(Write_LIST)):
            OF.write("%s" %Write_LIST[i])
            if(i != len(Write_LIST)-1):
                OF.write(" ")
            if(i == len(Write_LIST)-1):
                OF.write("\n")
        OF.close()


    def ROBOT(self):
        ROBOT_FLAG = 0
        ROBOT = 0
        print("                ======================================================================")
        print("                This is ROBOT TEST...")
        rbTT = -1
        while ROBOT == 0:
            rbTT = rbTT + 1
            try:
#                time.sleep(1)
                self.driver1.set_page_load_timeout(2+rbTT*2)
                self.driver1.implicitly_wait(2+rbTT*2)
                tt2 = self.driver1.find_elements_by_css_selector('.code_tit')
#                print(" [NEED YOUR HELP] -  Unfortunately, you need to prove that your are not a ROBOT on Web")
                ROBOT=1
            except:
                print("                RE-test due to driver doesn't responding")
#                time.sleep(3)
                ROBOT_FLAG = ROBOT_FLAG + 1
                if(ROBOT_FLAG>20):
                    print(" [NEED YOUR HELP] -  Please check internet connection...")
 
        if(len(tt2)!=0):
            print(" [NEED YOUR HELP] - 'Prove you are not ROBOT' on Web site *****")
            CONTINUE = 'test'
            while ((CONTINUE != "c") & (CONTINUE != "C")):
                for sounds in range(7):
#                    sounds = sounds + 1
                    sys.stdout.write('\a')
                    sys.stdout.flush()
#                    print('\a')
                    time.sleep(0.5)
                CONTINUE = input("input 'C' to be continue : \n")
#            time.sleep(2)
        print("                END of ROBOT TEST...")
        print("                ======================================================================")

    def QUIT(self):
        print("======================================================================")
        try:
            print ("ID : ", self.Id, "Access is closed")
        except:
            print ("No login process is closed")
        print("Closing Current Web Browser")
        print("======================================================================")
        print("\n")
        self.driver1.quit()


