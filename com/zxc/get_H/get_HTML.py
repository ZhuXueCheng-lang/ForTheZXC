import re

import requests
from bs4 import BeautifulSoup
F=[]
class Film:
    name=''
    Type=''
    msg=[]
    Torrent=[]
    TorrentURL=[]
    FilmURL=''

    def getList(self):
        list=[]
        I=0
        for m in self.msg:
            one={}
            one['name']=self.name
            one['Type']=self.Type
            one['doc']=m['doc']
            one['big']=m['big']
            one['objname']=m['name']
            one['img']=m['img']
            one['Torrent']=self.Torrent[I]
            one['FilmURL']=self.FilmURL
            one['id']=self.FilmURL+str(I)
            list.append(one)
            I+=1
        return list
        pass

    def setMsg(self,text):
        pp = re.split('【', text)
        name = ''
        big = 0
        for p in pp:
            o = re.split('】：', p)
            if o[0] in ['影片名称']:
                name = o[1]
            if o[0] in['影片大小','档案大小'] :

                if re.search('MB', o[1], flags=re.I):
                    big = float(re.split('MB', o[1], flags=re.I)[0])
                if re.search('G', o[1], flags=re.I):
                    big = float(re.split('G', o[1], flags=re.I)[0]) * 1024
        thisMsg={'doc':text,'name':name,'big':big,'img':[]}
        self.msg.append(thisMsg)
        pass

    def __init__(self,name,Type,URL):
        self.name=name
        self.Type+=Type
        self.FilmURL='https://cc.6hrz.icu/'+URL
        self.Torrent=[]
        self.TorrentURL=[]
        self.msg=[]
        html = requests.get(self.FilmURL)
        html.encoding = 'GBK'
        bf = BeautifulSoup(html.text, features="lxml")
        a_ls = bf.find_all('a')
        Ix=0
        for a in a_ls:
            a_text = a.text
            a_href = a.get('href')
            r_h=None
            if a_href!=None:
                r_h = re.search('hash', a_href)
            r = re.search('hash', a_text)
            if r != None:
                self.Torrent.append('http://www.rmdown.com/download.php?ref=' + a_text[r.span()[0]:])
                self.TorrentURL.append(a_text)
                a_p=a.find_parent()
                self.setMsg(a_p.text)
                img_ls=a_p.find_all('img')
                for img in img_ls:
                    p=img.get('data-src')
                    if re.search('jpg',p)!=None:
                        self.msg[Ix]['img'].append(str(p))
            elif r_h!=None:
                self.Torrent.append('http://www.rmdown.com/download.php?ref='+a_href[r.span()[0]:])
                self.TorrentURL.append('http://www.rmdown.com/link.php?' + a_href[r.span()[0]:])
                a_p = a.find_parent()
                self.setMsg(a_p.text)
                img_ls = a_p.find_all('img')
                for img in img_ls:
                    p=img.get('data-src')
                    if re.search('jpg',p)!=None:
                        self.msg[Ix]['img'].append(str(p))
            else:
                pass
            pass
        pass
    def __str__(self):
        show=self.name+'\t'+self.Type+'\t'+self.FilmURL+'\n'+'\t'
        for i in self.msg:
            show +=i['name']
            show +=str(i['big'])
        return show

def getFilm(i,Index,type):
    html = requests.get(f"https://cc.6hrz.icu/thread0806.php?fid={i}&page={Index}")
    html.encoding = 'GBK'
    bf = BeautifulSoup(html.text, features="lxml")
    itme_ls = bf.find_all('h3')
    for itme in itme_ls:
        href=itme.a.get('href')
        if len(str(href))==28:
            film=Film(itme.a.text,type,href)
            if len(film.msg)>0:
                F.append(film.getList())
                print(film.getList())
    return F
    pass
P=[[2,100,'亚洲无码'],[5,100,'里番动漫']]
if __name__ == '__main__':
    print(P)
    i=int(input ('数组索引：'))
    ii=int(input('第几页《100：'))
    getFilm(P[i][0], ii,P[i][2])


'''
暂时弃用
    def setTorrent(self):
        I=0
        for URL in self.TorrentURL:
            html = requests.get(URL)
            pattern = re.compile(r"var dlData = (.*?)$", re.MULTILINE | re.DOTALL)
            s = html.text
            lls = pattern.search(s).span()
            j = s[lls[0]:lls[1]]  # 87
            ls = re.split(f"<br>", j)
            code = re.split(': ', ls[0])[1]
            Downloaded = re.split(': ', ls[1])[1]
            self.Torrent.append('http://www.rmdown.com/download.php?ref=' + code)
            self.msg[I]['Downloaded'] = Downloaded
            I+=1
        pass
'''