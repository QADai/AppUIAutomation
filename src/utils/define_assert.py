# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import sys
import time
import pytest
import pathlib
import allure
import functools
from src.utils.log_util import log
from configure.configure import *

sys.path.append(r'.')
sys.path.append(r'../')
sys.path.append(r'../../')


def img_path():
    return os.path.join(screen_path, "Assure_Failed_" + time.strftime("%Y-%m-%d_%H_%M_%S") + ".png")


class Assertion_Failed(Exception):
    """Search keyword failed."""
    pass


class Assert:
    @classmethod
    def true(cls,value, base_driver):
        try:
            assert value, "{}的值不是True".format(value)
            return True
        except Exception as msg:
            base_driver.take_screen()
            log.error(msg)
            raise

    @classmethod
    def not_true(cls, value, base_driver):
        try:
            assert not value, "{}的值是True".format(value)
            return True
        except Exception as msg:
            base_driver.take_screen()
            log.error(msg)
            raise

    # @classmethod
    # def contain(cls, actual_value, expected_list, base_driver):
    #     with pytest.raises(ValueError):
    #         actual_value not in expected_list

    @classmethod
    def contain(cls, actual_value, expected_list, base_driver):
        try:
            assert actual_value in expected_list,"{0}的值不在{1}中".format(actual_value, expected_list)
            return True
        except Exception as msg:
            base_driver.take_screen()
            log.error(msg)
            raise

    @classmethod
    def equal(cls, actual, expect, base_driver):
        try:
            assert actual == expect, "{0} 的值和{1}的值不相等".format(actual, expect)
            return True
        except Exception as msg:
            base_driver.take_screen()
            log.error(msg)
            raise

    @classmethod
    def not_equal(cls, actual, expect, base_driver):
        try:
            assert actual != expect, "{0} 的值和{1}的值相等".format(actual, expect)
            return True
        except Exception as msg:
            base_driver.take_screen()
            log.error(msg)
            raise


if __name__ == "__main__":
    Assert.not_equal(3,3)