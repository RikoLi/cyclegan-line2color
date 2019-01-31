import os
from glob import glob

from PIL import Image

old_path = '../datasets/old_acg_line_dataset/'
trainA_path = '../datasets/line2color/trainA/'
testA_path = '../datasets/line2color/testA/'
img_list = glob(old_path+'*.jpg')
img_list = img_list + glob(old_path+'*.gif')
img_list = img_list + glob(old_path+'*.bmp')
img_list = img_list + glob(old_path+'*.png')

for i in range(len(img_list)):
    img = Image.open(img_list[i])
    if i < 900:
        img.save(trainA_path+str(i)+'_trainA.png')
    else:
        img.save(testA_path+str(i)+'_testA.png')
print('Done!')
