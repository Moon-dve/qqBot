import nonebot
from os import path
import logging, config
from json import loads, dump

def registerTrue():
    file = open('D:/dl/started.json', 'r')
    statusDict = loads(str(file.read()))
    statusDict['status'] = True
    with open('D:/dl/started.json', 'w+') as f:
        dump(statusDict, f, indent=4)

if __name__ == '__main__':
    registerTrue()
    nonebot.init(config)
    nonebot.log.logger.setLevel('WARNING')
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )
    logging.warning('Plugins successfully installed.')
    nonebot.run()







