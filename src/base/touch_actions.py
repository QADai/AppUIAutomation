# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


class Actions():
    """
    TouchAction方法是appium自已定义的新方法
    * 短按 (press) * 释放 (release) * 移动到 (moveTo) * 点击 (tap) * 等待 (wait) * 长按 (longPress)  * 执行 (perform)
    关于perform 官网给的伪代码中讲TouchAction().tap(el).perform()与driver.perform(TouchAction().tap(el))效果一致
    例子
    TouchAction(driver).press(el0).moveTo(el1).release()
    比如TouchAction(driver).press(x=0,y=308).release().perform()
    """
    def __init__(self, driver):
        self.driver = driver

    def press(self,el=None, x=None, y=None):
        """
        短按,比如TouchAction(driver).press(x=0,y=308).release().perform()
        """
        TouchAction(self.driver).press(el, x, y)

    def long_press(self,el=None, x=None, y=None, duration=1000):
        """长按控件
        longPress(WebElementel, int x, int y, Duration duration)
        开始按压一个元素或坐标点（x, y）。 相比press()方法，longPress()多了一个入参，既然长按，得有按的时间吧。duration以毫秒为单位。1000
        表示按一秒钟。其用法与press()方法相同。
        TouchAction action = new TouchAction(driver);
        action.longPress(names.get(200), 1000).perform().release();
        action.longPress(200, 200, 1000).perform().release();
        """
        TouchAction(self.driver).long_press(el, x, y, duration)

    def tap(self, el=None,x=None,y=None,count=1):
        """
         点击控件  tap(WebElement el, int x, int y)
         TouchAction action = new TouchAction(driver);
         action.tap(names.get(200)).perform().release();
         action.tap(200 ,200).perform().release();
        """
        TouchAction(self.driver).tap(el,x,y,count)

    def move_to(self,el=None,x=None,y=None):
        """
        移动到TouchAction action = new TouchAction(driver);
        action.moveTo(names.get(200)).perform().release();
        action.moveTo(200 ,200).perform().release();
        """
        TouchAction(self.driver).move_to(el,x,y)

    def wait(self, time):
        #等待, 单位为毫秒
        TouchAction(self.driver).wait(time)()

    def multi_touch(self,*actions):
        """
        MultiTouch 多点触控 它只提供了两个方法 一个add 一个执行perform.官网例子为
        action0 = TouchAction().tap(el1)
        action1 = TouchAction().tap(el2)
        MultiTouch().add(action0).add(action1).perform
        """
        for i in len(*actions):
            if i == 0:
                touch_obj = MultiAction.add(actions[i])
            else:
                touch_obj.add(actions[i])
        touch_obj.perform()
