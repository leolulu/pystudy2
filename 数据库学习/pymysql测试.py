import pymysql

db = pymysql.connect(host='132.232.0.240', port=3306, user='yxy', password='test', database='mydb')

cursor = db.cursor()

sql = '''insert into new_stock values(1233234,"shitsdfae","*9-23",2,2.223)'''
cursor.execute(sql)
db.commit()


db.close()
