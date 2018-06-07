import os
from src.untils.file_reader import yamlreader
import yaml

class Config():
    def get(self,yamlfilepath,element):
        data=yamlreader(yamlfilepath).data()
        URL = data[element]
        return URL