import time
from w0_TWITTER_py3_Firefox import TWITTER_SCRAP


twitter = TWITTER_SCRAP()
location = "NY"   ### do not change for a moment!!
keyword = "wine"
day = 31
month = 3
year = 2017
duration_day = 2
twitter.AWAKE_BROWSER()

IS_TWITTER = -1
for i in range(duration_day): 
    print("    ======================================================================")
    INFO =  twitter.DATE_MAKER(year,month,day)
    INFO_STR = twitter.MAKE_DATE_STR(INFO)
    year= INFO[0]
    month = INFO[1]
    day = INFO[2]+1
    print("")
    print("    **** This is",i+1,"th day rotation for", keyword)
    printstr = "    Starting from "+INFO_STR[0]+"!!!!"
    print(printstr)
    print("")

    TOT_TWEET=0
    for ii in range(6):
        FORMER_TWEET_NUM = -1
        if(ii==0):
            KEY_W = "drink%20" + keyword
            prstr = "    This time is for 'drink "+keyword+"' on "+ INFO_STR[0]
            print(prstr)
        elif(ii==1):
            KEY_W = "drank%20" + keyword
            prstr = "    This time is for 'drank "+keyword+"' on "+ INFO_STR[0]
            print(prstr)
        elif(ii==2):
            KEY_W = "have%20" + keyword
            prstr = "    This time is for 'have "+keyword+"' on "+ INFO_STR[0]
            print(prstr)
        elif(ii==3):
            KEY_W = "had%20" + keyword
            prstr = "    This time is for 'had "+keyword+"' on "+ INFO_STR[0]
            print(prstr)
        elif(ii==4):
            KEY_W = "get%20" + keyword
            prstr = "    This time is for 'get "+keyword+"' on "+ INFO_STR[0]
            print(prstr)
        elif(ii==5):
            KEY_W = "got%20" + keyword
            prstr = "    This time is for 'got "+keyword+"' on "+ INFO_STR[0]
            print(prstr)

#    URL_STR_LA = twitter.MAKE_LA_URL(DATE_LIST_INPUT=INFO_STR,KEYWORD=KEY_W)
        URL_STR_NY = twitter.MAKE_NY_URL(DATE_LIST_INPUT=INFO_STR,KEYWORD=KEY_W)
        print("    Now Accessing ",URL_STR_NY)
#    print(INFO_STR)

        twitter.ACCESS_URL(URL=URL_STR_NY)
        for j in range(100):
            time.sleep(1.5)
            TWEET_NUM = twitter.FIND_TWEET_NUMBER()
            if(TWEET_NUM==0):
                time.sleep(0.5)
                break
            twitter.SCROLL_BOTTOM()
            if(j==0):
                FORMER_TWEET_NUM = TWEET_NUM
            if((FORMER_TWEET_NUM == TWEET_NUM) & (j!=0)):
                time.sleep(1)
                TWEET_NUM = twitter.FIND_TWEET_NUMBER()
                if(FORMER_TWEET_NUM == TWEET_NUM):
#                    time.sleep(0.5)
                    break
                else:
                    pass
            FORMER_TWEET_NUM = TWEET_NUM
        print("        ******* Tweet number on this page :: ", TWEET_NUM, "*******")
        TOT_TWEET = TOT_TWEET + TWEET_NUM
        if(TWEET_NUM == 0):
            print("        !!!! Not wrinting into TEXT file, since there is no Tweet...")
            print("        End of",KEY_W," Counting. Let's move on!"); print("")
            continue
        ALL_TWEET_LIST = twitter.GET_TEXT_LIST()
        outname = twitter.OUTFILE_NAME_MAKER(LOCATION=location, KEYWORD=keyword, DATE=INFO_STR[0])
        twitter.CREATE_n_WRITE_INTO_TXT(outfileName=outname, Write_LIST=ALL_TWEET_LIST)
        print("        !!!! Successfully written to TEXT file !!!!")
        key_temp = KEY_W.replace("%20"," ")
        print("        End of",KEY_W," Counting. Let's move on!"); print("")

    print("    End of ",INFO_STR[0],"of",keyword,"...."); print("    Totally Counted Tweets Number :", TOT_TWEET, "!!")
    print("    ======================================================================"); print("")



twitter.QUIT()
