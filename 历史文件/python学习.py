#输出输入


#print("HELLO WORLD")
#print("hello","world")#遇到逗号，输出一个空格
#print("100+200=",100+200)
#name=input()#输入
#print(name)#输出
#name=input("please enter your name:")#不可回车
#print("hello,",name)
#print("1024 * 768 = ",1024*768)

#print("i\'m learning\npython")
#用r''表示''中的字符不需要转义

#print(r'\\\t\\')
#print('\\\t\\')

######用'''...'''可以表示多行内容，只能在交互模式下进行

#print('''line1
#line2
#line3''')

######布尔值经常用在条件判断中

#age=10
#if age>=18:
#    print('adult')
#else:
#    print('teenger')
#print(10%4)


######ord()函数获得字符的整数表示
######chr()函数编码转换为对应的字符
#print(ord('中'))
#print(chr(20013))

#a=3
#b=5
#print(r"%d\n"%a)

#name='Ma Yuansheng'
#print(name.lower())

######lower()把大写字母转换为小写
######upper()把小写字母转换为大写
######title()把首字母转换为改为大写

######rstrip()能删除多余的空格
#name='python '
#print(name,name.rstrip(),name)

######lstrip()能删除开头的空格
######strip()能删除两头的空格
#name=' python '
#print(name.strip()+'a')
#print(name.lstrip()+'a')

######用**表示乘方运算 空格不影响运算

#print(2**3)

######str()可以让非字符串表示为字符串

#age = 13
#print('happy '+age+'rd birthday')会错误
#而print("happy " +str(age)+"rd birthday!")正确


###################列表

######用[]表示列表，用逗号分隔其中的元素
######访问最后一个列表元素时提供了一个特殊的语法。通过索引指定为-1，可指向最后一个列表元素
######-2返回倒数第二个列表元素，-3返回倒数第三个列表元素，以此类推
######append(加入的元素)将元素增添到列表的末尾，不影响其他元素
######insert(索引的值，新元素)在列表任意位置添加新元素

######del 语句删除元素

#number=[1,2,3,4,5,6,7,8,9]
#del number[0]
#print(number)

######方法pop()可以让你删除列表末尾的元素，并接着使用它的值

#alph=['a','b','c']
#last_alph=alph.pop()
#print(last_alph)
#print(alph)

######实际上pop()可以删除列表中任何一个元素，只需在括号中指定要删除的元素的索引

#alph=['a','b','c']
#last_alph=alph.pop(1)
#print(last_alph)
#print(alph)

######如果你只知道要删除的值，不知道位置，可用remove(),remove()只删除了第一个出现的值

#alph=['a','b','c']
#alph.remove('a')
#print(alph)

######sort()可以永久性修改列表中的值，并按字母顺序排列
######sort(reverse=True)将会按字母顺序相反的顺序排列，也是永久性排列
######sorted()可用临时排列，同理，sorted(reverse=True)


#alph=['a','b','c']
#print(sorted(alph,reverse=True))

######reverse()可以反转列表元素的排列顺序，如果要恢复只需再次调用reverse()
######len()可以获得长度


#####################操作列表


##循环

#magicians=['alice','david','carolina']
#for magician in magicians:
#    print(magician.title()+'表演的太精彩了！')

#for value in range(1,5):
#    print(value)


######幂运算中左边的单目运算符优先级低，右边的单目运算符优先级高
#print(-1/9**-2)

######list()将range()的结构直接转换为列表。如果range()为list（）的一个参数，输出一个数字列表

#numbers = list(range(1,6))
#print(numbers[1])

######range()还可以定义步长，例如打印偶数
#for number in range(2,10,2):
#    print(number)



######min()最小值
######max()最大值
######sum()总和
#digital=[1,2,3,4,5,6,7,8,9]
#print(sum(digital))
#print(max(digital))
#print(min(digital))

           ######列表解析
#squares=[]
#for value in range(1,10):
#    squares.append(value**2)
#print(squares)

           ######可以简写为
#squares = [value**2 for value in range(1,10)]
#print(squares)

######切片
######如果要提取第2-4个的元素则应[1:4]
#numbers=[1,2,3,4,5,6,7,8,9,10]
#print(numbers[0:3])

######如果没有指定起始索引，则自动从表头开始
#numbers=[1,2,3,4,5,6,7,8,9,10]
#print(numbers[:4])

######如果要让切片止与列表末尾，也可以使用类似的语法
#numbers=[1,2,3,4,5,6,7,8,9,10]
#print(numbers[2:])

######如果你想输出后三个数字
#numbers=[1,2,3,4,5,6,7,8,9,10]
#print(numbers[-3:])

######遍历切片
#numbers=[1,2,3,4,5,6,7,8,9,10]
#for number in numbers[-3:]:
#    print(number)

######复制列表要用切片
#numbers1=[1,2,3,4,5,6,7,8,9,10]
#numbers2=[]
#numbers2=numbers1[:]
#print(numbers2)
#print(numbers1)

######如果直接使用numbers1=numbers2,这种语法实际上是将新numbers2关联到包含在numbers1中的列表，因此这两个变量都指向
######同一个列表
#numbers2=[]
#numbers1=[1,2,3,4,5,6,7,8,9,10]
#numbers2=numbers1
#numbers1.append(11)
#numbers2.append(12)
#print(numbers1)
#print(numbers2)



######元组一系列不可修改的元素
######元组使用圆括号而不是方括号。

#元组是不可以修改的。
#numbers=(10,20)
#numbers[0]=100

######修改元组变量,给元组变量赋值是合法的
#numbers=(10,100)
#print(numbers[:])
#numbers=(100,10)
#for number in numbers:
#    print(number)


######条件测试

######not in确定特定的值未包含在列表中
######in 可以检查列表中是否包含有特定元素
#number=list(range(1,11))
#if 1 not in number:
#    print('1不在列表中')
#elif 1 in number:
#    print('1在列表中')


#####检查列表是否为空，直接将列表名用在条件表达式中
#numbers=[]
#if numbers:
#    print('列表不为空')
#else:
#    print('列表为空')

######使用多个列表
#numbers1=[1,2,3,4,5,6,7]
#numbers2=[1,3,5,7,8]
#for number2 in numbers2:
#    if number2 in numbers1:
#        print('%d包含在列表numbers1中'%number2)
#    elif number2 not in numbers1:
#        print('%d不包含在列表numbers1中'%number2)

                  ######字典
######字典是一系列键—值对。每个键与一个值相关联
#person={'name':'马元帅','sex':'man'}
#print(person['name'])

######添加键-值对，依次指定字典名，用方括号括起来的键和相关联的值
#person={'name':'马元帅','sex':'man'}
#person['school']='中北大学'
#print(person)

######遍历字典
######items(),它返回一个键值对列表，遍历所有键值对。
#person={'first_name':'马','last_name':'元帅','age':'18','city':'太原'}
#for key,value in person.items():
#    print(key+':'+value)

######keys()遍历字典中的所有键
#person={'first_name':'马','last_name':'元帅','age':'18','city':'太原'}
#for key in person.keys():
#    print(key)

######遍历字典时，默认遍历所有键。
#person={'first_name':'马','last_name':'元帅','age':'18','city':'太原'}
#for key in person:
#    print(key)


######按顺序遍历字典中的所有键。
#person={'first_name':'马','last_name':'元帅','age':'18','city':'太原'}
#for name in sorted(person.keys()):
#    print(name)

######遍历字典中的所有值。
######value()遍历数组中的所有值。
#person={'first_name':'马','last_name':'元帅','age':'18','city':'太原'}
#for value in person.values():
#    print(value)

######值中可能有大量重复的数据，为剔除重复的数据可以集合set()，集合类似列表，但每一个元素都是独一无二的
#person={'first_name':'马','last_name':'元帅','age':'18','city':'太原'}
#for value in set(person.values()):
#    print(value)


######嵌套

######列表中使用字典

#person1={'name':'mayuansheng','sex':'man','location':'taiyuan'}
#person2={'name':'mayuan','sex':'man','location':'taiyuan'}
#person3={'name':'ma','sex':'man','location':'taiyuan'}
#persons=[person1,person2,person3]
#for person in persons:
#    for name in person.values():
#        print(name)

#创建30个马元帅
#person=[]
#创建空列表储存马元帅
#for person_numbeer in range(30):#使循环进行30次
#    new_person={'name':'mayuansheng','sex':'man','location':'taiyuan'}#进行初始化
#    person.append(new_person)#加到列表的末尾
#for perso in person[1:5]:
#    print(perso)


######在字典中储存列表

#number={'first':[1,2,3,4,5],'second':[6,7,8,9,10]}
#number['first'][0]=2#修改字典中列表的值
#for value in number.values():
#    print(value)

######有时候提示会超过一行，
#massage="If you tell us who you are ,we can personalize the message you see."
#massage+="\nWhat is your first name?"
#print(massage)
######使用int()来获取数值输入
#age=input("How old are you")
#if age >= 18:    #会报错因为input输入的为字符串不能与数值比较
#if int(age)>=18:
#    print(age)


######可使用while 删除所有cat、
#pets=['dog','cat','cat','cat','cat']
#while 'cat' in pets:
#    pets.remove('cat')
#print(pets)

######填充字典
#responses={}
#while True:
#    name2='姓名'
#    name1= input()
#    responses[name2]=name1
#    if(name1=='yuan'):
#        break
#print(responses)




##################函数定义
######def函数定义
######文档字符串的注释，描述函数做什么，由三引号括起
#"""显示简单的问候语"""

######位置传参

#def discribe_pet(animal_type,pet_name):
#    print(animal_type +pet_name)
#discribe_pet('dog','大黄' )

######关键字传参


#def discribe_pet(animal_type,pet_name):
#    print(animal_type +pet_name)
#discribe_pet(animal_type='dog',pet_name='大黄' )

######默认值，使用默认值时必须先列出没有默认值的形参，再列出有默认值的形参。
#def discribe_pet(pet_name,animal_type='dog'):
#    print(animal_type+' '+pet_name)
#discribe_pet('大黄')

#返回字典
#def person(first_name,last_name):
#    name={'firs_name':first_name,'las_name':last_name}
#    return name
#name=person('ma','yuan')
#print(name)

#禁止函数修改列表，可以使用切片传入副本
#列表被修改
#def numbe(number1):
#    number1.remove('2')
#number=['1','2','3','4','5']
#numbe(number)
#print(number)
#列表未被修改
#def numbe(number1):
#    number1.remove('2')
#number=['1','2','3','4','5']
#numbe(number[:])
#print(number)

######传递任意数量的实参
#def make_pizza(*toppings):
#    print(toppings)
#make_pizza("ad")
#make_pizza('ada','dad','daad')
######*toppings中的*是让python创建一个名为toppings的空元组，并将收到的值都封装到这个元组中
######如果还需要一个形参，则必须把*toppings放后面

######使用任意数量的关键字实参
#def build_profile(first,last,**user_info):
#    person={}
#    person['first_name']=first
#    person['last_name']=last
#    for key,value in user_info.items():
#        person[key]=value
#    return person
#person=build_profile('ma','yuan',location='taiyuan',age='18')
#print(person)

########将函数储存在模块内
#导入整个模块
#import pizza

#pizza.make_pizza(16,'pepperoni')
#pizza.make_pizza(12,'mushroom','green peppers','extra cheese')

#导入特定的函数
#from module_name import function_name
#可以导入任意数量的函数
#from module_name import function_1,function_2
#例
#from pizza import make_pizza

#make_pizza(16,'pepperoni')
#make_pizza(12,'mushroom','green peppers','extra cheese')

#使用as给函数指定别名
#from pizza import make_pizza as mp

#mp(16,'pepperoni')
#mp(12,'mushroom','green peppers','extra cheese')

#使用as给模块指定别名
#import pizza as mp

#mp.make_pizza(16,'pepperoni')
#mp.make_pizza(12,'mushroom','green peppers','extra cheese')

#导入模块中的所有函数
#使用*可以导入所有函数，由于导入了所有函数，可通过名称调用每个函数，无需句点
#from pizza import *

#make_pizza(16,'pepperoni')
#make_pizza(12,'mushroom','green peppers','extra cheese')


###############类
###以大写字母开头的名称指的是类
###方法__init__()中的 _ 为左右各两个，在定义这个方法时形参self必不可少
###self还必须位于其他形参的前面

#class User():
#    def __init__(self,first_name,last_name):
#        self.first_name=first_name
#        self.last_name=last_name
#    def describle_user(self):
#        print("user name is "+self.first_name.title()+' '+self.last_name.title())
#    def greet_user(self):
#        print("hello "+self.first_name+" "+self.last_name)

###Car类
#class Car():
#    """一次模拟汽车的简单尝试"""
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#        self.odometer_reading = 0
#    def get_descriptive_name(self):
#        long_name=str(self.year)+' '+self.make+' '+self.model
#        return long_name.title()
#my_new_car=Car('audi','a4','2016')
#print(my_new_car.get_descriptive_name())

###给属性默认值
#class Car():
#    """一次模拟汽车的简单尝试"""
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#        self.odometer_reading = 0
#    def get_descriptive_name(self):
#        long_name=str(self.year)+' '+self.make+' '+self.model
#        return long_name.title()
#    def read_odometer(self):
#        print("the car has "+str(self.odometer_reading)+' miles on it')
#my_new_car=Car('audi','a4','2016')
#print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()

###修改属性的值
# 1、通过实例修改
#class Car():
#    """一次模拟汽车的简单尝试"""
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#        self.odometer_reading = 0
#    def get_descriptive_name(self):
#        long_name=str(self.year)+' '+self.make+' '+self.model
#        return long_name.title()
#    def read_odometer(self):
#        print("the car has "+str(self.odometer_reading)+' miles on it')
#my_new_car=Car('audi','a4','2016')
#print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer=23#直接修改属性的值
#my_new_car.read_odometer()

# 2、通过方法修改属性的值
#class Car():
#    """一次模拟汽车的简单尝试"""
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#        self.odometer_reading = 0
#    def get_descriptive_name(self):
#        long_name=str(self.year)+' '+self.make+' '+self.model
#        return long_name.title()
#    def read_odometer(self):
#        print("the car has "+str(self.odometer_reading)+' miles on it')
#    def update_odometer(self,mileage):#通过定义了一个方法修改属性的值
#        """将里程表读数设置为指定的值"""
#       if mileage>=self.odometer_reading:
#        self.odometer_reading=mileage
#       else:
#       print("you can't roll back an odometer")
#my_new_car=Car('audi','a4','2016')
#print(my_new_car.get_descriptive_name())

#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

# 3、 通过方法将属性的值递增
#class Car():
#    """一次模拟汽车的简单尝试"""
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#        self.odometer_reading = 0
#    def get_descriptive_name(self):
#        long_name=str(self.year)+' '+self.make+' '+self.model
#        return long_name.title()
#    def read_odometer(self):
#        print("the car has "+str(self.odometer_reading)+' miles on it')
#    def update_odometer(self,mileage):#通过定义了一个方法修改属性的值
#        """将里程表读数设置为指定的值"""
#        self.odometer_reading=mileage
#    def increment_odometer(self,miles):#通过方法将属性的值递增
#        """将里程表读书增加到指定的值"""
#        self.odometer_reading+=miles
#my_new_car=Car('audi','a4','2016')
#print(my_new_car.get_descriptive_name())

#my_new_car.update_odometer(23500)
#my_new_car.read_odometer()
#my_new_car.increment_odometer(100)
#my_new_car.read_odometer()


######继承
###创建子类时，父类必须包含在当前文件中，且位于子类前面
###定义子类时，必须在括号内指定父类的名称。方法__init__()接受创建car实例所需的信息
###super()是一个特殊函数，帮助python将父类和子类关联起来
#class Car():
#    """一次模拟汽车的简单尝试"""
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#        self.odometer_reading = 0
#    def get_descriptive_name(self):
#        long_name=str(self.year)+' '+self.make+' '+self.model
#        return long_name.title()
#    def read_odometer(self):
#        print("the car has "+str(self.odometer_reading)+' miles on it')
#    def update_odometer(self,mileage):#通过定义了一个方法修改属性的值
#        """将里程表读数设置为指定的值"""
#        if mileage>=self.odometer_reading:
#            self.odometer_reading=mileage
#        else:
#            print("you can't roll back an odometer")


#class ElectricCar(Car):
#    def __init__(self,make,model,year):
#        super().__init__(make,model,year)
#        self.battery_size = 70

#    def discribe_battery(self):
#        print(" This car has a "+str(self.battery_size)+"kwh battery.")
#my_tesla =ElectricCar("tesla","model s","2016")
#print(my_tesla.get_descriptive_name())
#my_tesla.discribe_battery()

###重写父类的方法
###在子类中定义一个方法，即与要重写的父类方法同名。
###将实例用作属性，当类的细节越来越多时，属性和方法都越多，你可将大型类拆分成多个协同工作的小类。

#class Car():
#    """一次模拟汽车的简单尝试"""
#    def __init__(self,make,model,year):
#        self.make=make
#        self.model=model
#        self.year=year
#        self.odometer_reading = 0
#    def get_descriptive_name(self):
#        long_name=str(self.year)+' '+self.make+' '+self.model
#        return long_name.title()
#    def read_odometer(self):
#        print("the car has "+str(self.odometer_reading)+' miles on it')
#    def update_odometer(self,mileage):#通过定义了一个方法修改属性的值
#        """将里程表读数设置为指定的值"""
#        if mileage>=self.odometer_reading:
#            self.odometer_reading=mileage
#        else:
#            print("you can't roll back an odometer")

#class Battery():
#    def __init__(self,battery_size=70):
#        self.battery_size=battery_size
#    def discribe_battery(self):
#        print("This car has a "+str(self.battery_size)+"kwh battery.")
#    def get_range(self):
#        if self.battery_size == 70:
#            range = 240
#        elif self.battery_size == 85:
#            range = 270
#        message = "This car can go approximately " + str(range)
#        message += " miles on a full charge."
#        print(message)
#class ElectricCar(Car):
#    def __init__(self,make,model,year):
#        super().__init__(make,model,year)
#        self.battery=Battery()

#my_tesla =ElectricCar("tesla","model s","2016")
#print(my_tesla.get_descriptive_name())
#my_tesla.battery.discribe_battery()
#my_tesla.battery.get_range()

####导入类
#from car import Car
#class ElectricCar(Car):
#    def __init__(self,make,model,year):
#        super().__init__(make,model,year)
#        self.battery=Battery()

#my_tesla =ElectricCar("tesla","model s","2016")
#print(my_tesla.get_descriptive_name())
#my_tesla.battery.discribe_battery()
#my_tesla.battery.get_range()

###导入多个类,用逗号分隔
#from car import Car,ElectricCar

###导入整个模块
#import car

###导入模块中所有类
#from car import *

