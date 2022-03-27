"""
图片验证码
"""

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def check_code(width=120, height=30, char_length=5, font_file='FZSTK.TTF', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rnd_char():
        # 生成随机字母
        return chr(random.randint(65, 90))

    def rnd_color():
        # 生成随机颜色
        return random.randint(0, 255), random.randint(10, 255), random.randint(64, 255)

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rnd_char()
        code.append(char)
        h = random.randint(0, 4)
        draw.text([i * width / char_length, h], char, font=font, fill=rnd_color())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rnd_color())

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)
