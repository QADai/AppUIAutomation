# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from src.page.app_common import before_home, log

class Home_Page(before_home):
    _recommend = ("xpath", "//android.widget.TextView[@text='推荐']")
    _second_tab = ("xpath","//android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.TextView[1]")
    _first_news = ("xpath", "//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]")
    _search_box = ("id", "com.ss.android.article.lite:id/alb")
    _search_input_box = ("id", "com.ss.android.article.lite:id/db")
    _search_input_box_button =("id", "com.ss.android.article.lite:id/gk")
    _home_page_entrance = ("xpath", "//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.RelativeLayout[1]")
    _not_logn_entrance = ("xpath", "//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.RelativeLayout[5]")

    def __init__(self,driver):
        super(Home_Page, self).__init__(driver)
        if not self.driver_action.element_is_displayed(self._recommend[0], self._recommend[1]):
            self.enter_home()

    def enter_recommend(self):
        log.info("尝试打开推荐tab页面：")
        self.driver_action.element_click(self._home_page_entrance[0], self._home_page_entrance[1])
        self.driver_action.element_click(self._recommend[0], self._recommend[1])

    def enter_second_tab(self):
        log.info("尝试打开第二个tab页面：")
        self.driver_action.element_click(self._second_tab[0], self._second_tab[1])

    def open_first_news(self):
        log.info("尝试打开第一个头条内容页面：")
        self.driver_action.element_click(self._first_news[0], self._first_news[1])

    def enter_search_page(self):
        self.driver_action.element_click(self._home_page_entrance[0], self._home_page_entrance[1])
        log.info("尝试开启输入框：")
        element = self.driver_action.wait_for_element(self._search_box[0], self._search_box[1])
        if element is not None:
            element.click()
            return True
        else:
            log.info("不能找到外层的输入框")
            return False

    def do_search(self,keyword):
        inputbox = self.driver_action.wait_for_element(self._search_input_box[0], self._search_input_box[1])
        if inputbox is not None:
            inputbox.send_keys(keyword)
            self.driver_action.element_click(self._search_input_box_button[0], self._search_input_box_button[1])
            # self.driver_action.send_press_keycode(66)  # KEYCODE_SEARCH
        else:
            log.info("不能找到里层的输入框")


    # def do_search(self, keyword):
    #     log.info("尝试开启输入框：")
    #     element = self.driver_action.wait_for_element(self._search_box[0], self._search_box[1])
    #     if element is not None:
    #         element.click()
    #         inputbox= self.driver_action.wait_for_element(self._search_input_box[0], self._search_input_box[1])
    #         if inputbox is not None:
    #             inputbox.send_keys(keyword)
    #             self.driver_action.send_press_keycode(66)  # KEYCODE_SEARCH
    #         else:
    #             log.info("不能找到里层的输入框")
    #     else:
    #         log.info("不能找到外层的输入框")


    def do_refresh(self):
        self.driver_action.swipe_to_down()

    def enter_not_login_page(self):
        self.driver_action.element_click(self._not_logn_entrance[0], self._not_logn_entrance[1])

if __name__ == '__main__':
    from src.base.driver_engine import Driver_Engine
    x = Home_Page(Driver_Engine.drivers()[0])
    x.enter_home()
    from time import sleep
    sleep(1)
    x.skip_ad()
    sleep(1)
    x.do_search("中国")




