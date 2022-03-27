# -*- coding = utf-8 -*-
# @Time : 2022/3/14 15:11
# @Author : spray_dream
# @File : 001-生成随机验证码.py
# @Software: PyCharm

from PIL import Image, ImageDraw, ImageFont

# 生成一张白色的图片
img = Image.new(mode='RGB', size=(160, 40), color=(255, 255, 255))

# 创建一支画笔
draw = ImageDraw.Draw(img, mode='RGB')

# 导入字体文件
font = ImageFont.truetype('FZSTK.TTF', 28)

# 写入文本
draw.text([0, 0], '321', "red", font=font)

# 画点
draw.point([50, 10], fill='red')
draw.point([50, 30], fill=(255, 255, 255))

with open('code.png', 'wb') as f:
    img.save(f, format='png')
