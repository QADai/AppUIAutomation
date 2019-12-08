# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class getCrashText:
    def Count_crash(self, path):
        # 分析logcat日志
        count = 0
        count_line = 0
        word_list = ['ANR', 'FATAL']
        with open(path + '/logcat.log', 'rt', encoding="ISO-8859-1") as f:
            for line in f:
                count_line += 1
                for word in word_list:
                    if word in line:
                        text = f.readlines(count_line)
                        with open(path + "/crashInfo.txt", "a") as w:
                            w.write('=========================crash=========================\n')
                            w.writelines(text)
                            count += 1
                            w.close()
        return count

if __name__ == '__main__':
    print(getCrashText().Count_crash("."))
