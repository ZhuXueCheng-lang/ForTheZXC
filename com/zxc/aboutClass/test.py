# -*-coding:utf8-*-
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import time
import sys
import re
import json
import MySQLdb


# id av cid title tminfo time click danmu coins favourites duration honor_click honor_coins honor_favourites
# mid name article fans tags[3] common

urls = ['http://bilibili.com/video/av77547675']

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}
html = requests.get(urls[0], headers=head)
text = '''
<div>
    <ul>
        <li class="sp item-0" name="one"><a href="www.baidu.com">baidu</a>
        <li class="sp item-1" name="two"><a href="https://blog.csdn.net/qq_25343557">myblog</a>
        <li class="sp item-2" name="two"><a href="https://www.csdn.net/">csdn</a>
        <li class="sp item-3" name="four"><a href="https://hao.360.cn/?a1004">hao123</a>
'''
selector = etree.HTML(text)
content = selector.xpath("//a/text()")
print(html.text)
print('-----------------------------')
print(content)