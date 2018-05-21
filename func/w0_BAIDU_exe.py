# -*- coding: UTF-8 -*-
import sys
#sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from w0_BAIDU_py3_Firefox import BAIDU_INDEX

ID = "skyblue12"
PW = ""
KEYWORD = "%CE%ED%F6%B2"
outFILE = "BAIDU_PM20140104.txt"
YEAR =  str(2014)
s_MONTH = '0'+str(1)
e_MONTH = '0'+str(4)

baidu = BAIDU_INDEX()
baidu.AWAKE_BROWSER(filename = outFILE)
baidu.SEARCH_test()
baidu.LOGIN_BAIDU(ID, PW)
baidu.ACCESS_URL(start_year=YEAR, start_month=s_MONTH, end_month=e_MONTH)

baidu.QUIT()

