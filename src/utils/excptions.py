# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
class Element(object):

    # 常用操作关键字
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    INDEX = "index"
    find_elements_by_xpath = "xpaths"
    find_element_by_xpath = "xpath"
    find_element_by_css_selector = "css"
    find_element_by_class_name = "class_name"
    CLICK = "click"
    TAP = "tap"
    ACCESSIBILITY = "accessibility"
    ADB_TAP = "adb_tap"
    SWIPE_DOWN = "swipe_down"
    SWIPE_UP = "swipe_up"
    SWIPE_LEFT = "swipe_left"
    SET_VALUE = "set_value"
    GET_VALUE = "get_value"
    WAIT_TIME = 20
    PRESS_KEY_CODE = "press_keycode"

    GET_CONTENT_DESC = "get_content_desc"

    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"

    # 检查点
    CONTRARY = "contrary"  # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    CONTRARY_GETVAL = "contrary_getval"  # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check"  # 默认检查点，就是查找页面元素
    COMPARE = "compare"  # 历史数据和实际数据对比
    TOAST = "toast"


    RE_CONNECT = 1 # 是否打开失败后再次运行一次用例

    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    DEVICES_FILE = "devices.pickle"
    REPORT_FILE = "Report.xlsx"

def get_error(kw):
    elements = {
        Element.TIME_OUT: lambda: "==%s请求超时==" % kw["element_info"],
        Element.NO_SUCH: lambda: "==%s不存在==" % kw["element_info"],
        Element.WEB_DROVER_EXCEPTION: lambda: "==%s的driver错误==" % kw["element_info"],
        Element.INDEX_ERROR: lambda: "==%s索引错误==" % kw["element_info"],
        Element.STALE_ELEMENT_REFERENCE_EXCEPTION: lambda: "==%s页面元素已经发生==" % kw["element_info"],
        Element.DEFAULT_ERROR: lambda: "==请检查%s==" % kw["element_info"],
        Element.CONTRARY: lambda: "==检查点_%s失败_%s依然在页面==" % (kw["info"], kw["element_info"]),
        Element.CONTRARY_GETVAL: lambda: "==检查点_对比数据失败，当前取到到数据为:%s,历史取到数据为:%s" % (kw["current"], kw["history"]),
        Element.DEFAULT_CHECK: lambda: "==检查点_%s失败，请检查_%s==" % (kw["info"], kw["element_info"]),
        Element.COMPARE: lambda: "==检查点_对比数据失败，当前取到到数据为:%s,历史取到数据为:%s" % (kw["current"], kw["history"]),
        Element.TOAST: lambda: "==检查点_%s_查找弹框失败==" % kw["element_info"]
    }
    return elements[kw["type"]]()

class WrongLocation(Exception):
    def __init__(self, err='错误的元素定位方式'):
        Exception.__init__(self, err)


class ReadXmlError(Exception):
    def __init__(self, err='Xml读取初始化失败'):
        Exception.__init__(self, err)


class MailInitializationError(Exception):
    def __init__(self, err='邮件初始化'):
        Exception.__init__(self, err)


class GetDriverError(Exception):
    def __init__(self, err='初始化driver失败'):
        Exception.__init__(self, err)


class OpenXlsError(Exception):
    def __init__(self, err='打开用例文件失败'):
        Exception.__init__(self, err)


class CreatTestCaseError(Exception):
    def __init__(self, err='创建用例脚本失败'):
        Exception.__init__(self, err)


class CloseFileError(Exception):
    def __init__(self, err='关闭文件是发生错误'):
        Exception.__init__(self, err)


class ReadDeviceError(Exception):
    def __init__(self, err='读取待测设备时发生错误'):
        Exception.__init__(self, err)


class LogConfigError(Exception):
    def __init__(self, err='日志配置初始化错误'):
        Exception.__init__(self, err)


class InitResultError(Exception):
    def __init__(self, err='初始化测试结果表失败'):
        Exception.__init__(self, err)


class WriteResultError(Exception):
    def __init__(self, err='写入测试结果失败'):
        Exception.__init__(self, err)


class SaveReusltError(Exception):
    def __init__(self, err='保存测试结果失败'):
        Exception.__init__(self, err)


class ElementNotExist(Exception):
    def __init__(self, err='页面元素不存在'):
        Exception.__init__(self, err)
