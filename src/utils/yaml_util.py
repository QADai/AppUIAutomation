# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import yaml
import sys
sys.path.append(r'../../')
from configure.configure import *

class yaml_action:
    @classmethod
    def load(cls, path):
        with open(path, 'r', encoding='utf-8') as y:
            return yaml.load(y, Loader=yaml.FullLoader)

    @classmethod
    def dump(cls, file_path, data):
        with open(file_path, "w") as wf:
            yaml.dump(data, wf)

if __name__ == "__main__":
    print( yaml_action.load(desired_caps_param))