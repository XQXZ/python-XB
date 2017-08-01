#知识点
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
#试图绑定限定之外的属性将得到AttributeError的错误
#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


#练习
# -*- coding: utf-8 -*-

class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('score')

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, score)
        self.score = score

#test
s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print(s.score)
