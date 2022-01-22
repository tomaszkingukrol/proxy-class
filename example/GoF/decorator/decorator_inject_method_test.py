from src import proxyclass


class A:
    def __init__(self, a):
        self.a = a

    def foo(self, x):
        return x

    def bar(self):
        return self.a


@proxyclass
class MyDecorator:
    a: A

    def buz(self):
        return 1


def test_inject_method():
    decorator = MyDecorator(A(1))
    assert decorator.foo(x=1) == 1
    assert decorator.foo(1) == 1
    assert decorator.bar() == 1
    assert decorator.buz() == 1
