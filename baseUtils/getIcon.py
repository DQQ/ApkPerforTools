#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import os,sys
import zipfile

#----------------------------------------------------------------------
def getIcon(path = sys.argv[0]):
    path = str(path)
    if not os.path.exists(path):
        print '路劲错误!!!'
        return None
    for p in os.listdir(path):
        absPath = os.path.join(path,p)
        if os.path.splitext(absPath)[1] == '.apk':
            z = zipfile.ZipFile(absPath,'r')
            icon = z.read('res/drawable-hdpi-v4/main_icon.png')
            if  not os.path.exists('%s/icon'%path):
                os.mkdir('%s/icon'%path)
            with open('%s/icon/%s.png'%(path,os.path.splitext(p)[0]),'w') as f:
                f.write(icon)

if __name__ == '__main__':
    getIcon('/Users/dongqingqing/PycharmProjects/ApkPerforTools/upload')