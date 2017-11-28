# coding=utf-8
import json
from json import dumps

from baseUtils.Memory import GetMemory
from bottle import run, route
from monkey import Monkey
from bottle import PasteServer


@route('/api/meminfo', method='get')
def GetMemoryInfo():
    pidMemory = GetMemory()
    memdata = pidMemory.run()

    #输出json
    return json.dumps(memdata)

run(port=8082, reloader=False)