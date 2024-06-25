from PIL import Image

im = Image.open("img/1.png")
rgb_im = im.convert('RGB')
rgb_im.save('img/1.jpg')
