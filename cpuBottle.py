#coding=utf-8
import json
from json import dumps

from baseUtils.Cpuinfo import CpuGet
from baseUtils.Memory import GetMemory
from bottle import run, route
from monkey import Monkey


@route('/api/cpuinfo', method='get')
def GetCpuInfo():
    pidCpu = CpuGet()
    cpudata = pidCpu.run()
    # print cpudata
    return json.dumps(cpudata)


run(port=8083, reloader=False)