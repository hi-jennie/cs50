from PIL import Image,ImageFilter

before = Image.open("cat.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("catedge.bmp")