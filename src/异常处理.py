try:
    fh = open('./.gitignore1', 'r')
    print(
        fh.read()
    )
except:
    print('出错了')
else:
    fh.close()
    print('总之是运行完了')
