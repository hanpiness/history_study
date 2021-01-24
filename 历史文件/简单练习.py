#练习

####调整名字的大小写
#name='ma yuansheng'
#print(name.lower())
#print(name.upper())
#print(name.title())


####名言

#print('Albert Einstein once said,"A person who never made a mistake never tired anything new."')


####剔除人名中的空白

#famous_person='\tMao Zhedong\n'
#print(famous_person)
#print(famous_person.lstrip())
#print(famous_person.rstrip())
#print(famous_person.strip())


####数到20
#for value in range(1,21):
#    print(value)

####一百万
#number=[]
#for number in range(1,1000001):
#    print(number)

####计算1—1000000的总和
#number=list(range(1,1000001))
#print(min(number))
#print(max(number))
#print(sum(number))

####奇数
#numbers=list(range(1,21,2))
#for number in numbers:
#    print(number)

####3的倍数
#numbers=list(range(3,31,3))
#for number in numbers:
#    print(number)

###立方
#numbers=[]
#for number in range(1,11):
#    numbers.append(number**3)
#print(numbers)

###解析立方
#numbers=[value**3for value in range(1,11)]
#print(numbers)

###人
#person={'first_name':'马','last_name':'原晟','age':'18','city':'太原'}
#print(person['first_name'])
#print(person['last_name'])
#print(person['age'])
#print(person['city'])

###餐馆
#class Restaurant():
#    """一个餐馆"""
#    #__init__前后有两个_
#    def __init__(self,restaurant_name,cuisine_type):
#        """初始化属性"""
#        self.restaurant_name=restaurant_name
#        self.cuisine_type=cuisine_type
#    def describe_restaurant(self):
#        print('my restaurant name is '+self.restaurant_name)
#        print("my restaurant type is "+self.cuisine_type)
#    def open_restaurant(self):
#        print("my restaurant is opening")

#restaurant=Restaurant('老四川','辣')
#print("my restaurant name is "+restaurant.restaurant_name.title())
#print("my restaurant name is "+restaurant.cuisine_type.title())
#restaurant.describe_restaurant()
#restaurant.open_restaurant()

###三家餐馆
#class Restaurant():
#    """一个餐馆"""
#    #__init__前后有两个_
#    def __init__(self,restaurant_name,cuisine_type):
#        """初始化属性"""
#        self.restaurant_name=restaurant_name
#        self.cuisine_type=cuisine_type
#    def describe_restaurant(self):
#        print('my restaurant name is '+self.restaurant_name)
#        print("my restaurant type is "+self.cuisine_type)
#    def open_restaurant(self):
#        print("my restaurant is opening")
#restaurant1=Restaurant("老四川","辣")
#restaurant2=Restaurant("湘水人家","甜")
#restaurant3=Restaurant("东北虎","贵")

###用户
#class User():
#    def __init__(self,first_name,last_name):
#        self.first_name=first_name
#        self.last_name=last_name
#    def describle_user(self):
#        print("user name is "+self.first_name.title()+' '+self.last_name.title())
#    def greet_user(self):
#        print("hello "+self.first_name+" "+self.last_name)
#user=User('ma','yuansheng')
#user.describle_user()
#user.greet_user()



###就餐人数

#class Restaurant():
#    """一个餐馆"""
#    def __init__(self,restaurant_name,cuisine_type):
#        """初始化属性"""
#        self.restaurant_name=restaurant_name
#        self.cuisine_type=cuisine_type
#        self.nember_served=0
#    def describe_restaurant(self):
#        print('my restaurant name is '+self.restaurant_name)
#        print("my restaurant type is "+self.cuisine_type)
#    def open_restaurant(self):
#        print("my restaurant is opening")
#    def set_number_served(self,number):
#        self.nember_served=number
#    def increment_number_served(self,crease_number):
#        self.nember_served+=crease_number
#restaurant=Restaurant("东北虎",'贵')
#print(restaurant.nember_served)
#restaurant.nember_served=5
#print(restaurant.nember_served)
#restaurant.set_number_served(10)
#print(restaurant.nember_served)
#restaurant.increment_number_served(5)
#print(restaurant.nember_served)


###冰激淋小店

#class Restaurant():
#    """一个餐馆"""
#    def __init__(self,restaurant_name,cuisine_type):
#        """初始化属性"""
#        self.restaurant_name=restaurant_name
#        self.cuisine_type=cuisine_type
#        self.nember_served=0
#    def describe_restaurant(self):
#        print('my restaurant name is '+self.restaurant_name)
#        print("my restaurant type is "+self.cuisine_type)
#    def open_restaurant(self):
#        print("my restaurant is opening")
#    def set_number_served(self,number):
#        self.nember_served=number
#    def increment_number_served(self,crease_number):
#        self.nember_served+=crease_number
#class IceCreamStand(Restaurant):
#    def __init__(self,restaurant_name,cuisine_type):
#        super().__init__(restaurant_name,cuisine_type)
#        self.flavors=["yogurt_ice_cream","sorbet"]
#    def my_flavors(self):
#        for my_flavor in self.flavors:
#            print("my flavor ice_cream is "+my_flavor.title())
#my_icecream=IceCreamStand("蜜雪冰城","贵")
#my_icecream.my_flavors()

# -*-coding: utf-8 -*-

#s1 = 72
#s2 = 85

#print('小明比去年成绩提升了%.1f %%'%((85-72)/72))
#print('小明比去年成绩提升了{0:.1f}%'.format((85-72)/72))

# -*- coding: utf-8 -*-

#L = [
#    ['Apple','Google','Microsoft'],
#    ['Java','python','Ruby','PHP'],
#    ['Adam','Bart','Lisa']
#    ]
#print(L[1][2]);

#cannot modify tuple
#T = ('m','a')
#T[0] = 'a'
#print(T)


#s = 65/(1.8)**2
#if s < 18.5:
#    print('过轻')
#elif s < 25:
#    print('正常')
#elif s < 28:
#    print("过重")
#elif s <32:
#    print("肥胖")
#else :
#    print("严重肥胖")


#新奇的尝试

#a = {'a':(1,[2,3]),'b':90,(1,2,3):123}
#b = {'a',(1,[2,3])}

# -*- coding: utf-8 -*-

#n1 = 255
#n2 = 1000
#n1 = '%x' % 255
#print("%X"%255)
#n2 = hex(n2)
#print(n1,n2)

#
#def my_abs(n):
#    if n < 0:
#        n = -n
#    return n


#print(my_abs(-99))

#一元二次方程组

#import math
#def quadratic(a, b, c):
#    n1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
#    n2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
#    return n1,n2
## 测试:
#print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
#print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

#if quadratic(2, 3, 1) != (-0.5, -1.0):
#    print('测试失败')
#elif quadratic(1, 3, -4) != (1.0, -4.0):
#    print('测试失败')
#else:
#    print('测试成功')

#def product(*numbers):
#    if not numbers:
#        sum = 0
#    else:
#        sum = 0
#    for number in numbers:
#        sum = number * sum
#    return sum
# 测试
#print('product(5) =', product(5))
#print('product(5, 6) =', product(5, 6))
#print('product(5, 6, 7) =', product(5, 6, 7))
#print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
#if product(5) != 5:
#    print('测试失败!')
#elif product(5, 6) != 30:
#    print('测试失败!')
#elif product(5, 6, 7) != 210:
#    print('测试失败!')
#elif product(5, 6, 7, 9) != 1890:
#    print('测试失败!')
#elif product() != 0:
#    print("测试失败！")
#else:
#    print("测试成功！")

###汉诺塔
#def move(n,a,b,c):
#    if n == 1:
#        print("%c->%c"%(a,c))
#    else:
#        move(n-1,a,c,b)
#        print("%c->%c"%(a,c))
#        move(n-1,b,a,c)
#move(3,'A','B','C')


#切片
#def trim(s):
#    if s[:1] == ' ':
#        s=s[1:]
#    if s[-1:] == ' ':
#        s=s[:-1]
#    return s
## 测试:
#if trim('hello ') != 'hello':
#    print('测试失败!')
#elif trim(' hello') != 'hello':
#    print('测试失败!')
#elif trim(' hello ') != 'hello':
#    print('测试失败!')
#elif trim(' hello world ') != 'hello world':
#    print('测试失败!')
#elif trim('') != '':
#    print('测试失败!')
#elif trim(' ') != '':
#    print('测试失败!')
#else:
#    print('测试成功!')

#def findMinAndMax(L):
#    if not L:
#        return (None,None)
#    else:
#        max = L[0]
#        min = L[0]
#        for LS in L:
#           if max < LS:
#               max = LS
#           if min > LS:
#               min = LS
#        return (min,max)
## 测试
#if findMinAndMax([]) != (None, None):
#    print('测试失败!')
#elif findMinAndMax([7]) != (7, 7):
#    print('测试失败!')
#elif findMinAndMax([7, 1]) != (1, 7):
#    print('测试失败!')
#elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#    print('测试失败!')
#else:
#    print('测试成功!')

#L = [x * x for x in range(1,11)]
#print(L)

#def build_profile(first_name,last_name,**qita):
#    print(first_name)
#    print(last_name)
#    print(qita)
#class Restaurant():
#    def __init__(self,restaurant_name,cuisine_type):
#        self.restaurant_name = restaurant_name
#        self.cuisine_type = cuisine_type
#        self.number_served = 0
#    def describe_restaurant(self):
#        print(self.restaurant_name+'is a '+self.cuisine_type+'restaurant')
#    def open_restaurant(self):
#        print(self.restaurant_name+"is openning")

#    def set_number_served(self):
#        self.number_served = 3

#    def increment_number_served(self):
#        self.number_served += 10
#class User():
#    def __init__(self, first_name,last_name):
#        self.first_name = first_name
#        self.last_name = last_name
#        self.login_attempts = 0

#    def discribe_user(self):
#        print("username is "+ self.first_name.title()+" "+self.last_name.title())
#    def greet_user(self):
#        print("Hello " + self.first_name +" "+ self.last_name)

#    def increment_login_attempts(self):
#        self.login_attempts += 1

#    def reset_login_attempts(self):
#        self.login_attempts = 0