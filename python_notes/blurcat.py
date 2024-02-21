from PIL import Image,ImageFilter # 插入别人写好的图像滤镜import某个std的程序，在python中，不用再插入类似于<stdio.h>的所有functions，只需要用import调用所需要的函数类似
#类似from cs50 import get_string
before = Image.open("cat.bmp") # 打开一个文件名为cat.bmp图像
after = before.filter(ImageFilter.BoxBlur(12)) # 给before这个打开的图像加滤镜大（）表示图像滤镜的名字（12）表示模糊多少倍
after.save("catblur.bmp") # 将after存为这个名字