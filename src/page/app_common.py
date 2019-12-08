# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from src.base.driver import Actions, NoSuchElementException, TimeoutException
from src.utils.log_util import log

class before_home():
    _confirm_disclaimer = ("id", "com.ss.android.article.lite:id/pk")
    _red_package_close = ("id", "com.ss.android.article.lite:id/abq")
    _skip_ad = ("xpath", "//android.widget.TextView[@text='跳过广告']")

    def __init__(self,driver):
        self.driver = driver # 不要这里实例化driver方法，在testset中一边close
        self.driver_action = Actions(driver)

    def confirm_permisson(self):
        log.info("尝试关闭系统权限确认对话框")
        self.driver_action.click_persmisson_dialog(3)

    def click_disclaimer(self):
        log.info("尝试关闭免责声明")
        self.driver_action.element_click(self._confirm_disclaimer[0], self._confirm_disclaimer[1])

    def close_red_package_page(self):
        log.info("尝试关闭红包提示")
        self.driver_action.element_click(self._red_package_close[0], self._red_package_close[1])

    def skip_ad(self):
        log.info("尝试关闭广告")
        self.driver_action.element_click(self._skip_ad[0], self._skip_ad[1])

    def enter_home(self):
        self.driver_action.wait(2)
        self.confirm_permisson()

        self.driver_action.wait(1)
        self.click_disclaimer()

        self.driver_action.wait(1)
        self.close_red_package_page()

        self.driver_action.wait(1)
        self.skip_ad()

