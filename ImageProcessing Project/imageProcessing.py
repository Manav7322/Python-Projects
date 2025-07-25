from PIL import Image,ImageFilter
img=Image.open('./Pokedox/pikachu.jpg')
# print(img.format)
# print(img.size)
# print(img.mode)
filtered_img=img.filter=img.filter(ImageFilter.SMOOTH)
# print(dir(img))
filtered_img.save('blur.png','png')
