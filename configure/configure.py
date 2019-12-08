# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os

#文件夹路径
base_path = os.path.dirname(os.path.dirname(__file__))
apk_path = os.path.join(base_path, "app")
config_path = os.path.join(base_path, "configure")
log_path =  os.path.join(base_path, "logs")
screen_path = os.path.join(base_path, "screenshot")
report_path = os.path.join(base_path, "report")
result_path = os.path.join(base_path, "result")
TC_path = os.path.join(base_path, "testdata")
tools_path = os.path.join(base_path, "tools")


#服务器信息
test_server1_url = "https://www.baidu.com"
server1_username = "username1"
server1_password = "password"


#测试数据路径
search_excel = os.path.join(TC_path, 'search.xlsx')
desired_caps_param = os.path.join(config_path,'desired_caps.yaml')



#常用数字参数
load_page_timeout = 60


#用例优先级规则,设置方式为一个列表 一共分三个级别P1，P2，P3,e.g. ['P1', 'P2', 'P3']
Run_TC_Priority = ['P1', 'P2']

