# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os
import subprocess
from src.utils.log_util import log

def run_cmd(cmd):
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.info("exec command " + cmd)
    sout, serr = res.communicate()
    return sout.decode("gbk", "ignore")

def get_command_result(command: str) -> list:
    result_list = []
    result = os.popen(command).readlines()
    if len(result) > 0:
        for r in result:
            if r == '\n':
                continue
            result_list.append(r.strip('\n'))
    return result_list


def adb_cmd(cmd):
    return run_cmd("adb " +cmd)


def shell_cmd(cmd):
    return adb_cmd("shell " + cmd)

if __name__ == "__main__":
    print(adb_cmd("devices"))