# -*- coding: UTF-8 -*-
from cctv.ch1 import Host
import random

def Emergency():
    print('这里是cctv5，现在由{}为大家插播一条紧急新闻'.format(Host()))

def TV_Schedule():
    shows = ['2022世界杯','体坛快讯','奥林匹克','NBA']
    print("cctv5现在正在播放的是：{}".format(random.choice(shows)))

