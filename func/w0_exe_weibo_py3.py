import sys 
import time
sys.path.append("C:/Users/manggny/Desktop")
from w0_WEIBO_py3_Firefox import WEIBO

ID_junho = "manggny"
PASSWD_junho = "zine013559"
infilename = "PM_20180401_test.txt"
day = 12
month = 8
year = 2017

weibo = WEIBO()
weibo.AWAKE_BROWSER(filename = infilename)
#weibo.LOGIN(ID=ID_junho,PASSWD=PASSWD_junho)

for i in range(30):
    if(i%3==0):
        weibo.QUIT()
        weibo = WEIBO()
        weibo.AWAKE_BROWSER(filename = infilename)
        weibo.LOGIN(ID=ID_junho,PASSWD=PASSWD_junho)
    INFO =  weibo.DATE_MAKER(year,month,day)
    for j in range(18):
        if(j<=8):
            LOC_NUM = j+1
        elif(j<=15):
            LOC_NUM = j+2
        else:
            LOC_NUM = j+12
        for PG in range(50):
            web_page = weibo.MAKE_WEIBO_URL(INFO,LOCAL_NUM = LOC_NUM ,PAGE=PG+1); #print(web_page)
            CONTI = weibo.ACCESS_URL(web_page)
            print ("!!!!! Until Current page, cumulated keyword number : ",weibo.COUNT)
            print ("!!!!! District Number : ", LOC_NUM)
            print ("!!!!! Page Number : ", PG+1)
            print (""); print ("")
            if(CONTI == 0):
                break
    print (" * TOTAL COUNT NUM OF PM WORD : ",weibo.COUNT)
    INFO_STR = weibo.MAKE_DATE_STR(INFO)
    INPUT_LIST = [INFO_STR[3], weibo.COUNT]
    weibo.CREATE_n_WRITE_INTO_TXT(INPUT_LIST)
    weibo.GERP_WORD_to_zero()
    year= INFO[0]
    month = INFO[1]
    day = INFO[2]+1
weibo.QUIT()

