#encoding='utf-8'
"""
任务：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。 类似于图中效果
"""

from PIL import Image, ImageDraw, ImageFont
img = Image.open("resource/000.jpg")
h, w = img.size

posx, posy = (0.75*h, 0.10*w)
#print img.format
draw = ImageDraw.Draw(img)
newfont = ImageFont.truetype('simkai.ttf', 60)
draw.text((posx,posy),'4', (255,0,0),font=newfont)
img.show()



