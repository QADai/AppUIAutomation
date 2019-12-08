# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import allure
import pytest
import datetime
from src.base.driver import Actions
from src.testset.test_toutiao_home_page import appium_driver
Action = Actions(appium_driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 用例报错捕捉
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        f = Action.driver.get_screenshot_as_png()
        allure.attach(f, '失败截图', allure.attachment_type.PNG)
        logcat = Action.driver.get_log('logcat')
        c = '\n'.join([i['message'] for i in logcat])
        allure.attach(c, 'APPlog', allure.attachment_type.TEXT)
        # if Action.get_app_pid() != Action.apppid:
        #     raise Exception('设备进程 ID 变化，可能发生崩溃')


def pytest_runtest_call(item):
    # 每条用例代码执行之前，非用例执行之前
    allure.dynamic.description('用例开始时间:{}'.format(datetime.datetime.now()))
    # if Action.get_app_pid() != Action.apppid:
    #     raise Exception('设备进程 ID 变化，可能发生崩溃')


@pytest.fixture()
def driver_setup(request):
    request.instance.driver = appium_driver.driver

    def teardown():
        request.instance.driver.quit()
    request.addfinalizer(teardown)