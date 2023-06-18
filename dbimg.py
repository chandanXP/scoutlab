import json
import MySQLdb
from flask import Flask, jsonify

app = Flask(__name__)

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="scoutlab")
cur = db.cursor(MySQLdb.cursors.DictCursor)
sql = 'select * from links where pid<23010011'
cur.execute(sql)
user = cur.fetchall()


@app.route('/xyz')
def hello_world():
    with app.app_context():
        res = dict(zip(tuple(range(0, 11)), user))
        temp = jsonify(res)

        with open('data/display_image.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    app.run(debug=True, port=3000)


'''
@app.route('/')
def hello_world():
    with app.app_context():
        res = dict(zip(tuple(range(0, 11)), user))
        temp = jsonify(res)

        with open('display_image.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=4)
'''



