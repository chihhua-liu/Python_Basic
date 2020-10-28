#  demo46   urllib  and  PIL
# 手動建images的目錄
from urllib.request import urlopen
from PIL import Image

BASE = "./images/%s"
URL1 = "https://www.cwb.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-2020-10-27-15-40.jpg"

fileToSave = urlopen(URL1)
origImage = Image.open(fileToSave)
origImage.save(BASE % "original.jpg")
halfSize = (origImage.size[0] // 2, origImage.size[1] // 2)
halfImage = origImage.resize(halfSize, Image.ANTIALIAS)
halfImage.save(BASE % 'half.jpg')
r1 = halfImage.transpose(Image.ROTATE_90)
r1.save(BASE % 'r90.jpg')
r2 = halfImage.transpose(Image.ROTATE_180)
r2.save(BASE % 'r180.jpg')
r3 = halfImage.transpose(Image.ROTATE_270)
r3.save(BASE % 'r270.jpg')
r4 = halfImage.rotate(45)
r4.save(BASE%'r45.jpg')