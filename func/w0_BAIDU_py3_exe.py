# -*- coding: UTF-8 -*-
from w0_BAIDU_py3_Firefox import BAIDU_INDEX

ID = "skyblue12"
PW = ""
KEYWORD = "%CE%ED%F6%B2"

baidu = BAIDU_INDEX()
baidu.AWAKE_BROWSER()
baidu.SEARCH_test()
baidu.LOGIN_BAIDU(ID, PW)
baidu.ACCESS_URL()

#baidu.QUIT()

