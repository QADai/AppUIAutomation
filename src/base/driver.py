# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import time
from src.base.driver_engine import Driver_Engine
from appium.webdriver.connectiontype import ConnectionType
import selenium
import allure
import appium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from src.utils.log_util import log
from src.base.js_helper import JSHelper
from configure.configure import *


class Actions(object):
    def __init__(self, driver):
        self.driver = driver
        self.js = JSHelper()

    def find_element(self, locator_type, locator_value, parent_element=None):
        try:
            if parent_element == None:
                if locator_type == 'id':
                    find_obj = self.driver.find_elements_by_id(locator_value)
                elif locator_type == 'xpath':
                    find_obj = self.driver.find_element_by_xpath(locator_value)
                elif locator_type == 'css':
                    find_obj = self.driver.find_element_by_css_selector(locator_value)
                elif locator_type == 'and':
                    find_obj = self.driver.find_element_by_android_uiautomator(
                        'new Uiselector().%s' % locator_value)  # 这里在使用的时候比如使用text，那么这里的path为text('123')
                elif locator_type == 'class':
                    find_obj = self.driver.find_element_by_class_name(locator_value)
                elif locator_type == 'name':
                    find_obj = self.driver.find_element_by_xpath("//*[@text={0}]".format(locator_value))
                elif locator_type == 'acces':
                    find_obj = self.driver.find_element_by_accessibility_id(locator_value)
                elif locator_type == 'text':
                    find_obj = self.driver.find_element_by_link_text(locator_value)
                elif locator_type == 'partial':
                    find_obj = self.driver.find_element_by_partial_link_text(locator_value)
                elif locator_type == 'tag':
                    find_obj = self.driver.find_element_by_tag_name(locator_value)
                else:
                    log.error("no element,please send tag,xpath,text,id,css,id,tag")
                    raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
            else:
                if locator_type == 'id':
                    find_obj = parent_element.find_elements_by_id(locator_value)
                elif locator_type == 'xpath':
                    find_obj = parent_element.find_element_by_xpath(locator_value)
                elif locator_type == 'css':
                    find_obj = parent_element.find_element_by_css_selector(locator_value)
                elif locator_type == 'class':
                    find_obj = parent_element.find_element_by_class_name(locator_value)
                elif locator_type == 'name':
                    find_obj = parent_element.find_element_by_xpath("//*[@text={0}]".format(locator_value))
                elif locator_type == 'acces':
                    find_obj = parent_element.find_element_by_accessibility_id(locator_value)
                elif locator_type == 'text':
                    find_obj = parent_element.find_element_by_link_text(locator_value)
                elif locator_type == 'partial':
                    find_obj = parent_element.find_element_by_partial_link_text(locator_value)
                elif locator_type == 'tag':
                    find_obj = parent_element.find_element_by_tag_name(locator_value)
                else:
                    log.error("no element,please send tag,xpath,text,id,css,id,tag")
                    raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
            return find_obj
        except Exception as e:
            log.error("find elements error, the exception is {0}".format(e))
            return e

    def find_elements(self, locator_type, locator_value, parent_element=None):
        try:
            if parent_element == None:
                if locator_type == 'id':
                    find_objs = self.driver.find_elements_by_id(locator_value)
                elif locator_type == 'xpath':
                    find_objs = self.driver.find_elements_by_xpath(locator_value)
                elif locator_type == 'css':
                    # Native App 暂不能使用
                    find_objs = self.driver.find_elements_by_css_selector(locator_value)
                elif locator_type == 'class':
                    find_objs = self.driver.find_elements_by_class_name(locator_value)
                elif locator_type == 'name':
                    find_objs = self.driver.find_elements_by_xpath("//*[@text={0}]".format(locator_value))
                elif locator_type == 'acces':
                    find_objs = self.driver.find_elements_by_accessibility_id(locator_value)
                elif locator_type == 'text':
                    # Native App 暂不能使用
                    find_objs = self.driver.find_elements_by_link_text(locator_value)
                elif locator_type == 'partial':
                    # Native App 暂不能使用
                    find_objs = self.driver.find_elements_by_partial_link_text(locator_value)
                elif locator_type == 'tag':
                    # Native App 暂不能使用
                    find_objs = self.driver.find_elements_by_tag_name(locator_value)
                else:
                    log.error("no element,please send tag,xpath,text,id,css,id,tag")
                    raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
            else:
                if locator_type == 'id':
                    find_objs = parent_element.find_elements_by_id(locator_value)
                elif locator_type == 'xpath':
                    find_objs = parent_element.find_elements_by_xpath(locator_value)
                elif locator_type == 'css':
                    find_objs = parent_element.find_elements_by_css_selector(locator_value)
                elif locator_type == 'and':
                    find_objs = parent_element.find_elements_by_android_uiautomator(
                        'new Uiselector().%s' % locator_value)  # 这里在使用的时候比如使用text，那么这里的lujing为text('123')
                elif locator_type == 'class':
                    find_objs = parent_element.find_elements_by_class_name(locator_value)
                elif locator_type == 'name':
                    find_objs = parent_element.find_elements_by_xpath("//*[@text={0}]".format(locator_value))
                elif locator_type == 'acces':
                    find_objs = parent_element.find_elements_by_accessibility_id(locator_value)
                elif locator_type == 'text':
                    find_objs = parent_element.find_elements_by_link_text(locator_value)
                elif locator_type == 'partial':
                    find_objs = parent_element.find_elements_by_partial_link_text(locator_value)
                elif locator_type == 'tag':
                    find_objs = parent_element.find_elements_by_tag_name(locator_value)
                else:
                    log.error("no element,please send tag,xpath,text,id,css,id,tag")
                    raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
            return find_objs
        except Exception as e:
            log.error("find elements error, the exception is {0}".format(e))
            return e

    def get_by_type(self, locator_type):
        """
        返回查找位置的类型
        :param locator_type: str set by def which implement on SeleniumDriver class
        :return: tag type or False
        """
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'partial_link':
            return By.PARTIAL_LINK_TEXT
        elif locator_type == 'tag':
            return By.TAG_NAME
        elif locator_type == 'text' or locator_type == 'partial_text':
            return By.XPATH
        else:
            log.info("Locator type" + locator_type + " not correct/supported")
            return False

    def wait_for_element(self, locator_type, locator_value, time=10, poll=0.5):
        """此脚本主要用于查找元素是否存在，操作页面元素"""
        try:
            element = WebDriverWait(self.driver, time, poll).until(
            expected_conditions.presence_of_element_located((self.get_by_type(locator_type), locator_value)))
            return element
        except NoSuchElementException:
            log.debug("can't wait for the element, NoSuchElementException")
            return None
        except TimeoutException:
            log.debug("can't wait for the element, TimeoutException")
            return None
        else:
            log.debug("find element {0}, {1} fail".format(locator_type, locator_value))
            return None

    def wait(self, time):
        self.driver.implicitly_wait(time)

    def wait_until_presence_of_element(self, locator_type, locator_value, wait_time=5, poll=0.2):
        try:
            message = "Unable to find the element by {0}: '{1}' in the page '{2}'".format(locator_type, locator_value,
                                                                                          self.driver.current_url)
        except WebDriverException:
            message = "Unable to find the element by {0}: '{1}'".format(locator_type, locator_value)
        return WebDriverWait(self.driver, wait_time, poll).until(
            EC.presence_of_element_located((locator_type, locator_value)), message)

    def wait_until_element_disappear(self, locator_type, locator_value, timeout=10):
        try:
            message = "Unable to wait the element disappear by {0}: '{1}' in the page '{2}' during timeout '{3}'".format(
                locator_type, locator_value, self.driver.current_url, timeout)
        except WebDriverException:
            message = "Unable to wait the element disappear by {0}: '{1}' during timeout '{2}'".format(locator_type, locator_value,timeout)
        wait_time = 0
        while wait_time < timeout:
            elements = self.find_elements(locator_type, locator_value)
            if len(elements) == 0:
                log.info("the element disappear by {0}: '{1}' after wait {2}s".format(locator_type, locator_value,
                                                                                      wait_time))
                break
            else:
                time.sleep(0.5)
                wait_time += 0.5
                continue
        if wait_time >= timeout:
            log.info(message)
            return False
        else:
            return True

    def switch_to_navtive(self):
        """切换到native"""
        log.info("切换native")
        self.driver.switch_to.context("NATIVE_APP")

    def switch_to_webview(self):
        """切换到webview"""
        try:
            n = 1
            while n < 10:
                time.sleep(2)
                n = n + 1
                log.info(self.driver.contexts)
                for cons in self.driver.contexts:
                    if cons.lower().startswith("webview"):
                        self.driver.switch_to.context(cons)
                        # print(self.driver.page_source)
                        self.driver.execute_script('document.querySelectorAll("html")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("head")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("title")[0].style.display="block"')
                        log.info("切换webview成功")
                        return {"result": True}
            return {"result": False}
        except appium.common.exceptions.NoSuchContextException:
            log.error("切换webview失败")
            return {"result": False, "text": "appium.common.exceptions.NoSuchContextException异常"}

    def get_element_text(self, locator_type, locator_value, time=5, poll=0.5):
        """返回元素的文本值"""
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            log.info("得到元素的text值是：" + element.text)
            return element.text

    def get_element_tag_name(self, locator_type, locator_value, time=5, poll=0.5):
        """返回元素的tagName属性, 经实践返回的是class name"""
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            log.info("得到元素的tag_name值是：" + element.text())
            return element.tag_name()

    def element_click(self, locator_type, locator_value, time=5, poll=0.5):
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            element.click()

    def inputbox_clear(self, locator_type, locator_value, time=5, poll=0.5):
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            log.info("清空元素{0}".format(locator_value))
            element.clear()

    def inputbox_send_key(self, locator_type, locator_value, parameter, time=5, poll=0.5):
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            log.info("元素{0}输入参数{1}".format(locator_value, parameter))
            element.send_keys(parameter)

    def element_is_enabled(self, locator_type, locator_value, time=5, poll=0.5):
        """返回元素是否可用True of False"""
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            log.info("元素{0}enabled ?".format(element.is_enabled()))
            return element.is_enabled()

    def element_is_selected(self, locator_type, locator_value, time=5, poll=0.5):
        """返回元素是否选择。可以用来检查一个复选框或单选按钮被选中。用法 element.is_slected()"""
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            log.info("元素{0}selected ?".format(element.is_selected()))
            return element.is_selected()

    def get_element_size(self, locator_type, locator_value, time=5, poll=0.5):
        """获取元素的大小（高和宽）"""
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            log.info("元素的大小{0}: ".format(element.size))
            return element.size

    def element_is_displayed(self, locator_type, locator_value, time=5, poll=0.5):
        """此元素用户是否可见,简单地说就是隐藏元素和被控件挡住无法操作的元素
        （仅限 Selenium，appium是否实现了类似功能不是太确定）
        这一项都会返回 False用法 driver.element.is_displayed()"""
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            log.info("元素{0}is displayed ?".format(element.is_enabled()))
            return element.is_displayed()

    def get_element_location(self, locator_type, locator_value, time=5, poll=0.5):
        """获取元素左上角的坐标"""
        element = self.wait_for_element(locator_type, locator_value, time, poll)
        if element is not None:
            log.info("元素{0}is displayed ?".format(element.is_enabled()))
            return element.location()

    def swipe_left(self):
        """左滑动"""
        width = self.get_screen_size()["width"]
        height = self.get_screen_size()["height"]
        x1 = int(width * 0.75)
        y1 = int(height * 0.5)
        x2 = int(width * 0.05)
        self.swipe(x1, y1, x2, y1, 600)
        log.info("--swipe to left--")

    def swipe_to_right(self):
        width = self.get_screen_size()["width"]
        height = self.get_screen_size()["height"]
        x1 = int(width * 0.05)
        y1 = int(height * 0.5)
        x2 = int(width * 0.75)
        self.swipe(x1, y1, x1, x2, 1000)
        log.info("--swipe to right--")

    def swipe_to_down(self):
        """swipe start_x: 200, start_y: 200, end_x: 200, end_y: 400, duration: 2000 从200滑动到400"""
        width = self.get_screen_size()["width"]
        height = self.get_screen_size()["height"]
        x1 = int(width * 0.5)
        y1 = int(height * 0.25)
        y2 = int(height * 0.75)
        self.swipe(x1, y1, x1, y2, 1000)
        log.info("--swipe to down--")

    def swipe_to_up(self):
        width = self.get_screen_size()["width"]
        height = self.get_screen_size()["height"]
        x1 = int(width * 0.5)
        y1 = int(height * 0.75)
        y2 = int(height * 0.25)
        self.swipe(x1, y1, x1, y2, 1000)
        log.info("--swipe to up--")

    def install(self, path):
        """安装应用程序"""
        self.driver.install_app(path)

    def uninstall(self, package_name):
        """卸载应用程序"""
        self.driver.remove_app(package_name)

    def close_app(self):
        """关闭应用程序"""
        self.driver.close_app()

    def reset(self):
        """重置app,重置应用(类似删除应用数据)"""
        self.driver.reset()

    def hide_keyboard(self):
        """隐藏键盘"""
        self.driver.hide_keyboard()

    def send_keyevent(self, event):
        """发送键盘按键   填入的是手机物理按键的数字代号"""
        self.driver.keyevent(event=event)

    def send_press_keycode(self, keycode):
        """发送键盘按键  填入的是键盘按键的数字代号"""
        self.driver.press_keycode(keycode=keycode)

    def long_press_keycode(self, keycode):
        """发送一个长按的按键码（长按某键）"""
        self.driver.long_press_keycode(keycode)

    def current_activity(self):
        """获取当前activity"""
        return self.driver.current_activity()

    def wait_activity(self, activity, time, interval=1):
        """等待指定的activity出现直到超时，interval为扫描间隔1秒即每隔几秒获取一次当前的activity, 返回的True 或 False
        activity - target activity
        timeout - max wait time, in seconds
        interval - sleep interval between retries, in seconds"""
        self.driver.wait_activity(activity, time=time, interval=1)

    def run_background(self, second):
        """后台运行"""
        self.driver.background_app(seconds=second)

    def app_is_installed(self, baoming):  # ios需要buildid
        self.driver.is_app_installed(baoming)

    def launch_app(self):
        """启动app"""
        self.driver.launch_app()

    def start_activity(self, app_package, app_activity):
        """启动activity"""
        self.driver.start_activity(app_package, app_activity)

    def shake(self):
        """摇手机"""
        self.driver.shake()

    def device_time(self):
        return self.driver.device_time

    def open_notification_bar(self):
        """安卓api 18以上"""
        self.driver.open_notifications()

    def return_network(self):
        """返回网络连接"""
        network_type = self.driver.network_connection
        return network_type

    def set_network_type(self, network_type):
        if network_type == 'wifi' or network_type == 'WIFI' or network_type == 'w' or network_type == 'WIFI_ONLY':
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        elif network_type == 'data' or network_type == 'DATA' or network_type == 'd' or network_type == 'DATA_ONLY':
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        elif network_type == 'ALL' or network_type == 'all' or network_type == 'a' or network_type == 'ALL_NETWORK_ON':
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        elif network_type == 'NO' or network_type == 'no' or network_type == 'n' or network_type == 'NO_CONNECTION':
            self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        elif network_type == 'AIRPLANE_MODE' or network_type == 'air' or network_type == 'ar' or network_type == 'fly':
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        else:
            raise NameError('plase wifi ,data,all,no,fly')

    def run_input_method(self):
        """返回安卓设备可用的输入法"""
        input_method = self.driver.available_ime_engines
        return input_method

    def check_input_method_active(self):
        """检查设备是否有输入法服务活动。返回真/假。"""
        check = self.driver.is_ime_active
        return check

    def active_input_medthod(self, engine):
        """激活安卓设备中的指定输入法，设备可用输入法可以从“available_ime_engines”获取"""
        self.driver.activate_ime_engine(engine)

    def close_input_medthod(self):
        """关闭安卓设备当前的输入法"""
        self.driver.deactivate_ime_engine()

    def return_input_medthod(self):
        input_medthod_name = self.driver.active_ime_engine
        return input_medthod_name

    def open_location_serivce(self):
        """打开安卓设备上的位置定位设置"""
        self.driver.toggle_location_services()

    def set_loaction(self, latitude, longitude, altitude):
        """设置设备的经纬度"""
        self.driver.set_location(latitude, longitude, altitude)

    def screen(self, filename):
        self.driver.get_screenshot_as_base64(filename)

    def close(self):
        self.driver.close()

    def kill(self):
        self.driver.quit()

    def get_screen_size(self):
        """获取窗口大小"""
        return self.driver.get_window_size()

    def zoom_in(self, element):
        """放大"""
        self.driver.zoom(element)

    def pinch(self, element, percent=None, steps=None):
        """在元素上执行模拟双指捏（缩小操作）
        - element - the element to pinch
        - percent - (optional) amount to pinch. Defaults to 200%
        - steps - (optional) number of steps in the pinch action"""
        self.driver.pinch(element, percent, steps)

    def fast_move(self, s_x, s_y, e_x, e_y):
        """按住A点后快速滑动至B点"""
        self.driver.flick(s_x, s_y, e_x, e_y)

    def swipe(self, s_x, s_y, e_x, e_y, duration=None):
        self.driver.swipe(s_x, s_y, e_x, e_y)

    def tap(self, x, y, duration=None):
        """模拟手指点击（最多五个手指），可设置按住时间长度（毫秒）
    	数组中的元祖是一个坐标，最多可以5个坐标
    	"""
        self.driver.tap([(x, y)], 500)

    def scroll(self, original_element, destination_element):
        """从元素origin_el滚动至元素destination_el"""
        self.driver.scroll(original_element, destination_element)

    def drag_and_drop(self, original_element, destination_element):
        """将元素origin_el拖到目标元素destination_el"""
        self.driver.drag_and_drop(original_element, destination_element)

    def push(self, data, path):
        self.driver.push_file(data, path)

    def pull(self, path):
        self.driver.pull_file(path)

    def scrollbar_slide_to_bottom(self, element):
        '''将页面滚动条拖到底部
        js="var q=document.documentElement.scrollTop=10000" '''
        js = "var q=document.getElementById('%s').scrollTop=10000" % element
        self.driver.execute_script(js)
        time.sleep(3)
        log.debug("将元素%s滑动到底部" % element)

    def accept_alert(self):
        try:
            self.driver.switch_to_alert().accept()
            log.debug("切换到弹窗，并点击确定按钮")
        except Exception as e:
            log.error("接受弹窗，出现异常：" + str(e))

    def toast_is_show(self, message, wait=5):
        """Android检查是否有对应Toast显示,常用于断言
            message: Toast信息
            wait:  等待时间
        """
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % message)
        try:
            WebDriverWait(self.driver, wait, 0.2).until(expected_conditions.presence_of_element_located(toast_loc))
            log.info("当前页面成功找到toast: %s" % message)
            return True
        except:
            log.error("当前页面中未能找到toast为: %s" % message)
            return False

    def click_persmisson_dialog(self, confirm_times):
        """
        :return:检测权限窗口
        """
        for i in range(int(confirm_times)):
            log.info("第{0}次尝试关闭权限对话框".format(i+1))
            try:
                els = WebDriverWait(self.driver, 10).until(
                    lambda driver: self.find_elements("class", "android.widget.Button"))
                for el in els:
                    text1 = el.text
                    if text1 == '允许':
                        el.click()
                    elif text1 == '始终允许':
                        el.click()
                    elif text1 == '确定':
                        el.click()
            except:
                return False

    # uiautomator 方法
    def find_ele_fromparent(self, locator_tmp, locator_target, is_Multiple=False, wait=5):
        """
        通过uiautomator查找定位元素的兄弟节点元素,不支持xpath，且兄弟节点必须同级
        支持的定位方式有：text(name),description(特有的),id,class name
        """
        log.info("页面【{}】通过元素【{}】查找兄弟元素【{}】".format(locator_tmp.get("page"), locator_tmp.get('name'),
                                                   locator_target.get("name")))
        map = {
            "name": "textContains",
            "description": "descriptionContains",
            "id": "resourceId",
            "class name": "className"
        }
        type_tmp = map.get(locator_tmp["type"])
        type_target = map.get(locator_target["type"])

        if type_tmp == None or type_target == None:
            log.error('当前定位方式不支持')

        value_tmp = locator_tmp["value"]
        value_target = locator_target["value"]

        ui_value = 'new UiSelector().{}(\"{}\").fromParent(new UiSelector().{}(\"{}\"))'.format(type_tmp, value_tmp,
                                                                                                type_target,
                                                                                                value_target)
        try:
            WebDriverWait(self.driver, wait).until(
                lambda driver: driver.find_element_by_android_uiautomator(ui_value))

            if is_Multiple == False:
                return self.driver.find_element_by_android_uiautomator(ui_value)
            else:
                return self.driver.find_elements_by_android_uiautomator(ui_value)

        except:
            log.info('页面【{}】未找到 元素【{}】\n locator: {}'.format(locator_tmp.get("page"), locator_target.get('name'),
                                                             str(locator_target)))
            if is_Multiple == False:
                return None
            else:
                return []

    def full_match_text_uiautormator(self, text):
        # 匹配全部text文字
        return self.driver.find_element_by_android_uiautomator('new UiSelector().text({0})'.format(text))

    def contain_text_uiautormator(self, text):
        # 包含text文字
        return self.driver.find_element_by_android_uiautomator('new UiSelector().textContains({0})'.format(text))

    def start_with_text_uiautomator(self, text):
        # 以text什么开始
        return self.driver.find_element_by_android_uiautomator('new UiSelector().textStartsWith({0})'.format(text))

    def regex_match_text_uiautomator(self, regex_text):
        # 正则匹配text, eg."^手.*"
        return self.driver.find_element_by_android_uiautomator('new UiSelector().textMatches({0})'.format(regex_text))

    def find_elements_by_className_uiautomator(self, class_name):
        # 根据className查找
        return self.driver.find_elements_by_android_uiautomator('new UiSelector().className({0})'.format(class_name))

    def find_elements_match_className_uiautomator(self, regrex_class_name):
        # classNameMatches, e.g. ^android.widget.*
        return self.driver.find_elements_by_android_uiautomator(
            'new UiSelector().classNameMatches({0})'.format(regrex_class_name))

    def find_element_resource_id_uiautomator(self, resouce_id):
        # resource-id、resourceIdMatches    类似我们html id 这个可能重复，
        return self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId({0})'.format(resouce_id))

    def find_element_description_uiautomator(self, text):
        # description, eg."S 日历"
        return self.driver.find_element_by_android_uiautomator('new UiSelector().description({0})'.format(text))

    def find_element_description_start_with_uiautomator(self, text):
        # descriptionStartsWith
        return self.driver.find_element_by_android_uiautomator(
            'new UiSelector().descriptionStartsWith({0})'.format(text))

    def find_element_description_match_uiautomator(self, regex_text):
        # descriptionMatches, e.g.".*历$"
        return self.driver.find_element_by_android_uiautomator(
            'new UiSelector().descriptionMatches({0})'.format(regex_text))

    # 以下是web behaviors
    def get_currnt_context(self):
        # 返回当前session中的app类型
        return self.driver.current_context

    def get_context(self):
        # 返回当前app的类型
        # WEBVIEW 或 WEBVIEW
        # 底层实际调用current_context
        return self.driver.context

    def get_contexts(self):
        # 获取app所有的类型
        # 有WEBVIEW的则以list的形式展示两个
        return self.driver.contexts

    def switch_to_context(self, context):
        # app类型切换 参数接收app类型
        # appium对selenium的switch_to的扩展
        # 增加了MobileSwitchTo，继承了selenium的switch_to
        self.driver.switch_to.context(context)

    def open_new_window(self, url):
        self.driver.execute_script("window.open('%s')" % url)

    def close_all_windows(self):
        for window in self.driver.window_handles:
            self.driver.switch_to.window(window)
            self.driver.close()

    def switch_to_the_other_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_current_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source

    def wait_page_load(self, timeout=5):
        log.info("Wait page load")
        status = "checking"
        while timeout:
            time.sleep(0.5)
            timeout -= 0.5
            status = self.driver.execute_script(self.js.get_page_load_status)
            if status.lower() == "complete":
                log.info("Page load completed")
                return True
        log.info("Page load not completed after timeout, now status is %s" % status)
        return False

    def get_logcat(self):
        self.driver.get_log("logcat")

    def get_appium_server_log(self):
        self.driver.get_log("server")

    def get_bug_report(self):
        self.driver.get_log("bugreport")

    def get_driver_log(self):
        self.driver.get_log("driver")

    def get_client_log(self):
        self.driver.get_log("client")

    def get_console_log(self):
        self.driver.get_log("browser")

    def screen_as_file(self):
        """返回 ture,flase"""
        img = self.driver.get_screenshot_as_file()
        return img

    def take_screen(self, name="app截图_"):
        """获取当前app的截图并加载到报告的对应附件中"""
        png_data = self.driver.get_screenshot_as_png()
        current_time = time.strftime('_%H:%M:%S_', time.localtime(time.time()))
        current_name = name + current_time + '.png'
        allure.attach(current_name, png_data, allure.constants.AttachmentType.PNG)

        # browser_instance.capture_screen(img_path)
        # if pathlib.Path(img_path).exists():
        #     allure.attach("失败截图", open(img_path, "rb").read(), allure.attach_type.PNG)
        # raise msg

    def execute_script(self, js_script, *args):
        """
        在当前窗口/框架（特指 Html 的 iframe ）同步执行 javascript 代码。
        你可以理解为如果这段代码是睡眠5秒，这五秒内主线程的 javascript 不会script: The JavaScript to execute.
        args: Any applicable arguments for your JavaScript.driver.execute_script('document.title')
        """
        self.driver.execute_script(js_script)

    def execute_async_script(self, js_script, *args):
        """
        插入 javascript 代码，只是这个是异步的，也就是如果你的代码是睡眠5秒，
        那么你只是自己在睡，页面的其他 javascript 代码还是照常执行driver.execute_async_script('document.title')
        """
        self.driver.execute_async_script(js_script)
