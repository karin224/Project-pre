import sys 
import time
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from w0_WEIBO_py2 import WEIBO

ID_junho = ""
PASSWD_junho = ""
infilename = "PM_20180401_test.txt"
year = 2016
day = 31
month = 3

weibo = WEIBO()
#weibo.LOGIN(ID=ID_junho,PASSWD=PASSWD_junho)

for i in range(750):
    INFO =  weibo.DATE_MAKER(year,month,day)
    month = INFO[1]
    day = INFO[2]+1
    year= INFO[0]
    print INFO[0],INFO[1],INFO[2],INFO[3],INFO[4],INFO[5]

