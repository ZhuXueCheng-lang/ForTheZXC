import pymysql
import com.zxc.get_H.get_HTML as H
class MySQLFiml(object):
    # 类的初始化
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306  # 端口号
        self.user = 'root'  # 用户名
        self.password = "root"  # 密码
        self.db = "fiml_h"  # 库
        self.table = "fiml"  # 表

    # 链接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')
    def insertFiml(self, fiml):
        table =self.table  # 要操作的表格
        # 注意，这里查询的sql语句url=' %s '中%s的前后要有空格
        sqlExit = f"SELECT * FROM {table}  WHERE id = ' %s '" % (fiml['id'])
        res = self.cursor.execute(sqlExit)
        if res:  # res为查询到的数据条数如果大于0就代表数据已经存在
            print("数据已存在", res)
            return 0
        # 数据不存在才执行下面的插入操作
        try:
            fiml['big']=str(fiml['big'])
            fiml['doc']=''
            fiml['img']='[\\"'+'",'.join(fiml['img'])+'\\"]'
            cols = ', '.join(fiml.keys())#用，分割
            values = '"," '.join(fiml.values())
            sql = f"INSERT INTO {table} (%s) VALUES (%s)" % (cols, '"' + values + '"')
            #拼装后的sql如下
            # INSERT INTO home_list (img_path, url, id, title) VALUES ("https://img.huxiucdn.com.jpg"," https://www.huxiu.com90.html"," 12"," ")
            try:
                result = self.cursor.execute(sql)
                #insert_id = self.conn.insert_id()  # 插入成功后返回的id
                self.conn.commit()
            except pymysql.Error as e:
                # 发生错误时回滚
                self.conn.rollback()
                # 主键唯一，无法插入
                if "key 'PRIMARY'" in e.args[1]:
                    print("数据已存在，未插入数据")
                else:
                    print("插入数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
        except pymysql.Error as e:
            print("数据库错误，原因%d: %s" % (e.args[0], e.args[1]))


class MySQLImg(object):
    # 类的初始化
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306  # 端口号
        self.user = 'root'  # 用户名
        self.password = "root"  # 密码
        self.db = "fiml_h"  # 库
        self.table = "Img"  # 表

    # 链接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')
    def insertFiml(self, Img):
        table =self.table  # 要操作的表格
        # 注意，这里查询的sql语句url=' %s '中%s的前后要有空格
        sqlExit = f"SELECT * FROM {table}  WHERE id = ' %s '" % (Img['id'])
        res = self.cursor.execute(sqlExit)
        if res:  # res为查询到的数据条数如果大于0就代表数据已经存在
            print("数据已存在", res)
            return 0
        # 数据不存在才执行下面的插入操作
        try:
            fiml['big']=str(fiml['big'])
            fiml['img']='['+','.join(fiml['img'])+']'
            cols = ', '.join(Img.keys())#用，分割
            values = '"," '.join(Img.values())
            sql = f"INSERT INTO {table} (%s) VALUES (%s)" % (cols, '"' + values + '"')
            #拼装后的sql如下
            # INSERT INTO home_list (img_path, url, id, title) VALUES ("https://img.huxiucdn.com.jpg"," https://www.huxiu.com90.html"," 12"," ")
            try:
                result = self.cursor.execute(sql)
                #insert_id = self.conn.insert_id()  # 插入成功后返回的id
                self.conn.commit()
            except pymysql.Error as e:
                # 发生错误时回滚
                self.conn.rollback()
                # 主键唯一，无法插入
                if "key 'PRIMARY'" in e.args[1]:
                    print("数据已存在，未插入数据")
                else:
                    print("插入数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
        except pymysql.Error as e:
            print("数据库错误，原因%d: %s" % (e.args[0], e.args[1]))


if __name__=='__main__':
    T=H.P[1]
    i=0
    list=[[{'name': '\u3000[犬江しんすけ] ひめさまおとし', 'Type': 'lif', 'doc': '漫画名字\u3000[犬江しんすけ] ひめさまおとし漫画语言\u3000中文漫画色彩\u3000黑白文件大小\u3000692MB图片格式\u3000JPG漫画页数\u3000220\u3000分辨率\u30002086X3000\xa0http://www.rmdown.com/link.php?hash=193666e15d222fca3d6e0d512d5026aee976449e3ef', 'big': '0', 'objname': '', 'img': ['https://www.x6img.com/u/20191005/13351167.jpg'], 'Torrent': 'http://www.rmdown.com/download.php?ref=hash=193666e15d222fca3d6e0d512d5026aee976449e3ef', 'FilmURL': 'https://cc.6hrz.icu/htm_data/1912/5/3733345.html', 'id': 'https://cc.6hrz.icu/htm_data/1912/5/3733345.html0'}]
,[{'name': '[三糸シド] 少女肉欲痴態~ラストフルフラワーズ~', 'Type': 'lif', 'doc': '漫画名字\u3000[三糸シド] 少女肉欲痴態~ラストフルフラワーズ~漫画语言\u3000中文漫画色彩\u3000黑白文件大小\u3000411MB图片格式\u3000JPG漫画页数\u3000214\u3000分辨率\u30002479X3800\xa0http://www.rmdown.com/link.php?hash=1934ebf17da0cc8c5c6aafc2ea36aac22d71d01102d', 'big': '0', 'objname': '', 'img': ['https://www.x6img.com/u/20191005/13344541.jpg'], 'Torrent': 'http://www.rmdown.com/download.php?ref=hash=1934ebf17da0cc8c5c6aafc2ea36aac22d71d01102d', 'FilmURL': 'https://cc.6hrz.icu/htm_data/1912/5/3733344.html', 'id': 'https://cc.6hrz.icu/htm_data/1912/5/3733344.html0'}]
]
    # while i<=0:
    #     list.extend(H.getFilm(T[0],i,T[2]))
    sqldb=MySQLFiml()
    sqldb.connectMysql()
    for fimls in list:
        for fiml in fimls:
            sqldb.insertFiml(fiml)
    pass
