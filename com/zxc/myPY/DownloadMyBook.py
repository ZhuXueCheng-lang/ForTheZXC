# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import time
from elasticsearch import Elasticsearch
import threading
from concurrent.futures import ThreadPoolExecutor


es = Elasticsearch('http://localhost:9200')
#通用网络超时自关闭线程

def DownloadBook(target):
    global DownTime
    global book
    global pool

    # 笔趣阁网站根路径
    index_path='https://www.nbiquge.com'
    req = requests.get(url=target)
    # 查看request默认的编码，发现与网站response不符，改为网站使用的gdk
    print(req.encoding)
    req.encoding = 'gbk'
    # 解析html
    soup = BeautifulSoup(req.text, "html.parser")
    list_tag = soup.find_all('div',id="list")
    # 获取小说名称
    bookname = list_tag[0].dl.dt.string

    print(bookname+'开始下载')
    # 开始循环每一个章节，获取章节名称，与章节对应的网址
    index = 0
    for dd_tag in list_tag[0].dl.find_all('dd'):
        # 章节名称
        chapter_name = dd_tag.string
        # 章节网址
        chapter_url = index_path + dd_tag.a.get('href')
        book[str(index)]=Chapter(chapter_name,chapter_url)
        index+=1
    DownTime = index
    t1=pool.submit(DownINpc,bookname)
    indexD =0
    while indexD<=index:
        chapter=book[str(indexD)]
        pool.submit(DownInMap, chapter)
        indexD+=1

def DownInMap(Chapter):
    URL=Chapter.URL
    # 访问该章节详情网址，爬取该章节正文
    chapter_req = requests.get(url=URL)
    chapter_req.encoding = 'gbk'
    chapter_soup = BeautifulSoup(chapter_req.text, "html.parser")
    # 解析出来正文所在的标签
    content_tag = chapter_soup.div.find(id="content")
    # 获取正文文本，并将空格替换为换行符
    content_text = str(content_tag.text.replace('\xa0', ''))
    Chapter.putContent(content_text)
    print(Chapter.name)
    return
#章节封装类
class Chapter:
    Start=False
    content=''
    URL=''
    name=''
    ok=False
    #构造函数
    def __init__(self,name,url):
        self.name=name
        self.URL=url
    #内容存入
    def putContent(self,content):
        self.content=content
        self.ok=True


#吧book存入本地
def DownINpc(name):
    global DownTime
    global book
    # 本地保存爬取的文本根路径
    save_path = 'Book'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    # 根据小说名称创建一个文件夹,如果不存在就新建
    dir_path = save_path + '/' + name
    if not os.path.exists(dir_path):
        os.path.join(save_path, name)
        os.mkdir(dir_path)
    time.sleep(3)
    with open(dir_path + '/' +name + '.txt', 'w') as f:
        index=0
        wite=0
        while index<=DownTime:
            txt=book[str(index)]
            if txt.ok:
                f.write(f'\n\n第{str(index+1)}章\n'+ txt.name + '\n'+ txt.URL)
                f.write(txt.content)
                print(txt.name+'写入完毕')
                del book[str(index)]
                index+=1
            else:
                if wite<20:
                    wite += 1
                    time.sleep(1)
                else:
                    wite=0
                    f.write(f'\n\n第{str(index + 1)}章\n' + txt.name + '\n' + txt.URL)
                    f.write('连接超时')
                    print(f'第{str(index + 1)}章下载失败')
                    index += 1



#查询模块
def findURL(thetype,keyWord):
    doc = {
        "query": {
            "match": {
                f"{thetype}": f"{keyWord}"
            }
        },
        "from": 1,
        "size": 100
    }
    res = es.search(index="biqu_book", body=doc)
    itme=res.get('hits').get('hits')
    url=[]
    index=0
    for book in itme:
        msg=book.get('_source')
        print('++-----------------------------------++')
        print(f'id :{index}')
        print(f'书名 ：{msg.get("name")}')
        print(f'类型 ：{msg.get("tags").get("bookType")}')
        print(f'作者 ：{msg.get("tags").get("Author")}')
        url.append(msg.get('URL'))
        index+=1
    print('++-----------------------------------++')
    id=int(input("\n\n请输入要想下载的书的ID :"))
    return url[id]
if __name__=='__main__':
    i=['name','tags.Author','tags.bookType']
    ipt=input("选择搜索方式： 0:书名   1：作者   2：小说类型")
    thetype=i[int(ipt)]
    keyWord=input("请输入关键字：")
    url=findURL(thetype,keyWord)
    DownTime=True
    book={}
    pool = ThreadPoolExecutor(max_workers=30)
    DownloadBook(url)