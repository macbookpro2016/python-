from PIL import Image,ImageDraw,ImageFont,ImageColor


def add_num(img):
	draw = ImageDraw.Draw(img)
	myFont = ImageFont.truetype('font1033\Starjout.ttf',size = 40)
	fillcolor = ImageColor.colormap.get('red')
	width,height = img.size
	draw.text((width-20,0-20),'1',font = myFont,fill = fillcolor)
	# img.save('result','jpeg')
	img.save('result.jpg', 'jpeg')
	return 0

if __name__ == '__main__':
	img = Image.open('1950561-b515ddc13b60429e.jpg')
	add_num(img)
