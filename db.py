import MySQLdb
import json
from flask import Flask
import os
app = Flask(__name__)


def create_query(low, size):
    q = ("select * from products left join links on products.pid=links.pid limit %s, %s;" % (low, size))
    return q


def db_api(sql, file_link):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="scoutlab")
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    with app.app_context():
        res = dict(zip(tuple(range(0, len(data))), data))
        print(res)
    open(file_link, 'w').close()
    with open(file_link, 'w', encoding='utf-8') as f:
        while os.stat(file_link).st_size != 0:
            print("Error: file is not empty!")
            open(file_link, 'w').close()
        json.dump(res, f, ensure_ascii=False, indent=4)

    cur.close()
    db.close()


def get_data(file_link):
    i = open(file_link)
    return json.load(i)


def get_rankings(sql, file_link):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="scoutlab")
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    with app.app_context():
        res = dict(zip(tuple(range(0, 10)), data))
        print(res)
    open(file_link, 'w').close()
    with open(file_link, 'w', encoding='utf-8') as f:
        while os.stat(file_link).st_size != 0:
            print("Error: file is not empty!")
            open(file_link, 'w').close()
        json.dump(res, f, ensure_ascii=False, indent=4)

    cur.close()
    db.close()
