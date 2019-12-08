# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from appium import webdriver
from configure.configure import *
from src.utils.yaml_util import yaml_action
from src.base.env_info import Apk_Info, Device_Info
from src.utils.log_util import log


class Driver_Engine(object):
    '''
    automationName: uiautomator2
    platformName: Android
    platformVersion: 7.1.2
    deviceName: placeholder1
    newCommandTimeout: 120
    app: test.apk
    browserName: Chrome, 不能和appPackage共存
    appPackage: com.jufuns.effectsoftware
    appActivity: com.jufuns.effectsoftware.act.SplashActivity
    resetKeyboard: True
    unicodeKeyboard: True
    noReset: False
    recreateChromeDriverSessions: True
    '''
    @staticmethod
    def drivers():
        PATH = lambda p: os.path.abspath(p)
        driver_list = []

        yaml_desires = yaml_action.load(desired_caps_param)
        yaml_desires_length = len(yaml_desires)
        if yaml_desires_length <1:
            log.error("yaml文件中没有设备信息")
            return None
        else:
            for desired_caps_return in yaml_desires:
                app_path = PATH(desired_caps_return["app"])

                for value in desired_caps_return.values():
                    if value == "":
                        log.info("发现desired_caps中有的元素值为空, 初始化env类，动态获取相应的值")
                        apk_info = Apk_Info(app_path)
                        device_info = Device_Info()

                desired_caps = dict()
                desired_caps['automationName'] = desired_caps_return["automationName"]
                desired_caps['platformName'] = desired_caps_return["platformName"]
                if desired_caps_return["platformVersion"] != None and desired_caps_return["platformVersion"] != "":
                    desired_caps['platformVersion'] = desired_caps_return["platformVersion"]
                else:
                    desired_caps['platformVersion'] = device_info.os_version()

                if desired_caps_return["deviceName"] != None and desired_caps_return["deviceName"] != "":
                    desired_caps['deviceName'] = desired_caps_return["deviceName"]
                else:
                    desired_caps['deviceName'] = device_info.device_sn()

                desired_caps['newCommandTimeout'] = desired_caps_return["newCommandTimeout"]
                desired_caps['app'] = app_path
                if desired_caps_return["appPackage"] != None and desired_caps_return["appPackage"] != "":
                    desired_caps['appPackage'] = desired_caps_return["appPackage"]
                else:
                    desired_caps['appPackage'] = apk_info.package_name()

                if desired_caps_return["appActivity"] != None and desired_caps_return["appActivity"] != "":
                    desired_caps['appActivity'] = desired_caps_return["appActivity"]
                else:
                    desired_caps['appActivity'] = apk_info.startup_activity()
                desired_caps['resetKeyboard'] = desired_caps_return["resetKeyboard"]
                desired_caps['unicodeKeyboard'] = desired_caps_return["unicodeKeyboard"]
                desired_caps['noReset'] = desired_caps_return["noReset"]
                desired_caps['recreateChromeDriverSessions'] = desired_caps_return["recreateChromeDriverSessions"]
                host_name = desired_caps_return["ip"]
                host_port = desired_caps_return["port"]

                # eval("device_desire_{0}".format(yaml_desires.index(device_desire)))["recreateChromeDriverSessions"]

                server_address = "http://" + str(host_name) + ":" + str(host_port) + "/wd/hub"
                log.debug("server address is: " + server_address + "current server match desire_Caps are below: " )
                log.debug(desired_caps)
                driver = webdriver.Remote(server_address, desired_caps)
                driver.implicitly_wait(5)
                driver_list.append(driver)
        return driver_list

if __name__ == "__main__":
    d = Driver_Engine()
    # print(d.drivers())