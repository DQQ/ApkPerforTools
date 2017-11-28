#coding:utf-8

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice


device=MonkeyRunner.waitForConnection()
device.installPackage('F:\\QQ_374.apk')
MonkeyRunner.sleep(3.0)
runComponent = "com.tencent.qqmusic/.activity.AppStarterActivity"
device.startActivity(component=runComponent)