# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os
import re
from math import floor
from src.utils.run_cmd import run_cmd, adb_cmd, shell_cmd
from src.utils.log_util import log
from src.base.adb import Actions

class Apk_Info(object):
    def __init__(self,apkPath):
        self.apkPath = apkPath
        self.dump_info = run_cmd("aapt dump badging {}" .format(self.apkPath))

    def apk_size(self):
        """
        得到app的文件大小
        """
        size = floor(os.path.getsize(self.apkPath) / (1024 * 1000))
        return str(size) + "M"

    def package_name(self):
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(self.dump_info)
        if not match:
            raise Exception("can't get packageinfo")
        return match.group(1)

    def version_name(self):
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(self.dump_info)
        if not match:
            raise Exception("can't get packageinfo")
        return match.group(3)

    def version_code(self):
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(self.dump_info)
        if not match:
            raise Exception("can't get packageinfo")
        return match.group(2)

    def apk_name(self):
        for item in self.dump_info.split():
            match = re.compile("application-label:'(\S+)'", re.M).search(item)
            if match is not None:
                return match.group(1)

    def startup_activity(self):
        match = re.compile("launchable-activity: name=(\S+)").search(self.dump_info)
        if match is not None:
            return match.group(1)
        else:
            log.error("didn't find the launcher activity")


class Device_Info(object):
    def __init__(self, device=""):
        self.device = device

    def model(self):
        return shell_cmd("getprop ro.product.model").strip()

    def os_version(self):
        """
        获取设备中的Android版本号，如4.2.2
        """
        return shell_cmd("getprop ro.build.version.release").strip()

    def sdk_version(self):
        """
        获取设备SDK版本号
        """
        return shell_cmd("getprop ro.build.version.sdk").strip()

    def ip_address(self):
        return shell_cmd("ifconfig |{0} Mask".format(Actions.find_type)).strip().split("  Bcast")[0].split(":")[1]

    def brand_name(self):
        return shell_cmd("getprop ro.product.brand").strip()

    def device_name(self):
        return shell_cmd("getprop ro.product.name").strip()

    def device_sn(self):
        return shell_cmd("getprop ro.serialno").strip()

    def men_total(self):
        get_cmd = shell_cmd("cat /proc/meminfo")
        men_total = 0
        men_total_str = "MemTotal"
        for line in get_cmd.split("\r\n"):
            if line.find(men_total_str) >= 0:
                men_total = line[len(men_total_str) + 1:].replace("kB", "").strip()
                break
        return int(men_total)

    def cpu_kel(self):
        get_cmd = shell_cmd("cat /proc/cpuinfo")
        find_str = "processor"
        int_cpu = 0
        for line in get_cmd.split("\r\n"):
            if line.find(find_str) >= 0:
                int_cpu += 1
        return str(int_cpu) + "核"

    def app_pix(self):
        result = shell_cmd(" wm size")
        return result.split("Physical size:")[1]

if __name__ == "__main__":
    x = Apk_Info(r"C:\Users\dai\Desktop\sw\P_prj\2019\AppUIAuto\app\netdisk.apk")
    x.package_name()