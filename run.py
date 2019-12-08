# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from configure.configure import *
from time import sleep
import subprocess
import pytest
import os
from src.utils.convert_code import *


def exec_test_run():
    subprocess.call(["pytest", "./src/testset", "--alluredir", "./result"])
    sleep(1)
    xml_file = get_xml_file(result_path)
    modify_text(xml_file)
    sleep(1)
    os.system("allure generate ./result -o ./report --clean")

if __name__ == "__main__":
    exec_test_run()
