import os
import re
from sklearn.externals import joblib


base_dir = r'E:\python\pystudy2\public\yandere'
tf = joblib.load('./图像处理相关/tf.pkl')
bys = joblib.load('./图像处理相关/bys.pkl')

file_list_tuple = [(os.path.join(base_dir, i), ' '.join(i.split('.')[0].split('_')[1:])) for i in os.listdir(base_dir)]

for i in file_list_tuple:
    explicit_rating = round(bys.predict_proba(tf.transform([i[1]]))[0][list(bys.classes_).index('Explicit')], 2)

    if explicit_rating < 0.05:
        cated_rating = 'Safe(0-5)'
    if explicit_rating >= 0.05 and explicit_rating < 0.1:
        cated_rating = 'Safe(5-10)'
    if explicit_rating >= 0.1 and explicit_rating < 0.15:
        cated_rating = 'Safe(10-15)'
    if explicit_rating >= 0.15 and explicit_rating < 0.20:
        cated_rating = 'Safe(15-20)'
    if explicit_rating >= 0.20 and explicit_rating < 0.25:
        cated_rating = 'Safe(20-25)'
    if explicit_rating >= 0.25:
        cated_rating = 'Explicit({})'.format(explicit_rating)

    os.rename(i[0], re.sub(r"\\(\d+)_", r"\\{}_\1_".format(cated_rating), i[0]))
