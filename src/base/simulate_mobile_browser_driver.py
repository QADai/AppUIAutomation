# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from selenium import webdriver

#这个类没有将变量抽象出来，在使用中根据具体情况下抽象出来
class SimulateMobileBrowserDriver:
    @classmethod
    def create(cls, device_name):
        user_agents = {
            "iPhone": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
            "Android": "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36",
            "iPad": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"
        }
        device_metrics = {
            "iPhone": {"width": 360, "height": 640},
            "Android": {"width": 360, "height": 640},
            "iPad": {"width": 768, "height": 1024},
        }
        if device_name in user_agents.keys():
            mobile_emulation = {"deviceMetrics": device_metrics[device_name], "userAgent": user_agents[device_name]}
            print(mobile_emulation)
        else:
            mobile_emulation = {"deviceName": device_name}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        return webdriver.Chrome(options=chrome_options)
