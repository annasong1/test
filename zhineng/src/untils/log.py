#coding=utf-8
import logging
import os
import time


class Logger():
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        logpath=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'/log/'
        logname=logpath+rq+'.log'
        fh=logging.FileHandler(logname)
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

