import pymysql
import uuid

def create_table(num,length):
	con = pymysql.connect('localhost','python','python','python3test',use_unicode = True,charset = 'utf8')
	cursor = con.cursor()
	sql = 'drop table if exists uuid'
	cursor.execute(sql)
	sql = """create table uuid(
	rank int primary key not null auto_increment,
	id varchar(20) not null  
	)auto_increment = 1"""
	print(sql)
	cursor.execute(sql)
	result = create_uuid(num,length)
	i = 0
	print('len(list):'+str(len(result)))
	while i < len(result):
		sql = 'insert into uuid (id) values ("'+ result[i] +'")'
		print(sql)
		cursor.execute(sql)
		i += 1
	con.commit()
	con.close()

def create_uuid(num,length = 16):
	result = []
	while num > 0:
		uuid_temp = uuid.uuid1()
		temp = str(uuid_temp).replace('-','')[:length]
		if temp not in result:
			result.append(temp)
		num -= 1
	return result

def main():
	create_table(500,16)

if __name__ == '__main__':
	main()