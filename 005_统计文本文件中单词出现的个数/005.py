import re
# 统计英文字符的个数
def count_words(file_path):
	with open(file_path) as file:
		text = file.read()
		words = re.findall(r'[a-zA-Z]',text)
		print(words)
		count = len(words)
		return count

def main():
	i = count_words('friendship.txt')
	print(i)

if __name__ == '__main__':
	main()