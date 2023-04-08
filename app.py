import nltk
from flask import Flask, render_template
from collections import Counter
from nltk.corpus import stopwords
import numpy as np
app = Flask(__name__)


def df_maker(df, pname):
    p_df = df.loc[df['title'] == pname]
    return p_df


def df_filter(df, flag):
    if flag == 0:
        return df[df.rating <= 3]
    else:
        return df[df.rating > 3]


def word_breaker(li, stopword):
    newr = []
    for i in li:
        newr.append(i.lower())

    filtered_words = []
    # stop word removal
    for ele in newr:
        if ele not in stopword:
            filtered_words.append(ele)

    fil = [word for word in filtered_words if word not in stopwords.words('english')]
    sno = nltk.stem.SnowballStemmer('english')
    sm = []
    for i in fil:
        # stemming
        sm.append(sno.stem(i))

    return sm


def word_finder(df, col):
    li = df[col].tolist()
    tokenr = []
    for ele in li:
        # tokenize
        tokenr.append(np.array(nltk.word_tokenize(ele)))

    mat = np.array(tokenr)
    out = np.concatenate(mat).ravel().tolist()
    # change 'stopword' -> stopword
    word_list = word_breaker(out, 'stopword')
    if col == 'promise':
        # remove duplicates from desc
        word_list = set(word_list)
        word_list = list(word_list)

    return word_list


def match(desc_li, rev_li):
    # hash table
    hash_match = {}
    for word in desc_li:
        if rev_li.count(word) > 1:
            if hash_match.get(word) is None:
                hash_match[word] = rev_li.count(word)
    # number of matched words / total words in desc = ratio of delivery
    return len(hash_match)/len(desc_li)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('base.html')


@app.route("/rankings", methods=['GET', 'POST'])
def rankings():
    return render_template('rankings.html')


@app.route("/reviews", methods=['GET', 'POST'])
def reviews():
    return render_template('reviews.html')


@app.route("/pos-neg", methods=['GET', 'POST'])
def pos_neg():
    return render_template('pos_neg.html')


@app.route("/user-opinions", methods=['GET', 'POST'])
def user_opinions():
    return render_template('user_opinions.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)
