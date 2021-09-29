 # 可以在模块中定义变量，在模块中定义的变量，在引入模块后，就可以直接使用了
a = 10
b = 20

# 添加了_的变量，只能在模块内部访问，在通过import * 引入时，不会引入_开头的变量(开头为_的变量是私有的)
_c = 30

# 可以在模块中定义函数，同样可以通过模块访问到
def test():
    print('test')

def test2():
    print('test2')

# 也可以定义类    
class Person:
    def __init__(self):
        self.name = '孙悟空'

# 编写测试代码，这部分代码，只要当当前文件作为主模块的时候才需要执行
#   而当模块被其他模块引入时，不需要执行的，此时我们就必须要检查当前模块是否是主模块  
if __name__ == '__main__':  #这部分代码是测试用的，只有当此模块为主模块才执行，否则不执行
    test()
    test2()
    p = Person()
    print(p.name)