import logging
import datetime
import os
"""日志路径"""
dirname = os.path.dirname(__file__)
# print(dirname)
logname = str(datetime.date.today()) + '.log'
# print(logname)
filepath = os.path.join(dirname + f"/logs/{logname}")
# print(filepath)

class Logger:

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(filepath,mode="a",encoding="utf8")
        sh = logging.StreamHandler()
        fm = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s==>(%(lineno)d) 日志信息：%(message)s')
        sh.setLevel(logging.DEBUG)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(fm)
        sh.setFormatter(fm)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)



logger = Logger().logger


