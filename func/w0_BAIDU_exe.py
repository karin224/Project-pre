# -*- coding: UTF-8 -*-
import sys
#sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from w0_BAIDU_py3_Firefox import BAIDU_INDEX

ID = "skyblue12"
PW = ""
#KEYWORD = "%CE%ED%F6%B2"
KEYWORD = "%C9%A4%D7%D3%CC%DB"
outFILE = "BAIDU_SangZiTeng20140101.txt"
YEAR =  str(2014)
s_MONTH = 9
e_MONTH = 12
if s_MONTH<9:
    s_MONTH = '0'+str(s_MONTH)
else:
    s_MONTH = str(s_MONTH)

if e_MONTH<9:
    e_MONTH = '0' + str(e_MONTH)
else:
    e_MONTH = str(e_MONTH)
Init_URL = "http://index.baidu.com/?tpl=trend&type=1&area=514&time=13&word="
URL_TARGET = Init_URL + KEYWORD

baidu = BAIDU_INDEX()
baidu.AWAKE_BROWSER(filename = outFILE)
baidu.SEARCH_test()
baidu.LOGIN_BAIDU(ID, PW)
#baidu.ACCESS_URL(URL=URL_TARGET, start_year=YEAR, start_month=s_MONTH, end_month=e_MONTH)
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2014', start_month='01', end_month='04')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2014', start_month='05', end_month='08')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2014', start_month='09', end_month='12')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2015', start_month='01', end_month='04')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2015', start_month='05', end_month='08')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2015', start_month='09', end_month='12')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2016', start_month='01', end_month='04')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2016', start_month='05', end_month='08')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2016', start_month='09', end_month='12')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2017', start_month='01', end_month='04')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2017', start_month='05', end_month='08')
baidu.ACCESS_URL(URL=URL_TARGET, start_year='2017', start_month='09', end_month='12')

baidu.QUIT()

