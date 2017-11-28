# coding=utf-8
import threading
import os
import re
import xlsxwriter
from xlsxwriter import workbook
from xlsxwriter.workbook import Workbook
import time
import platform
import json


# class CpuGet(threading.Thread):
class CpuGet():
    _list = []
    flag = True
    sleepTime = 1
    num = 0
    _start0 = 0
    _end0 = 0
    _start1 = 0
    _end1 = 0

    def __init__(self, num=6, sleepTime=1):
        # threading.Thread.__init__(self)
        self.num = num
        self.maxline = num
        self.rst_cpu_data = []
        self.pid, self.pName = CpuinfoTools().getCurrentPID()
        self._devices_name = CpuinfoTools().get_devices()
        self._product_name = CpuinfoTools().get_product()
        self.sleepTime = sleepTime

    def run(self):
        self._start0 = CpuinfoTools().getTotalCpuTime()
        self._start1 = int(CpuinfoTools().getPIDCpuTime(self.pid)[0])
        while self.flag:
            time.sleep(self.sleepTime)
            self._end0 = CpuinfoTools().getTotalCpuTime()
            self._end1 = int(CpuinfoTools().getPIDCpuTime(self.pid)[0])
            cpuUsage = float((self._end1 - self._start1)) / (self._end0 - self._start0) * 100
            runtimes = CpuinfoTools().getPIDCpuTime(self.pid)[1]
            self._list.append([runtimes,float('%.2f' % cpuUsage)])
            # self.cpu_list = [self._list,runtimes]
            print '%.2f' % cpuUsage
            self._start0 = self._end0
            self._start1 = self._end1
            self.num -= 1
            if self.num < 1:
                self.flag = False
                print 'stop trace!'

                rst_cpu_data = {
                    'status': 200,
                    'title': 'cpu监控信息',
                    'desc': 'cpu信息',
                    'name': 'cpu监控',
                    'mobile': self._product_name,
                    'devices_name': self._devices_name,
                    'pName': self.pName,
                    'user_data': self._list,
                    'total_data': self._start0,
                }
                # print rst_cpu_data
                CpuinfoTools().writeTxt(self._product_name, self._devices_name, self.pName, rst_cpu_data)

                return rst_cpu_data

                # CTools().writeChart(self._list, self._product_name, self._devices_name, self.pName, self.maxline - 2)
                # CTools.writeJson(self._list,self.pName)


class CpuinfoTools():
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

    def get_product(self):
        """
        获取设备品牌名称
        :return:设备品牌名称
        """
        p = os.popen('adb shell cat /system/build.prop |grep "ro.product.name"')
        product = p.readlines()
        spl = product[0].split('=')
        product_name = spl[1].strip()
        if product_name == '':
            return "请确认设备是否连接"
        else:
            return product_name

    def getCurrentPID(self):
        system = platform.system()
        if system is "Windows":
            _result = os.popen('adb shell dumpsys activity top | findstr ACTIVITY').read().strip()
        else:
            _result = os.popen('adb shell dumpsys activity top | grep ACTIVITY').read().strip()

        _resultPid = re.findall(u'pid=(\d+)', _result)[0]
        _resultPName = re.findall(u'(com.\w+.\w+)', _result)[0]
        return [_resultPid, _resultPName]

    def getTotalCpuTime(self):
        _result = os.popen('adb shell cat /proc/stat').read().strip()
        _result = _result.split('\n')[0]
        _result = re.findall(u'(\d+)', _result)
        _result = reduce(lambda x, y: int(x) + int(y), _result)
        return _result

    def getPIDCpuTime(self, pid):
        _result = os.popen('adb shell cat /proc/%s/stat' % pid).read().strip()
        runtimes = time.strftime('%H:%M:%S', time.localtime())
        _result = re.findall(u'(\d+)', _result)
        #求和
        _result = reduce(lambda x, y: x + y, [int(_result[11]), int(_result[12]), int(_result[13]), int(_result[14])]);
        return [_result,runtimes]


    def writeTxt(self,_product_name, _devices_name, pName,rst_cpu_data):
        f = open(
            '/Users/dongqingqing/PycharmProjects/ApkPerforTools/result/' + 'cupinfo-' + _product_name + '-' + _devices_name + '-' + self.getCurrentTime() + '.txt',
            'w')
        f.write(str(rst_cpu_data) + '\n')
        f.close()

if __name__ == '__main__':
    CpuGet().run()
