# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os
import re
import sys
import time
import platform
from src.utils.run_cmd import run_cmd, adb_cmd, shell_cmd
from src.utils.log_util import log


class Actions(object):
    if platform.system() == "Linux":
        find_type = "grep"
    elif platform.system() == "Windows":
        find_type = "findstr"

    @staticmethod
    def timestamp():
        return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

    @staticmethod
    def get_all_devices():
        '''
        get device list
        :return:
        '''
        devices = []
        result = adb_cmd("devices")
        for device in result.strip("\r\n").split("\r\n"):
            sn = device.replace("\tdevice", "")
            if "devices" not in sn and sn != "":
                devices.append(sn)
        return devices

    @staticmethod
    def device_ready(devics_sn = ""):
        '''
        get device state
        device：设备正常连接
        offline：连接出现异常，设备无响应
        unknown：没有连接设备
        no device return error: no devices/emulators found
        more then one device return error: more than one device/emulator
        :return:
        '''
        if devics_sn == "":
            result = adb_cmd("get-state")
        else:
            result = adb_cmd("-s {0} get-state".format(devics_sn))
        if result.strip() == "device":
            return True
        else:
            log.error("the state device is " + result)
            return False

    @staticmethod
    def reboot():
        """
        retboot devices
        :return:
        """
        command = "reboot"
        adb_cmd(command)

    @staticmethod
    def get_screen_resolution():
        '''
        :return:返回 x,y 的坐标值
        '''
        result = shell_cmd("wm size")
        if result != None and result != "":
            result = result.split(":")[-1].strip()
            x = result.split("x")[0]
            y = result.split("x")[1]
            return (int(x), int(y))
        else:
            result = shell_cmd("dumpsys window displays | {0} init=".format(Actions.find_type))
            "    init=1080x1920 480dpi cur=1080x1920 app=1080x1920 rng=1080x1008-1920x1848"
            result = result.strip().split(" ")[0].split("=")[1]
            x = result.split("x")[0]
            y = result.split("x")[1]
            return (int(x), int(y))

    @staticmethod
    def push(local, remote):
        '''
        # 将电脑文件拷贝到手机里面
        '''
        result = adb_cmd("push %s %s" % (local, remote))
        return result

    @staticmethod
    def pull(remote, local):
        '''
        # 拉数据到本地
        '''
        result = adb_cmd("pull %s %s" % (remote, local))
        return result

    @staticmethod
    def sync(directory, **kwargs):
        '''
        # 同步更新 很少用此命名
        '''
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += " -l"
            result = adb_cmd(command)
            return result

    @staticmethod
    def open_app(packagename,activity):
        '''
        打开指定app
        '''
        result = adb_cmd("shell am start -n %s/%s" % (packagename, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    @staticmethod
    def get_app_pid(pkg_name):
        '''
        # 根据包名得到进程id
        '''
        result = adb_cmd("shell ps | {0} ".format(Actions.find_type)+pkg_name)
        if result == '':
            return "the process doesn't exist."
        result = result.split(" ")
        return result[7]

    @staticmethod
    def get_focused_package_and_activity():
        '''
        获取当前应用界面的包名和Activity，返回的字符串格式为：packageName/activityName, 使用正则从如下字符串中提取
        mResumedActivity: ActivityRecord{149fa48 u0 com.dai.testsave/.MainActivity t86}
        :return:
        '''
        pattern = re.compile(r"mResumedActivity: ActivityRecord{.+\s(.+)\s.+}")
        out = shell_cmd("dumpsys activity ")
        return pattern.findall(out)[0].strip()

    @staticmethod
    def get_current_package_name():
        """
         获取当前运行应用的activity
         """
        return Actions.get_focused_package_and_activity().split("/")[0]

    @staticmethod
    def get_current_activity():
        """
        获取当前设备的activity
        """
        return Actions.get_focused_package_and_activity().split("/")[-1]

    @staticmethod
    def get_battery_level():
        """
        获取电池电量
        """
        level = shell_cmd("dumpsys battery |{0} level".format(Actions.find_type) ).split(": ")[-1]
        return int(level)

    @staticmethod
    def get_battery_status():
        """
        获取电池充电状态
        BATTERY_STATUS_UNKNOWN：未知状态
        BATTERY_STATUS_CHARGING: 充电状态
        BATTERY_STATUS_DISCHARGING: 放电状态
        BATTERY_STATUS_NOT_CHARGING：未充电
        BATTERY_STATUS_FULL: 充电已满
        """
        statusDict = {1 : "UNKNOWN",
                      2 : "CHARGING",
                      3 : "DISCHARGING",
                      4 : "NOT_CHARGING",
                      5 : "FULL"}
        status = shell_cmd("dumpsys battery | {0} status" .format(Actions.find_type)).split(": ")[-1]

        return statusDict[int(status)]

    @staticmethod
    def get_battery_temperature():
        """
        获取电池温度
        """
        temp = shell_cmd("dumpsys battery | {0} temperature".format(Actions.find_type)).split(": ")[-1]
        return int(temp) / 10.0

    @staticmethod
    def get_system_app_list():
        """
        获取设备中安装的系统应用包名列表
        """
        sysApp = []
        for packages in shell_cmd("pm list packages -s").split("\r\n")[:-1]:
            sysApp.append(packages.split(":")[-1])
        return sysApp

    @staticmethod
    def get_third_app_list():
        """
        获取设备中安装的第三方应用包名列表
        """
        thirdApp = []
        for packages in shell_cmd("pm list packages -3").split("\r\n")[:-1]:
            thirdApp.append(packages.split(":")[-1])
        return thirdApp

    @staticmethod
    def get_matching_app_list(keyword):
        """
        模糊查询与keyword匹配的应用包名列表
        usage: getMatchingAppList("qq")
        """
        matApp = []
        for packages in shell_cmd("pm list packages %s" % keyword).split("\r\n")[:-1]:
            matApp.append(packages.split(":")[-1])
        return matApp

    @staticmethod
    def install_app(appFile):
        """
        安装app，app名字不能含中文字符
        """
        adb_cmd("install -r %s" % appFile)

    @staticmethod
    def uninstall_app(pkg_name):
        """
            卸载应用args:- packageName -:应用包名，非apk名
        """
        adb_cmd(" uninstall %s" % pkg_name)

    @staticmethod
    def is_install_app(packageName):
        """
        判断应用是否安装，已安装返回True，否则返回False
        usage: isInstall("com.example.apidemo")
        """
        flag = False
        result = Actions.get_third_app_list()
        if result is None or len(result) < 0:
            return None
        for i in result:
            if re.search(packageName, i.strip()):
                flag = True
        return flag

    @staticmethod
    def clear_app_data(packageName):
        """
        清除应用用户数据
        usage: clearAppData("com.android.contacts")
        """
        if "Success" in shell_cmd("pm clear %s" % packageName):
            return "clear user data success "
        else:
            return "make sure package exist"

    @staticmethod
    def reset_current_app():
        """
        重置当前应用
        """
        packageName = Actions.get_current_package_name()
        component = Actions.get_current_activity()
        Actions.do_clear_app_data(packageName)
        Actions.do_start_activity(packageName + "/" + component)

    @staticmethod
    def start_activity(component):
        """
        启动一个Activity
        usage: startActivity(component = "com.android.settinrs/.Settings")
        """
        shell_cmd("am start -n %s" % component)

    @staticmethod
    def start_webpage(url):
        """
        使用系统默认浏览器打开一个网页
        usage: startWebpage("http://www.baidu.com")
        """
        shell_cmd("am start -a android.intent.action.VIEW -d %s" % url)

    @staticmethod
    def call_phone(number):
        """
        启动拨号器拨打电话
        usage: callPhone(10086)
        """
        shell_cmd("am start -a android.intent.action.CALL -d tel:%s" % str(number))

    @staticmethod
    def press_key(event_keys):
        """
        发送一个按键事件
        args:
        - event_keys -:
        http://developer.android.com/reference/android/view/KeyEvent.html
        usage: sendKeyEvent(event_keys.HOME)
        """
        shell_cmd("input keyevent %s" % str(event_keys))
        time.sleep(0.5)

    @staticmethod
    def long_press_key(event_keys):
        """
        发送一个按键长按事件，Android 4.4以上
        usage: longPressKey(event_keys.HOME)
        POWER = 26
        BACK = 4
        HOME = 3
        MENU = 82
        VOLUME_UP = 24
        VOLUME_DOWN = 25
        SPACE = 62
        BACKSPACE = 62
        ENTER = 66
        MOVE_HOME = 122
        MOVE_END = 123
        """
        shell_cmd("input keyevent --longpress %s" % str(event_keys))
        time.sleep(0.5)

    @staticmethod
    def touch(x=None, y=None):
        """
        触摸事件
        usage: touch(e), touch(x=0.5,y=0.5)
        """
        shell_cmd("input tap %s %s" % (str(x), str(y)))
        time.sleep(0.5)

    @staticmethod
    def touch_by_ratio(ratioWidth, ratioHigh):
        """
        通过比例发送触摸事件
        args:
        - ratioWidth -:width占比, 0<ratioWidth<1
        - ratioHigh -: high占比, 0<ratioHigh<1
        usage: touchByRatio(0.5, 0.5) 点击屏幕中心位置
        """
        shell_cmd("input tap %s %s" % (str(ratioWidth * Actions.get_screen_resolution()[0]), str(ratioHigh * Actions.get_screen_resolution()[1])))
        time.sleep(0.5)

    @staticmethod
    def swipe_by_coord(start_x, start_y, end_x, end_y, duration=" "):
        """
        滑动事件，Android 4.4以上可选duration(ms)
        usage: swipe(800, 500, 200, 500)
        """
        shell_cmd("input swipe %s %s %s %s %s" % (str(start_x), str(start_y), str(end_x), str(end_y), str(duration)))
        time.sleep(0.5)

    @staticmethod
    def swipe_by_ratio(start_ratioWidth, start_ratioHigh, end_ratioWidth, end_ratioHigh, duration=" "):
        """
        通过比例发送滑动事件，Android 4.4以上可选duration(ms)
        usage: swipeByRatio(0.9, 0.5, 0.1, 0.5) 左滑
        """
        shell_cmd("input swipe %s %s %s %s %s" % (str(start_ratioWidth * Actions.get_screen_resolution()[0]), str(start_ratioHigh * Actions.get_screen_resolution()[1]), \
                                             str(end_ratioWidth * Actions.get_screen_resolution()[0]), str(end_ratioHigh * Actions.get_screen_resolution()[0]), str(duration)))
        time.sleep(0.5)

    @staticmethod
    def swipe_to_left():
        """
        左滑屏幕
        """
        Actions.swipeByRatio(0.8, 0.5, 0.2, 0.5)

    @staticmethod
    def swipe_to_right():
        """
        右滑屏幕
        """
        Actions.swipeByRatio(0.2, 0.5, 0.8, 0.5)

    @staticmethod
    def swipe_to_up():
        """
        上滑屏幕
        """
        Actions.swipeByRatio(0.5, 0.8, 0.5, 0.2)

    @staticmethod
    def swipe_to_down():
        """
        下滑屏幕
        """
        Actions.swipeByRatio(0.5, 0.2, 0.5, 0.8)

    @staticmethod
    def long_press_element( e):
        """
       长按元素, Android 4.4
        """
        shell_cmd("input swipe %s %s %s %s %s" % (str(e[0]), str(e[1]), str(e[0]), str(e[1]), str(2000)))
        time.sleep(0.5)

    @staticmethod
    def long_press_by_ratio(ratioWidth, ratioHigh):
        """
        通过比例长按屏幕某个位置, Android.4.4
        usage: longPressByRatio(0.5, 0.5) 长按屏幕中心位置
        """
        Actions.swipeByRatio(ratioWidth, ratioHigh, ratioWidth, ratioHigh, duration=2000)

    @staticmethod
    def send_text(string):
        """
        发送一段文本，只能包含英文字符和空格，多个空格视为一个空格
        usage: sendText("i am unique")
        """
        text = str(string).split(" ")
        out = []
        for i in text:
            if i != "":
                out.append(i)
        length = len(out)
        for i in range(length):
            shell_cmd("input text %s" % out[i])
            if i != length - 1:
                Actions.press_key(62)
        time.sleep(0.5)

    @staticmethod
    def do_fastboot():
        """
        进入fastboot模式
        """
        adb_cmd("reboot bootloader")

    @staticmethod
    def quit_app(packageName):
        """
        退出app，类似于kill掉进程
        usage: quitApp("com.android.settings")
        """
        shell_cmd("am force-stop %s" % packageName)

    @staticmethod
    def restart_5037():
        pid1 = os.popen("netstat -ano | findstr 5037 | findstr  LISTENING").read()
        if pid1 is not None:
            pid = pid1.split()[-1]
        # 下面的命令执行结果，可能因电脑而异，若获取adb.exe时出错，可自行调试！
        # E:\>tasklist /FI "PID eq 10200"
        # Image Name                     PID Session Name        Session#    Mem Usage
        # ========================= ======== ================ =========== ============
        # adb.exe                      10200 Console                    1      6,152 K

        process_name = os.popen('tasklist /FI "PID eq %s"' %pid).read().split()[-6]
        process_path = os.popen('wmic process where name="%s" get executablepath' %process_name).read().split("\r\n")[1]

        # #分割路径，得到进程所在文件夹名
        # name_list = process_path.split("\\")
        # del name_list[-1]
        # directory = "\\".join(name_list)
        # #打开进程所在文件夹
        # os.system("explorer.exe %s" %directory)
        # 杀死该进程
        os.system("taskkill /F /PID %s" %pid)
        os.system("adb start-server")

    @staticmethod
    def input_text(text):
        text_list = list(text)
        specific_symbol = set(['&','@','#','$','^','*'])
        for i in range(len(text_list)):
            if text_list[i] in specific_symbol:
                if i-1 < 0:
                    text_list.append(text_list[i])
                    text_list[0] = "\\"
                else:
                    text_list[i-1] = text_list[i-1] + "\\"
        seed = ''.join(text_list)
        shell_cmd('input text "%s"'%seed)

    @staticmethod
    def adb_image(path):
        shell_cmd("rm /sdcard/screenshot.png")
        shell_cmd("/system/bin/screencap -p /sdcard/screenshot.png")
        log.info(">>>截取屏幕成功，在桌面查看文件。")
        c_time = time.strftime("%Y_%m_%d_%H-%M-%S")
        image_path = os.path.join(path, c_time+".png")
        adb_cmd('pull /sdcard/screenshot.png %s"'%image_path)

    @staticmethod
    def adb_video(path, times=20):
        """
        android6 可以
        """
        PATH = lambda p: os.path.abspath(p)
        sdk = int(Actions.get_sdk_version())
        if sdk >= 19:
            shell_cmd("screenrecord --time-limit --size 640 * 360 %d --verbose /data/local/tmp/screenrecord.mp4" % times)
            log.info( ">>>Get Video file...")
            time.sleep(1.5)
            path = PATH(path)
            if not os.path.isdir(path):
                os.makedirs(path)
            c_time = time.strftime("%Y_%m_%d_%H-%M-%S")
            adb_cmd("pull /data/local/tmp/screenrecord.mp4 %s" % PATH("%s/%s.mp4" % (path, c_time)))
            # shell_cmd("rm /data/local/tmp/screenrecord.mp4")
        else:
            log.error( "sdk version is %d, less than 19!" % sdk)
            sys.exit(0)

    @staticmethod
    def get_crash_log(path):
        # 获取app发生crash的时间列表
        time_list = []
        result_list = shell_cmd("dumpsys dropbox | {0} data_app_crash".format(Actions.find_type))
        for time in result_list:
            temp_list = time.split(" ")
            temp_time= []
            temp_time.append(temp_list[0])
            temp_time.append(temp_list[1])
            time_list.append(" ".join(temp_time))

        if time_list is None or len(time_list) <= 0:
            log.info( ">>>No crash log to get")
            return None
        c_time = time.strftime("%Y_%m_%d_%H-%M-%S")
        log_file = os.path.join(path, c_time+".log")
        f = open(log_file, "wb")
        for timel in time_list:
            cash_log = shell_cmd(timel)
            f.write(cash_log)
        f.close()

    @staticmethod
    def get_permission_list(package_name):
        PATH = lambda p: os.path.abspath(p)
        permission_list = []
        result_list = shell_cmd("dumpsys package {0} | {1} android.permission" .format(package_name, Actions.find_type))
        for permission in result_list.split("\r\n"):
            if permission != "":
                permission_list.append(permission.strip())
        return permission_list

    @staticmethod
    def get_ui_dump_xml(xml_path):
        """
        获取当前Activity的控件树
        """
        PATH = lambda a: os.path.abspath(a)
        if int(Actions.get_sdk_version()) >= 19:
            shell_cmd("uiautomator dump --compressed /data/local/tmp/uidump.xml")
        else:
            shell_cmd("uiautomator dump /data/local/tmp/uidump.xml")
        path = PATH(xml_path)
        if not os.path.isdir(path):
            os.makedirs(path)
        adb_cmd("pull /data/local/tmp/uidump.xml %s" % PATH(path)).wait()
        shell_cmd("rm /data/local/tmp/uidump.xml").wait()
        if os.path.exists(os.path.join(path, "uidump.xml")):
            return True
        else:
            return False