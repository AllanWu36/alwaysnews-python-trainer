# -*- coding: UTF-8 -*-
from cctv.ch5 import Emergency
import random

def Breaking_News():
    Emergency()

def TV_Schedule():
    shows = ['新闻联播','焦点访谈','天气预报','今日说法']
    print("cctv1现在正在播放的是：{}".format(random.choice(shows)))

def Host():
    hosts = ['撒贝宁','朱广权']
    return random.choice(hosts)


