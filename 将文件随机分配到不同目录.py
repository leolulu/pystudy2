import os
import shutil
import math
import random
from PIL import Image
# 定义文件目录及变量
base_path = r'E:\python\pystudy2\public\konachan-sideboob'
dic_path = r'F:\F盘中转站\flower'
batch_dir_name = 'sideboob'
batch_capacity = 50
dic_path = os.path.join(dic_path, batch_dir_name)
# 读取文件列表
file_list = os.listdir(base_path)
random.shuffle(file_list)
dic_list = []
core_list = []
how_many_batch = math.floor(len(file_list) / batch_capacity)
num_of_last_batch = len(file_list) % batch_capacity
# 根据长宽比排序
for i in range(len(file_list)):
    core_list.append({'file_dir': os.path.join(base_path, file_list[i])})
for i in core_list:
    i['img_size'] = Image.open(i['file_dir']).size
for i in core_list:
    i['aspect_ratio'] = i['img_size'][0] / i['img_size'][1]
core_list.sort(key=lambda x: x['aspect_ratio'])
# 创建文件夹
# for i in range(10):
#     try:
#         os.mkdir('第{}批文件'.format(str(i+1)))
#     except Exception as e:
#         print(e)
for i in range(how_many_batch+1):
    new_dic_name = os.path.join(dic_path, str(i+1))
    os.makedirs(new_dic_name)
    dic_list.append(new_dic_name)
# 移动文件
# for i in range(10):
#     i = i+1
#     for j in range(11):
#         file_name = file_list.pop()
#         if os.path.splitext(file_name)[1] == '.txt':
#             print(file_name,str(i))
#             shutil.move(file_name,str(i))
for i in range(how_many_batch):
    for j in range(batch_capacity):
        shutil.move(core_list.pop()['file_dir'], dic_list[i])
for i in range(len(core_list)):
    shutil.move(core_list.pop()['file_dir'], dic_list[-1])
