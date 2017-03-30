#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

class DBHelper:
    def __init__(self, host, username, password, port, charset, dbname):
        self.host = "127.0.0.1" if host == '' else host
        self.username = "root" if username == '' else username
        self.password = "root" if password == '' else password
        self.port = "3306" if port == '' else port
        self.charset = "gbk" if charset == '' else charset
        self.dbname = "mysql" if dbname == '' else dbname

    def getConn(self):
        conn = MySQLdb.connect(host=self.host, user=self.username, passwd=self.password, port=int(self.port),db=self.dbname,charset=self.charset)

        return conn

    def closeDB(self,conn):
        if conn == '':
            return 0
        else:
            conn.close()
            return 1

    def query(self, conn, sql):
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        for row in result:
            print("-" * 50)  # 输出50个-,作为分界线
            print row

    def update(self, conn, sql):
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        print result

    def delete(self, conn, sql):
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        print result

    def insert(self, conn, sql):
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        print result

if __name__ == '__main__':
    db = DBHelper(host='127.0.0.1',username='root',password='root',port='3306',dbname='',charset='gbk')
    conn = db.getConn()
    sql = u'SELECT * FROM  db'
    db.query(conn=conn,sql=sql)

