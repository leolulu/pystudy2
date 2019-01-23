import pandas as pd
import pymysql
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib


conn = pymysql.connect('132.232.0.240', 'yxy', 'test', 'mydb')
sql = """SELECT * FROM gelbooru_anlaly g
where g.tag_list <> ''
and g.rating <> 'Questionable'
LIMIT 1000000"""

data = pd.read_sql(sql, conn)

tf = TfidfVectorizer()
bys = MultinomialNB(alpha=1)

x_train = tf.fit_transform(data.tag_list)
bys.fit(x_train, data.rating)

joblib.dump(tf, './图像处理相关/tf.pkl')
joblib.dump(bys, './图像处理相关/bys.pkl')
