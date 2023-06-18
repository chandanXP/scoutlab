import MySQLdb
import json
from flask import Flask
import os
app = Flask(__name__)


# query = "select pid, pname, r_score  from products order by r_score DESC"
searchValue = "Mivi"
# sql_ = ("select pid, pname, r_score from products where instr(pname, '%s') > 0;" % (searchValue))
q = ("select * from products left join links on products.pid=links.pid where instr(pname, '%s') > 0" % (searchValue))
# link = 'data/search.json'
# sql = ("select * from %s limit %s, %s;" % (table, low, size))


def get_rankings(sql, file_link):
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


get_rankings(q, "data/search.json")
