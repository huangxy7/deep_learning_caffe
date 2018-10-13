#!/usr/bin/env python
#_*_coding=utf-8_*_

#########################
# >File Nime: pic.py
# >author: ly
# >email: 406728295@qq.com
#########################
from PIL import Image
import os

path='/home/jsj/xylook/train/1/' #图片路径
paths='/home/jsj/xylook/1/'#保存的文件夹




def change():
    f=os.listdir(path) #所有图片存入列表
    n = 0
    for i in f:
        try:
        #设置旧文件名（就是路径+文件名）
            oldname=path+f[n]
            pic = Image.open(oldname)
            #pic_rotate = pic.transpose(Image.FLIP_TOP_BOTTOM)#上下翻转图片
            pic_rotate = pic.transpose(Image.FLIP_LEFT_RIGHT)#左右翻转图片
            #pic_rotate = pic.rotate(point)#旋转15 30,45,60,75,90,105,120, 135 150,165,195,210,225,240,255,270度
            pic_rotate.save(paths + str(n) + 'asaa.jpg')
            n+=1
        except Exception as e:
            print(n)
            n+=1
            pass


    
def rename():   
    f=os.listdir(paths) #所有图片存入列表
    #获取该目录下所有文件，存入列表中
    n = 0
    for i in f:
        
        #设置旧文件名（就是路径+文件名）
        oldname=paths+f[n]
        #设置新文件名
        newname=paths+'has_'+str(i)+'.jpg'
        
        #用os模块中的rename方法对文件改名
        os.rename(oldname,newname)
        print(oldname,'======>',newname)
        n += 1
    
'''for i in range(15, 360, 15):
    if i == 180:
        continue
    change(i)
    rename()'''
change()
rename()