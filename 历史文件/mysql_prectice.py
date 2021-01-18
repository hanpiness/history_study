import pymysql

# 1、连接数据库
# db = pymysql.connect(host='localhost', user='root', password='0310', port=3306)
# # 获取MYSQL的操作游标，利用游标来操作语句
# cursor = db.cursor()
# # 用execute方法执行SQL
# cursor.execute('SELECT VERSION()')
# # fetchone 获取第一条数据
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

# 2、创建表
# db = pymysql.connect(host='localhost', user='root', password='0310', port=3306)
# cursor = db.cursor()
# cursor.execute('use spiders')
# sql = 'CREATE TABLE IF NOT EXISTS students(id varchar(255) not null, name varchar(255) not null, age int not null,' \
#       ' primary key(id))'
# cursor.execute(sql)
# db.close()

# 3、插入数据
# id = '20210001'
# user = 'Bob'
# age = 20
# db = pymysql.connect(host='localhost', user='root', password='0310', port=3306)
# cursor = db.cursor()
# sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql, (id, user.age))
#     # 需要执行db的commit方法才可以实现数据的插入，这个方法才是真正将语句提交到数据库执行的方法
#     db.commit()
# except:
#     db.rollback()
# db.close()

# 改进
# data = {
#     'id': '20210002',
#     'name': 'Bob',
#     'age': 20
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# db = pymysql.connect(host='localhost', user='root', password='0310', port=3306)
# cursor = db.cursor()
# cursor.execute('use spiders')
# sql = 'INSERT INTO {table}({keys}) values({values})'.format(table=table, keys=keys, values=values)
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         # 需要执行db的commit方法才可以实现数据的插入，这个方法才是真正将语句提交到数据库执行的方法
#         print('Successful')
#         db.commit()
#
# except:
#     print('Failed')
#     db.rollback()
# db.close()

# 4、更新数据
# data = {
#     'id': '20120001',
#     'name': 'Bob',
#     'age': 21
# }
#
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s']*len(data))
#
# sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
#                                                                                     values=values)
# update = ', '.join([" {key} = %s".format(key=key) for key in data])
# sql += update
# db = pymysql.connect(host='localhost', user='root', password='0310', port=3306)
# cursor = db.cursor()
# cursor.execute('USE spiders')
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

# 5、删除数据
# table = 'students'
# condition = 'age > 20'
# db = pymysql.connect(host='localhost', user='root', password='0310', port=3306)
# cursor = db.cursor()
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute('USE spiders')
#     cursor.execute(sql)
#     db.commit()
#     print('Successful')
# except:
#     print('False')
#     db.rollback()
# db.close()

# 6、查询数据

sql = 'SELECT * FROM students WHERE age >=20'
db = pymysql.connect(host='localhost', user='root', password='0310', port=3306)
cursor = db.cursor()
cursor.execute('use spiders')
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results:', type(results))
    for row in results:
        print(row)
except:
    print('ERROR')

# 如果数据量很大时，通过fetchall()方法获取所有数据，占用的内存开销将会很大，
# 不建议使用fetchall()来获取全部数据，
# 而是用while循环加fetchone()方法获取数据
sql = 'SELECT * FORM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row', row)
        row = cursor.fetchone()
except:
    print('Error')
