# -*- coding: UTF-8 -*-
import random
import cctv.ch6

def TV_Schedule():
    shows = ['财经新闻','财经评论','消费主张','正点财经']
    print("cctv2现在正在播放的是：{}".format(random.choice(shows)))
