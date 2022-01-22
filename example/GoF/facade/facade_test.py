from src import proxyclass


class A:
    def __init__(self):
        self.a = 'foo'

    def foo(self):
        return self.a

    def buz(self):
        return 'bu'


class B:
    def __init__(self):
        self.b = 'bar'

    def bar(self):
        return self.b

    def buz(self):
        return 'z'


@proxyclass
class MyFacade:
    a: A
    b: B
    foo: A.foo
    bar: B.bar

    def buz(self):
        return self.a.buz() + self.b.buz()


def test_facade_by_kwargs():
    facade = MyFacade(a=A(), b=B())
    assert facade.foo() == 'foo'
    assert facade.bar() == 'bar'
    assert facade.buz() == 'buz'


def test_facade_by_args():
    facade = MyFacade(A(), B())
    assert facade.foo() == 'foo'
    assert facade.bar() == 'bar'
    assert facade.buz() == 'buz'
