# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os
import socket
import time
import platform
import threading
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
from src.utils.log_util import log
from src.utils.run_cmd import run_cmd, get_command_result
from src.base.adb import Actions


def check_port(host, port):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mysocket.connect((host,port))
        mysocket.shutdown(2)
    except OSError as e:
        log.info("port %s is available!"%port)
        log.debug("尝试测试端口是否可以用，except返回信息："+str(e))
        return True
    else:
        log.info("port %s already be in use!"%port)
        return False


def release_port(port):
    find_type = Actions().find_type
    if platform.system().lower() == 'windows':
        get_port_info_cmd = 'netstat -ano | {0} {1}'.format(find_type,port)
        result = run_cmd(get_port_info_cmd)
        if str(port) and 'LISTENING' in result:
            i = result.index('LISTENING')
            start = i + len('LISTENING') + 7
            end = result.index('\n')
            pid = result[start:end]
            kill_cmd = 'taskkill /pid {0} -t -f'.format(pid)
            run_cmd(kill_cmd)
            log.info("kill the process with using port %s" % (port))
        else:
            log.info('port %s is available' % port)
    elif platform.system().lower() == 'darwin':
        # CHECK_PORT = 'lsof -i:'
        LIST_RUNNING_SERVER_PID = "ps -ef | grep 'node' | awk '/[A|a]ppium/{print $2}'"

        server_pid_list = get_command_result(LIST_RUNNING_SERVER_PID)
        for pid in server_pid_list:
            run_cmd('kill -9 {0}'.format(pid))

class AppiumServer:
    def __init__(self, host,kwargs=None):
        self.kwargs = kwargs

    def start_server(self):
        """start the appium server
        """
        for i in range(0, len(self.kwargs)):
            cmd = "appium --session-override  -p %s -bp %s -U %s" % (
            self.kwargs[i]["port"], self.kwargs[i]["bport"], self.kwargs[i]["devices"])
            if platform.system() == "Windows":  # windows下启动server
                t1 = RunServer(cmd)
                p = Process(target=t1.start())
                p.start()
                while True:
                    log.info("--------start_win_server-------------")
                    if self.win_is_runnnig("http://" + host +":" + self.kwargs[i]["port"] + "/wd/hub" + "/status"):
                        log.info("-------win_server_ 成功--------------")
                        break
            else:
                appium = run_cmd(cmd)
                while True:
                    appium_line = appium.stdout.readline().strip().decode()
                    time.sleep(1)
                    log.info("---------start_server----------")
                    if 'listener started' in appium_line or 'Error: listen' in appium_line:
                        log.info("----server_ 成功---")
                        break

    def win_is_runnnig(self, url):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        time.sleep(1)
        try:
            response = urllib.request.urlopen(url, timeout=5)
            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        except socket.timeout:
            return False
        finally:
            if response:
                response.close()

    def stop_server(self, devices):
        sysstr = platform.system()

        if sysstr == 'Windows':
            os.popen("taskkill /f /im node.exe")
        else:
            for device in devices:
                cmd = "lsof -i :{0}".format(device["port"])
                plist = os.popen(cmd).readlines()
                plisttmp = plist[1].split("    ")
                plists = plisttmp[1].split(" ")
                os.popen("kill -9 {0}".format(plists[0]))

    def check_service(self, times=5):
        # 检查服务是否已经启动,通过开启服务的端口校验
        #使用那个方法check_port
        pass

    def restart_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()


class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)





if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4723
    check_port(host, port)
    release_port(port)