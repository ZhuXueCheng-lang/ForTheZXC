# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

"""
从www.biqubao.com笔趣阁爬取小说，楼主教程中的网址我当时没打开，
就参照楼主教程，爬取了笔趣阁小说网的内容。
    2018-07-31
"""
def DownloadBook(target):
    # 本地保存爬取的文本根路径
    save_path = 'Book'
    # 笔趣阁网站根路径
    global index_path
    req = requests.get(url=target)
    # 查看request默认的编码，发现与网站response不符，改为网站使用的gdk
    print(req.encoding)
    req.encoding = 'gbk'
    # 解析html
    soup = BeautifulSoup(req.text, "html.parser")
    list_tag = soup.div(id="list")
    print('list_tag:', list_tag)
    # 获取小说名称
    story_title = list_tag[0].dl.dt.string
    # 根据小说名称创建一个文件夹,如果不存在就新建
    dir_path = save_path + '/' + story_title
    if not os.path.exists(dir_path):
        os.path.join(save_path, story_title)
        os.mkdir(dir_path)
    # 开始循环每一个章节，获取章节名称，与章节对应的网址
    for dd_tag in list_tag[0].dl.find_all('dd'):
        # 章节名称
        chapter_name = dd_tag.string
        # 章节网址
        chapter_url = index_path + dd_tag.a.get('href')
        # 访问该章节详情网址，爬取该章节正文
        chapter_req = requests.get(url=chapter_url)
        chapter_req.encoding = 'gbk'
        chapter_soup = BeautifulSoup(chapter_req.text, "html.parser")
        # 解析出来正文所在的标签
        content_tag = chapter_soup.div.find(id="content")
        # 获取正文文本，并将空格替换为换行符
        content_text = str(content_tag.text.replace('\xa0', '\n'))
        # 将当前章节，写入以章节名字命名的txt文件
        with open(dir_path + '/' + chapter_name + '.txt', 'w') as f:
            f.write('本文网址:' + chapter_url)
            f.write(content_text)
def getURL(**Filter):
    global index_path
    if 'keyWord' in Filter:
        keyWord=Filter.get('keyWord')
        html=requests.get(index_path+f'/search.php?keyword={keyWord}')
        bf = BeautifulSoup(html.text)
        itme_ls=bf.find_all('div',class_='result-item result-game-item')
        bookURL_ls=[]
        for item in itme_ls:
            b=str(BeautifulSoup(str(item)).find('div', class_="result-game-item-pic"))
            a=BeautifulSoup(b).find('a').get('href')
            bookURL_ls.append(a)
        return bookURL_ls
if __name__=='__main__':
    index_path = 'https://www.biqubao.com'
    i=input('请输入要下载的书名：')
    URL_ls=getURL(keyWord=i)
    for URL in URL_ls:
        DownloadBook(URL)


