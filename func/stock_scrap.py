# the original code is from the pythonSpider repository in github, and manggny remaked it for using in PYKU
# How to use : find the company's code in http://quote.eastmoney.com/stocklist.html, and write it in the main def which is bottom of this python code
import requests
from bs4 import BeautifulSoup
import time

class stock_scrap():

    global headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.1708.400 QQBrowser/9.5.9635.400'
    }

    def __init__(self):

        #year = "2016"
        #from_year =
        url = 'http://quotes.money.163.com/trade/lsjysj_601857.html?year=2016&season=4'

        pass

    def sharesCrawl2(self,shareCode,year,season):
        shareCodeStr = str(shareCode)
        yearStr = str(year)
        seasonStr = str(season)
        url = 'http://quotes.money.163.com/trade/lsjysj_' + shareCodeStr + '.html?year=' + yearStr + '&season=' + seasonStr
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'lxml')
        stockData = soup.select('div.inner_box > table > tr > td')
        resultString = ''
        for index, value in enumerate(stockData):
            if index % 11 == 10:
                resultString += value.get_text() + '\n'
            else:
                resultString += value.get_text() + '\t'

        return resultString

    def clean(self,k):
        all_str = " "
        try:
            while 1:
                line,k = k.split("\n",1)
                days,other_thing = line.split("\t",1)
                days = days.replace("-",'')
                result_str = days+" "+other_thing
                #print(result_str)
                if all_str == " ":
                    all_str = "\n"+ result_str
                else:
                    all_str = '\n'+result_str + all_str
        except:
            return all_str

        return all_str

    def createUrl(self,shareCode,beginYear,endYear):
        shareCodeStr = str(shareCode)

        f = open('./' + shareCodeStr + '.txt', 'w+')
        f.write('date 开盘价 最高价 最低价 收盘价 涨跌额 涨跌幅（%）  volume(num) amount(10,000RMB) amplitude（%） 换手率（%）')
        try:
            for i in range(beginYear,endYear+1):
                print("year = "+str(i)+" is working....")
                time.sleep(5)

                for j in range(1,5):
                    data = self.sharesCrawl2(shareCode,i,j)
                    #strings = strings#.encode()
                    re_data = self.clean(data)
                    f.write(re_data)
                    time.sleep(5)
        except:
            print('----- 爬虫出错了！再试图。。-----')
            data = self.sharesCrawl2(shareCode, i, j)
            re_data = self.clean(data)  # .encode()

            f.write(re_data)
        finally:
            f.close()

if __name__ == '__main__':
    code = 600070 # you can find the codes in url http://quote.eastmoney.com/stocklist.html; some codes don't have data! you should check this first
    from_date = 2008
    end_date = 2018
    stock_data = stock_scrap()
    stock_data.createUrl(code,from_date,end_date)
