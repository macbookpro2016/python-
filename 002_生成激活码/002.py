import uuid

#生成num个激活码，长度默认为16，可设置 
def create_num(num,length = 16):
	result = []
	while num > 0:
		uuid_id = uuid.uuid1()
		# 用空替换掉uuid中的-,取出前length个字符
		temp = str(uuid_id).replace('-','')[:length]
		num -= 1
		if temp not in result:
			result.append(temp)
	return result

if __name__ == '__main__':
	uids = create_num(200)
	print(uids)