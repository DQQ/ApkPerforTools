# coding=utf-8

import time
import os
import platform
import re
import threading
import xlsxwriter
import json

from bottle import route


class GetMemory():
    _list = []
    flag = True
    sleepTime = 1
    num = 0
    _toalMemo = 0
    _appMemo = 0
    _end1 = 0


    def __init__(self, num=6, sleepTime=1):
        # threading.Thread.__init__(self)
        self.num = num
        self.maxline = num
        self.rst_mem_data = []
        self.pid, self.pName = GetAppInfo().getCurrentPID()
        self._devices_name = GetAppInfo().get_devices()
        self._product_name = GetAppInfo().get_product()

        self.sleepTime = sleepTime

    def run(self):
        self._toalMemo = GetAppInfo().getToalMemory()
        self._appMemo = GetAppInfo().getPidMemory(self.pid)
        while self.flag:
            time.sleep(self.sleepTime)
            # self._end0 = GetAppInfo().getToalMemory()
            self._end1 = GetAppInfo().getPidMemory(self.pid)
            json.dumps(self._list.append(self._end1))
            # self._appMemo = self._end1
            self.num -= 1
            if self.num < 1:
                self.flag = False
                # print 'stop trace!'
                print("stop trace!")
                rst_mem_data = {
                    'mobile': self._product_name,
                    'pName': self.pName,
                    'total_data': self._toalMemo,
                    'user_data': self._list,
                }


                # print 'rst_mem_data:' +srt(rst_mem_data)

                GetAppInfo().writeTxt(self._product_name, self._devices_name, self.pName, rst_mem_data)

                # json_mem = json.dumps(rst_mem_data)
                return rst_mem_data

                # GetAppInfo().writeChart(self._list, self._product_name, self._devices_name, self.pName, self.maxline - 2)


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

    def get_packge_name(self):
        system = platform.system()
        if system is "Windows":
            _result = subprocess.popen('aapt dump badging  |findstr package').read()
        else:
            _result = subprocess.popen('aapt dump badging  |grep package').read()

        # spl = packge_name[1].split('name=')
        # product_name = spl[1].strip()
        # _result = _result[0]

        print _result
        return _result



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

        _resultProm = os.popen('adb shell top -n 1 -d 0.1 |grep' + _resultPName).read()
        print([_resultPid, _resultPName])
        return [_resultPid, _resultPName]

    def getToalMemory(self):
        _result = os.popen('adb shell cat /proc/meminfo |grep -iE MemTotal').read().strip()
        _result = _result.split('\n')[0]
        _result = re.findall(u'(\d+)', _result)
        _result = _result[0]
        _result = round(int(_result)/1024,3)
        print(_result)
        return _result

    def getPidMemory(self,pid):
        _result = os.popen('adb shell dumpsys meminfo %s |grep TOTAL' % pid).read().strip()
        runtimes = time.strftime('%H:%M:%S', time.localtime())
        _result = re.findall(u'(\d+)', _result)
        _result = _result[0]
        _result = round(int(_result)/1024,3)
        print([runtimes, _result])
        return [runtimes, _result]

    def writeTxt(self,_product_name, _devices_name, pName,rst_mem_data):
        f = open(
            '/Users/dongqingqing/PycharmProjects/ApkPerforTools/result/' + 'meminfo-' + _product_name + '-' + _devices_name + '-' + self.getCurrentTime() + '.txt',
            'w')
        f.write(str(rst_mem_data) + '\n')
        f.close()


    # def writeChart(self, _list, _product_name, _devices_name, _PidName='unknow', _maxline=20):
    #
    #     workBook = xlsxwriter.Workbook('/Users/dongqingqing/PycharmProjects/ApkPerforTools/result/'+'meminfo-'+_product_name + '-' + _devices_name + '-' + self.getCurrentTime() + '.xls')
    #     workSheet = workBook.add_worksheet("MemroyInfo")
    #     workSheet.set_column(1, 1, 15)
    #     bold = workBook.add_format({"bold": 1})
    #     workSheet.write("A1", u"内存曲线", bold)
    #     _row = 1
    #     for info in _list:
    #         workSheet.write(_row, 0, info)
    #         _row += 1
    #
    #     chart = workBook.add_chart({"type": "line"})
    #     chart.add_series(
    #         {'categories': "=MemroyInfo!$A$2$:A$%d" % (_maxline + 1), 'values': ["MemroyInfo", 1, 0, (_maxline + 2), 0],
    #          'line': {'color': 'red'}})
    #     chart.set_title({"name": u"Memroy" + '\n' + u'进程：' + _PidName})
    #     chart.set_x_axis({"name": u"次数"})
    #     chart.set_y_axis({"name": u"当前进程使用率"})
    #     workSheet.insert_chart(0, 3, chart)
    #     workBook.close()


if __name__ == '__main__':
    GetMemory().run()
    # GetAppInfo().writeTxt(_product_name, _devices_name, pName, rst_mem_data)
    # GetAppInfo().get_packge_name()

