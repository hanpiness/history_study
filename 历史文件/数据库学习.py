# show dbs
# 显示当前的所有数据库
# use 数据库名
# 进入到指定的数据库中
# db
# 表示的是当前所处的数据库
# show collections
# 显示数据库中的所有集合

#数据库的CRUD的操作
##向数据库中插入文档
###db.<collections>.insert(doc)
        # 向集合中插入一个文档

# 连接MongoDB
#import pymongo
#client = pymongo.MongoClient('mongodb://localhost',port = 27017)
#client = pymongo.MongoClient("mongodb://localhost:27017/")

# 连接Mongodb时，我们需要使用MongoClient传入MongoDB的IP端口即可
# 其中第一个参数为地址host第二个参数为端口port
# 第一个参数host还可以直接传入mongodb开头的字符串

# 指定数据库
#db = client.test
#db = client['test']

# 调用client的test属性即可返回test数据库


## 指定集合
# MongoDB的每个数据库包含许多集合

#collection = db.students

## 插入数据
#import pymongo

#client = pymongo.MongoClient(host='localhost',port = 27017)
#db = client.test
#collection = db.students
#student = {
#    'id':'20170101',
#    'name':'Jordan',
#    'age':'20',
#    'gender':'male'
#    }
#result = collection.insert(student)
#print(result)

# insert()方法可以插入数据
# 在Mongodb中，每条数据其实都有一个_id属性来唯一标识
# insert()方法执行后会返回_id值

#import pymongo

#client = pymongo.MongoClient(host='localhost',port = 27017)
#db = client.test
#collection = db.students
#student1 = {
#    'id':'20170101',
#    'name':'Jordan',
#    'age':'20',
#    'gender':'male'
#    }
#student2 ={
#    'id':'20170102',
#    'name':'Mike',
#    'age':'20',
#    'gendar':'male'
#    }
#result = collection.insert([student1,student2])
#print(result)

# 官方推荐使用insert_one()和insert_many()方法来
# 分别插入单条记录和多条记录

#import pymongo

#cilent = pymongo.MongoClient('mongodb://localhost:27017')
#bd = cilent.test
#collection = bd.students
#student1 = {
#    'id':'20170101',
#    'name':'Jordan',
#    'age':20,
#    'gender':'male'
#    }
#student2 ={
#    'id':'20170102',
#    'name':'Mike',
#    'age':20,
#    'gendar':'male'
#    }
#result = collection.insert_many([student1,student2])
#print(result)
#print(result.inserted_id)

# 与insert()方法不同,这次返回的是InsertOneResult对象
# 我们调用其inserted_id属性获取_id

# 查询
#result = collection.find_one({'name':'Mike'})
#print(type(result))
#print(result)

# 插入数据后，我们利用find_one()或find()方法查询
# find()返回一个生成器对象
#results = collection.find({'age':'20'})
#print(results)
#for result in results:
#    print(result)

# 如果要查询年龄大于20的数据

#results = collection.find({'age':{'$gt':20}})
# $gt 大于
# $gte 大于等于
# $lt 小于
# $lte 小于等于
# $ne 不等于
# $in 在范围内
# $nin 不在范围内

# 计数
#import pymongo

#cilent = pymongo.MongoClient('mongodb://localhost:27017')
#db = cilent.taobao
#collection = db.products
#count = collection.find().count()
#print(count)

# 排序
#results = collection.find().sort('name',pymongo.ASCENDING)
#print([result['name'] for result in results])

# 偏移
#在某些情况下，我们可能只想取某几个元素

#results = collection.find().sort('name',pymongo.ASCENDING).skip(2)
#print([result['name'] for result in results])
# 偏移2就忽略前两个元素，得到第三个及以后的元素

#results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
#print([result['name'] for result in results])
# limit()指定要取的结果个数

