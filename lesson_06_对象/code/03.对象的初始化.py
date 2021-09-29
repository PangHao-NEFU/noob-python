# class Person :
#     # 在类中可以定义一些特殊方法（魔术方法）
#     # 特殊方法都是以__开头，__结尾的方法：比如 __init__
#     # 特殊方法不需要我们自己调用，不要尝试去调用特殊方法
#     # 特殊方法将会在特殊的时刻自动调用
#     # 学习特殊方法：
#     #   1.特殊方法什么时候调用
#     #   2.特殊方法有什么作用
#     # 创建对象的流程
#     # p1 = Person()的运行流程
#     #   1.创建一个变量
#     #   2.在内存中创建一个新对象
#     #   3.__init__(self)方法执行
#     #   4.将对象的id赋值给变量

#     # init会在对象创建以后立刻执行
#     # init可以用来向新创建的对象中初始化属性
#     # 调用类创建对象时，类后边的所有参数都会依次传递到init()中
#     def __init__(self,name):          #当使用魔法方法时，创建实例时后面的参数会传给__init__中
#         # print(self)
#         # 通过self向新建的对象中初始化属性
#         self.name = name

#     def say_hello(self):
#         print('大家好，我是%s'%self.name)


# 目前来讲，对于Person类来说name是必须的，并且每一个对象中的name属性基本上都是不同
# 而我们现在是将name属性在定义为对象以后，手动添加到对象中，这种方式很容易出现错误
# 我们希望，在创建对象时，必须设置name属性，如果不设置对象将无法创建
#   并且属性的创建应该是自动完成的，而不是在创建对象以后手动完成
# p1 = Person()
# # 手动向对象添加name属性
# p1.name = '孙悟空'

# p2 = Person()
# p2.name = '猪八戒'

# p3 = Person()
# p3.name = '沙和尚'

# p3.say_hello()

# p1 = Person('孙悟空')
# p2 = Person('猪八戒')
# p3 = Person('沙和尚')
# p4 = Person('唐僧')
# p1.__init__() 不要这么做！！！

# print(p1.name)
# print(p2.name)
# print(p3.name)
# print(p4.name)

# p4.say_hello()

# #类的基本结构：
# class 类名([父类]):
#     公共属性.....
#     #对象的初始化方法
#     def __init__(self[,其他参数]):
#         ...

#     #其他方法
#     def method_1(self[,其他参数]):
#         ...
#     def method_2(self[,其他参数]):
#         ...




#练习：定义一个狗的类(dog)
    # 属性：name，age，gender，height...
    # 方法：jiao(),yao(),run()

class Dog :
    def __init__(self,name,age,gender,height):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height

    def jiao(self):
        print('%s朝你汪汪叫了两声'%self.name)

    def yao(self):
        print('你被%s咬了！'%self.name)

    def run(self):
        print('%s跑开了'%self.name)


jinmao=Dog('金毛','3','公','20')
jinmao.jiao()
jinmao.yao()
jinmao.run()

       











