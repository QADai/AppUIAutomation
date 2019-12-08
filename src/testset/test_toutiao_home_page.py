# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import sys
sys.path.append(r'.')
sys.path.append(r'../')
sys.path.append(r'../../')
from src.testset.driver_instances import instances
from src.utils.log_util import log
from src.page.toutiao.home_page import Home_Page
import pytest
import allure
from src.testset.data_resources import *
from src.utils.define_assert import *
from src.base.driver import Actions

@allure.feature("主页相关功能测试")
class TestTouTiaoHomePage():
    def setup_class(self):
        log.info("初始化 page object homepage >>>")
        self.driver = instances.single()
        self.driver_action = Actions(self.driver)
        self.HP = Home_Page(self.driver)

    def teardown_class(self):
        log.info("page object homepage 测试结束 <<<")
        self.driver.quit()

    @allure.story('进入推荐页面，检查tab页面内容')
    @allure.severity("critical")
    # @allure.description("启动程序，进入推荐tab页面")
    def test_enter_recommend(self):
        """启动程序，进入推荐tab页面"""
        self.HP.enter_recommend()
        recommend_text = self.driver_action.get_element_text(self.HP._recommend[0], self.HP._recommend[1])
        Assert.equal(recommend_text, "推荐", self.driver_action)

    @allure.story('查看未登录状态')
    @allure.severity("Normal")
    def test_enter_not_login(self):
        """查看未登录状态，这个是一个验证测试的实例"""
        self.HP.enter_not_login_page()
        # 以下元素直接写入元素是没有对应的page，暂时直接使用
        login_text = self.driver_action.get_element_text("xpath",
                                                         "//android.widget.TextView[@resource-id='com.ss.android.article.lite:id/aj5']")
        Assert.equal(login_text, "登录成功", self.driver_action)

    @allure.story("在查询页面输入不同的关键词查询，检查查询功能")
    @allure.severity("blocker")
    @pytest.mark.parametrize("key_word, TC_title", get_search_data(Run_TC_Priority))  # 参数化，从excel表格中根据不同的优先级
    def test_search(self, key_word, TC_title):
        """
        从excel表格中提取搜索的关键词，搜索并且检查标题中是否包含相应的字符串
        """
        _search_input_box = ("id", "com.ss.android.article.lite:id/db")
        paras = vars()
        allure.attach("用例参数:","搜索关键词：{0}； 测试描述：{1}".format(paras['key_word'], paras['TC_title']))
        inputbox = self.driver_action.wait_for_element(_search_input_box[0], _search_input_box[1])
        if inputbox is None:
            self.HP.enter_search_page()
            self.HP.do_search(key_word)
        else:
            self.HP.do_search(key_word)
        self.driver_action.wait(3)
        # log.info(self.driver_action.get_page_source())
        # Assert.contain(key_word, title_text, self.driver_action)


if __name__ == '__main__':
    # 使用如下的语句不能执行成功，通过命令行执行的
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
    # pytest.main(['-q', 'test_toutiao_home_page.py'])

# if __name__ == "__main__":
#     from subprocess import Popen, PIPE
#     with Popen(['pytest', '--tb=short',  # shorter traceback format
#                 str(__file__)], stdout=PIPE, bufsize=1,
#                 universal_newlines=True) as p:
#         for line in p.stdout:
#             print(line, end='')
