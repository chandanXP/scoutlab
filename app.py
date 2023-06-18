from flask import request
from flask import Flask, render_template
from db import get_data, create_query, db_api

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    button_value = request.args.get('button_value')
    print(button_value)
    low = 0
    table = 'products'
    # loading in browser
    if button_value is None:
        low = 0
    else:
        low = (int(button_value)-1)*30
        # 60
    sql = create_query(low, 30)
    db_api(sql, 'C:\scoutlab\data\post.json')
    data = get_data('C:\scoutlab\data\post.json')
    return render_template('index.html', data=data)


@app.route("/rankings", methods=['GET', 'POST'])
def rankings():
    sql = "select pid, pname, r_score  from products order by r_score DESC limit 10"
    db_api(sql, 'data/rankings.json')
    ranks = get_data('data/rankings.json')
    return render_template('rankings.html', ranks=ranks)


@app.route("/reviews", methods=['GET', 'POST'])
def reviews():
    sql = "select pid, pname, rcount  from products order by rcount DESC limit 10"
    db_api(sql, 'data/rankings.json')
    review = get_data('data/rankings.json')
    return render_template('reviews.html', review=review)


@app.route("/pos-neg", methods=['GET', 'POST'])
def pos_neg():
    sql = "select pid,pname,pos_count,neg_count,(pos_count-neg_count) as diff from products order by diff DESC limit 10"
    db_api(sql, 'data/rankings.json')
    diff = get_data('data/rankings.json')
    return render_template('pos_neg.html', diff=diff)


@app.route("/user-opinions", methods=['GET', 'POST'])
def user_opinions():
    return render_template('user_opinions.html')


@app.route("/product", methods=['GET', 'POST'])
def product():
    val_ = request.form['product_name']
    sql_ = ("select * from products left join links on products.pid=links.pid where instr(pname, '%s') > 0" % val_)
    db_api(sql_, "data/search.json")
    data = get_data("data/search.json")
    print(data)
    return render_template('index.html', data=data)


@app.errorhandler(404)
def page_not_found(e):
    # your processing here
    return render_template('page404.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)


