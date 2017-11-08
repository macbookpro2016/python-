import os
from PIL import Image

Iphone6_Width = 750
Iphone6_Height = 1334

def reset_image_size(file_path,new_path,width = Iphone6_Width,height = Iphone6_Height):
	image = Image.open(file_path)
	image_width,image_height = image.size

	# if image_width > width:
	# 	image_height = image_height * width // image_width
	# 	image_width = width
	# if image_height > height:
	# 	image_width = image_width * height // image_height
	# 	image_height = height
	image_width = Iphone6_Width
	image_height = Iphone6_Height
	new_image = image.resize((image_width,image_height),Image.ANTIALIAS)
	new_image.save(new_path)

# 从文件夹中依次循环改变每一张图片
def find_and_reset_from_dir(dir_path):
	# os.mkdir('iphone6')
	for root,dirs,files in os.walk(dir_path):
		for file in files:
			if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
				file_path = os.path.join(root,file)
				file_new_path = 'iphone6_'+file
				reset_image_size(file_path = file_path,new_path = file_new_path)

def main():
	find_and_reset_from_dir(os.getcwd())

if __name__ == '__main__':
	main()