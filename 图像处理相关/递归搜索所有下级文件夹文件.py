import os

class RecursionFileSerach:
    '''
    递归搜索所有下级文件夹文件
    '''
    def __init__(self,base_dir):
        self.path = base_dir
        self.total_path_file_list = []
    def recursionFileSerach(self,path):
        file_list = [os.path.join(path,i) for i in os.listdir(path)]
        inner_file_num = sum([1 if os.path.isfile(i) == True else 0 for i in file_list])
        inner_dir_num = sum([1 if os.path.isdir(i) == True else 0 for i in file_list])
        inner_file_list = [i for i in file_list if os.path.isfile(i) == True]
        inner_dir_list = [i for i in file_list if os.path.isdir(i) == True]
        self.total_path_file_list.extend(inner_file_list)
        if inner_dir_num != 0:
            for inner_dir in inner_dir_list:
                self.recursionFileSerach(inner_dir)
    def run(self):
        self.recursionFileSerach(self.path)
        return self.total_path_file_list

if __name__ == '__main__':
    r1 = RecursionFileSerach(r'E:\Python\PycharmProjects\pystudy3-data-analysis\数据分析项目实战\陌陌财报分析')
    x=r1.run()
    print([i for i in x if i.find('验证')!=-1])