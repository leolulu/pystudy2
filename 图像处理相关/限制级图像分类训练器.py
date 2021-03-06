import pandas as pd
import pymysql
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib


def timeprint(*args):
    import datetime
    print('['+datetime.datetime.now().strftime('%F %X')+']', end=' ')
    for i in args[:-1]:
        print(i, end=' ')
    print(args[-1])


conn = pymysql.connect('132.232.0.240', 'yxy', 'test', 'mydb')
sql = """SELECT * FROM gelbooru_anlaly g
where g.tag_list <> ''
and g.rating <> 'Questionable'"""

timeprint('开始下载数据...')
data = pd.read_sql(sql, conn)
timeprint('数据下载完毕...')

tf = TfidfVectorizer()
bys = MultinomialNB(alpha=1)


timeprint('开始训练...')
x_train = tf.fit_transform(data.tag_list)
bys.fit(x_train, data.rating)
timeprint('训练完毕...')

joblib.dump(tf, './tf.pkl')
joblib.dump(bys, './bys.pkl')
timeprint('模型保存完毕...')
