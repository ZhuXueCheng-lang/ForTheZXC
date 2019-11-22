from elasticsearch import Elasticsearch
import requests
from bs4 import BeautifulSoup
es = Elasticsearch('127.0.0.1:9200')
mappings = {
            "mappings": {
                "book": {
                    "properties": {
                        "id": {
                            "type": "long",
                            "index": "false"
                        },
                        "name": {
                            "type": "text",
                            "index": "true"
                        },
                        "URL": {
                            "type": "text",
                            "index": False
                        },
                        "tags": {
                            "type": "object",
                            "properties": {
                                "bookType": {"type": "text", "index": True},
                                "Author": {"type": "keyword", "index": True}
                            }
                        }
                    }
                }
            }
        }
res = es.indices.create(index = 'biqu_book',body =mappings)
def putOne(type,id,li):
    bf=BeautifulSoup(li,features="lxml")
    URL=bf.find('a').get('href')
    Msg=bf.text.split('/')
    name=Msg[0]
    author=Msg[1]
    action = {
        "id": f"{id}",
        "name": f"{name}",
        "URL": f"{URL}",
        # 以下tags.content是错误的写法
        # "tags.content" :"标签2",
        # "tags.dominant_color_name": "域名的颜色黄色",
        # 正确的写法如下：
        "tags": {"bookType": f"{type}", "Author": f"{author}"},
        # 按照字典的格式写入，如果用上面的那种写法，会直接写成一个tags.content字段。
        # 而不是在tags中content添加数据，这点需要注意
    }
    es.index(index="biqu_book", doc_type="book", body=action)
if __name__=='__main__':
    html=requests.get("https://www.nbiquge.com/quanbuxiaoshuo/")
    html.encoding='GBK'
    bf = BeautifulSoup(html.text,features="lxml")
    itme_ls = bf.find_all('div', class_='novellist')
    theid=0
    for itme in itme_ls:
        bf=BeautifulSoup(str(itme),features="lxml")
        type=BeautifulSoup(str(bf.find('h2')),features="lxml").text
        print(type)
        li_ls = BeautifulSoup(str(bf.find('ul')),features="lxml").find_all('li')
        for li in li_ls:
            theid+=1
            putOne(type, theid,str(li))

