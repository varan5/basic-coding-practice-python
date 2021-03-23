class Parent:
    def method1(self):
        print('Parent method')

class Child(Parent):
    def method1(self):
        super().method1()


c = Child()
c.method1()