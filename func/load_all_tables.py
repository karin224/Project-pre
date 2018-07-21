## written by manggny
# fetch all tables data from selected db, and saved as txt format(if you want)

import pymysql
import datetime


def call_all(id, pw, ip):
	all_result = {}
	createVar = locals()
	try:
		conn = pymysql.connect(
			user=id,
			passwd=pw,
			host=ip,
			charset='utf8')
	except:
		conn = pymysql.connect(
			user=id,
			passwd=pw,
			host=ip,
			charset='utf8')
	cur = conn.cursor()
	cur.execute("show databases")
	dblist = []
	for row in cur.fetchall():
		dblist.append(''.join(row))
	print("what db do you want to get?")
	for i in range(len(dblist)):
		print(str(i) + " : " + dblist[i])
	num = input("Please enter the number of db")
	saveornot = input("Do you want save tables as txt file?(Enter 1 for Yes, others for No)")
	cur.execute("use " + dblist[int(num)])
	cur.execute("show tables;")
	# cur.execute("show tables")
	tblist = []
	for i in cur.fetchall():
		tblist.append(''.join(i))
	for i in tblist:
		lists = locals()
		cur.execute('desc ' + i)
		col_list = []
		col_type = []
		for j in cur.fetchall():
			q = 0
			for k in j:
				if q == 0:
					col_list.append(k)
				elif q == 1:
					col_type.append(k)
					break
				q += 1
		for j in col_list:
			lists[i+j+'_list'] = [j]
		cur.execute('select*from ' + i)

		for row in cur.fetchall():
			k = 0
			for j in row:
				if type(j) is datetime.date:
					j=j.strftime("%Y-%m-%d-%H")

				lists.get(i+col_list[k]+'_list').append(j)

				k +=1
		table_lists = []
		for k in range(len(col_list)):
			table_lists.append(lists.get(i+col_list[k]+'_list'))
		all_result[i]=table_lists

		if saveornot == '1':
			f = open(dblist[int(num)] + "_" + i + ".txt",'w')
			for w in range(len(lists.get(i+col_list[0]+'_list'))):
				for l in range(len(col_list)):
					if l == (len(col_list)-1):
						f.write(str(lists.get(i+col_list[l]+'_list')[w])+"\n")
					else:
						f.write(str(lists.get(i + col_list[l] + '_list')[w]) + " ")

			f.close()
		else:
			continue

	cur.close()
	conn.close()
	return all_result

if __name__ == '__main__':
	result = call_all('root', 'pyku2018', '154.8.160.186')
	print(result['BAIDU_FeiYan'])
