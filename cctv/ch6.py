# -*- coding: UTF-8 -*-
import random

def TV_Schedule():
    shows = ['中国电影报道','今日影评','电影快讯','光影星播客']
    print("cctv6现在正在播放的是：{}".format(random.choice(shows)))
