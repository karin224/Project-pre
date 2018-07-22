# -*- coding: utf-8 --
import time
import sys
from bs4 import BeautifulSoup
import requests


def sharesCrawl(shareCode,year,season):
	url = "http://quotes.money.163.com/trade/lsjysj_"+shareCode+".html?year="+year+"&season="+season
	data = requests.get(url, headers=headers)
	soup = BeautifulSoup(data.text, 'lxml')

	table = soup.findAll('table', {'class': 'table_bg001'})[0]
	rows = table.findAll('tr')
	return rows[::-1]
def writeCSV(shareCode,beginYear,endYear):

	csvFile = open('./data/' + shareCodeStr + '.csv', 'wb')
	writer = csv.writer(csvFile)
	writer.writerow(('日期', '开盘价', '最高价', '最低价', '收盘价', '涨跌额', '涨跌幅', '成交量', '成交金额', '振幅', '换手率'))
	for i in range(beginYear, endYear + 1):
		print(str(i) + ' is going')
		time.sleep(4)
		for j in range(1, 5):
			rows = sharesCrawl(shareCode, i, j)
			for row in rows:
				csvRow = []
				# 判断是否有数据
				if row.findAll('td') != []:
					for cell in row.findAll('td'):
						csvRow.append(cell.get_text().replace(',', ''))
					if csvRow != []:
						writer.writerow(csvRow)
		< span	style = "white-space:pre;" > < / span > \
				time.sleep(3)
		print(str(i) + '年' + str(j) + '季度is done')

if __name__ == '__main__':
	print(" ")


