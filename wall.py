from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import ctypes
import random
import os

def splitn(seq, n):
    while seq:
        yield seq[:n]
        seq = seq[n:]

def pad(line):
	if line.startswith('*'):
		return line
	else:
		return '   ' + line

os.chdir('D:\\vocab')

with open('vocab.txt', encoding='utf-8') as f:
    text = f.read()
    chunks = text.split('\n\n')

sl = []
for chunk in random.sample(chunks, 3):
    if 'CHAPTER' in chunk:
        continue
    chunks_m = []
    for lines in chunk.split('\n'):
        chunk_m = []
        for line in lines.split('\n'):
            words = line.split()
            lines_m = []
            for l in splitn(words, 9):
                lines_m.append(' '.join(l))
            chunk_m.append('\n'.join(map(pad, lines_m)))
        chunks_m.append('\n'.join(chunk_m))
    sl.append('\n'.join(chunks_m))
s = '\n\n'.join(sl)
print(len(s))
n = len(s)
if n < 700:
    fs = 36
elif 700 <= n < 1000:
    fs = 32
elif 1000 <= n < 1300:
    fs = 28
else:
    fs = 24

im = Image.open('wall/16.png')
draw = ImageDraw.Draw(im)
ft = ImageFont.truetype('times.ttf', fs)
white = (255, 255, 255)
black = (0, 0, 0)
draw.text((180, 130), s, white, font=ft)
im.save('out.jpg')

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, 'D:\\vocab\\out.jpg', 3)
