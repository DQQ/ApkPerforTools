#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import platform
import re
import time

class db_Utils():

    def get_devices(self):
        """
        获取设备名称
        :return:设备名称
        """
        a = os.popen('adb devices')
        devices = a.readlines()
        spl = devices[1].find('	')
        devices_name = devices[1][:spl]
        if devices_name == '':
            return "请确认设备是否连接"
        else:
            return devices_name

    def execADB(self, _adb):
        """"""
        return os.popen(_adb).read().strip()

    def adb_con(self, ip):
        """"""
        _adb = 'adb connect %s' % ip
        self.execADB(_adb)

    def adb_check(self):
        """"""
        _adb = 'adb get-state'
        adb_result = self.execADB(_adb)
        if adb_result == 'device':
            return True
        else:
            return False

    def readSetting(self):
        """"""
        with open(os.path.join(os.getcwd(), 'setting.txt'), 'r+') as f:
            return [f.readline().strip('\n'), f.readline().strip('\n')]


class GetAppInfo():
    def getCurrentTime(self):
        return time.strftime('%Y%m%d-%H%M%S', time.localtime())

    def get_devices(self):
        """
        获取设备名称
        :return:设备名称
        """
        a = os.popen('adb devices')
        devices = a.readlines()
        spl = devices[1].find('	')
        devices_name = devices[1][:spl]
        if devices_name == '':
            return "请确认设备是否连接"
        else:
            return devices_name

    def getCurrentPID(self):
        system = platform.system()
        if system is "Windows":
            _result = os.popen('adb shell dumpsys activity top | findstr ACTIVITY').read().strip()
        else:
            _result = os.popen('adb shell dumpsys activity top | grep ACTIVITY').read().strip()

        _resultPid = re.findall(u'pid=(\d+)', _result)[0]
        _resultPName = re.findall(u'(com.\w+.\w+)', _result)[0]

        # _resultProm = os.popen('top -n 1 -d 0.1 |grep' + _resultPName).read().strip()
        print [_resultPid, _resultPName]
        return [_resultPid, _resultPName]

    def getToalMemory(self):
        _result = os.popen('adb shell cat /proc/meminfo |grep -iE MemTotal').read().strip()
        _result = _result.split('\n')[0]
        _result = re.findall(u'(\d+)', _result)
        _result = _result[0]
        print _result
        return _result

    def getPidMemory(self,pid):
        _result = os.popen('adb shell dumpsys meminfo %s |grep TOTAL' % pid).read().strip()
        _result = re.findall(u'(\d+)', _result)
        _result = _result[0]
        print _result
        return _result

    def getTotalCpuTime(self):
        _result = os.popen('adb shell cat /proc/stat').read().strip()
        _result = _result.split('\n')[0]
        _result = re.findall(u'(\d+)', _result)
        _result = reduce(lambda x, y: int(x) + int(y), _result)
        return _result

    def getPIDCpuTime(self, pid):
        _result = os.popen('adb shell cat /proc/%s/stat' % pid).read().strip()
        _result = re.findall(u'(\d+)', _result)
        #求和
        _result = reduce(lambda x, y: x + y, [int(_result[11]), int(_result[12]), int(_result[13]), int(_result[14])]);
        return _result




if __name__ == '__main__':
    print db_Utils().readSetting()