# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from src.utils.log_util import log
from src.base.driver_engine import Driver_Engine
from src.page.toutiao.home_page import Home_Page


class instances:
    @classmethod
    def single(cls):
        return Driver_Engine.drivers()[0]

    @classmethod
    def spec_driver(cls,num):
        """
        返回指定的driver对象
        :param num: -1的原因是默认从0开始
        :return:
        """
        return Driver_Engine.drivers()[num-1]