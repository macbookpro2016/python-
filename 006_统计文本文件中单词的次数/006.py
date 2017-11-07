import os 
import re

def get_file_list(file_path):
	file_list = []
	for root,dirs,files in os.walk(file_path):
		for file in files:
			if file.lower().endswith('.txt'):
				file_list.append(os.path.join(root,file))
	return file_list

def find_keyword(file_path):
	keywords = {}
	file_name = os.path.basename(file_path)
	with open(file_path,encoding = 'GBK') as file:
		text = file.read()
		word_list = re.findall(r'[a-zA-Z]+',text.lower())
		for word in word_list:
			if word in keywords:
				keywords[word] += 1
			else:
				keywords[word] = 1
		keywords_sorted = sorted(keywords.items(),key = lambda d:d[1])
	return file_name,keywords_sorted

for path in get_file_list(os.getcwd()):
	name,results = find_keyword(path)
	print(u"在 %s 文件中， %s 为关键词，共出现了 %s 次" %(name,results[-1][0],results[-1][1]))

