#coding=utf-8
import yaml
import os

class yamlreader():
    def __init__(self,yamlfilepath):
        if os.path.exists(yamlfilepath):
            self.yamlfilepath=yamlfilepath

        else:
            print u'文件不存在'

    def data(self):
        stream = file(self.yamlfilepath, 'r')
        data = yaml.load(stream)
        return data








