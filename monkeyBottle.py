from bottle import run, route, static_file, get
from monkey import Monkey


@get('/monkey',method='get')
def runMonkey():
    mk = Monkey()
    print mk.get_conf()
    print mk.get_command()
    mk.run(mk.get_command())

    return static_file('monkey.html', root='/Users/dongqingqing/PycharmProjects/ApkPerforTools/static/html')


run(port=8081, reloader=False)