from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("a.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("sans-serif.ttf", 16)

draw.text((30, 5),"4",(255,0,0))
img.save('sample-out.jpg')
