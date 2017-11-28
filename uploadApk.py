# coding=utf-8
import json
import os
import platform
import time
from json import dumps

import bottle
from bottle import *

from baseUtils.Cpuinfo import CpuGet
from baseUtils.Memory import GetMemory
from cupInfoHtml import CUPINFO
from memInfoHtml import MEMINFO, MEMINFO2
from monkey import Monkey
from uploadApkHtml import UPLOADAPKHTML, UPLOADAPKHTML2


base_path = os.path.dirname(os.path.realpath(__file__))

upload_path = os.path.join(base_path, 'upload')
if not os.path.exists(upload_path):
    os.makedirs(upload_path)


@route('/', method='GET')
@route('/upload', method='GET')
@route('/index.html', method='GET')
@route('/upload.html', method='GET')
def index():
    """显示上传页"""
    return UPLOADAPKHTML2

@route('/upload', method='POST')
def do_upload():
    """处理上传文件"""
    filedata = request.files.get('fileField')
    """按时间上传新建目录"""
    load_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())
    apk_path = os.path.join(upload_path,load_time)
    if not os.path.exists(apk_path):
        os.makedirs(apk_path)

    if filedata.file:
        file_name = os.path.join(apk_path, filedata.filename)
        try:
            filedata.save(file_name)  # 上传文件写入
            time.sleep(1)
            a = os.popen('adb install -r '+ file_name)
            os.system(str(a))
        except IOError:
            return '上传文件失败'
        # return '上传并安装成功, 文件名: {}'.format(file_name)
        return static_file('upload.html', root='/Users/dongqingqing/PycharmProjects/ApkPerforTools/static/html')

    else:
        return '上传文件失败'


def get_packge_name():
    system = platform.system()
    if system is "Windows":
        _result = os.popen('aapt dump badging  |findstr package').read().strip()
    else:
        _result = os.popen('aapt dump badging  |grep package').read().strip()
        _result = _result.split('\n')[0]
        _result = re.findall(u'(\d+)', _result)
        _result = _result[0]

        print _result
        return _result

# @route('/favicon.ico', method='GET')
# def server_static():
#     """处理网站图标文件, 找个图标文件放在脚本目录里"""
#     return static_file('favicon.ico', root=base_path)
#
# @route('/images/<filename:re:.*\.png>')
# def send_image(filename):
#     return static_file(filename, root='/path/to/image/files', mimetype='image/png')

@route('/static/js/<path>')
def js(path):
    return static_file(path, root='/Users/dongqingqing/PycharmProjects/ApkPerforTools/static/js')  # 返回js文件，js文件在该目录的上级目录下的js文件夹下


@route('/memhtml', method='get')
def GetMemory_html():

    return static_file('mem.html', root='/Users/dongqingqing/PycharmProjects/ApkPerforTools/static/html')


@route('/cpuhtml', method='get')
def GetCpu_html():
    return static_file('cpu.html', root='/Users/dongqingqing/PycharmProjects/ApkPerforTools/static/html')

@route('/apklist', method='get')
def Getapklist_html():
    return static_file('apklist.html', root='/Users/dongqingqing/PycharmProjects/ApkPerforTools/static/html')



# @route('/api/meminfo', method='get')
# def GetMemoryData():
#
#     pidMemory = GetMemory()
#     memdata = pidMemory.run()
#
#     #输出json
#     return json.dumps(memdata)


# @route('/api/cupinfo', method='get')
# def GetCpuData():
#     pidCpu = CpuGet()
#     cpudata = pidCpu.run()
#
#     return json.dumps(cpudata)

@route('/getcurpkname', method='get')
def get_cur_pknm():
    try:
        f = os.popen('adb shell dumpsys window windows | grep mFocusedApp')
        for x in f.readlines():
            pknm = x.strip().split(' ')[4]
        pk_info = pknm.split('/')
        pk_data = {
            'errmsg': '查询成功',
            'package_name': pk_info[0],
            'avtivity_name': pk_info[1]
        }
    except Exception as e:
        pk_data = {
            'errmsg': '请确认设备正确连接或者是否有打开APP?'
        }
    return pk_data

@route('/getthirdpackage' ,method='get')
def get_third_package():
    rst = []
    f = os.popen('adb shell pm list package -3')
    for x in f.readlines():
        rst.append(x.strip().split(':')[1])

    third_package_data = {
        'third_pknm': rst,
        'errmsg': 'ok'
    }
    return third_package_data


@error(404)
def error404(error):
    """处理错误信息"""
    return '404 发生页面错误, 未找到内容'

# run(host='10.20.226.64',port=8081, reloader=False)  # reloader设置为True可以在更新代码时自动重载
run(port=8081, reloader=False)  # reloader设置为True可以在更新代码时自动重载
