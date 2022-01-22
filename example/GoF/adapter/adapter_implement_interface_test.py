from abc import ABC, abstractmethod

from src.proxyclass import proxyclass


class Interface(ABC):
    @abstractmethod
    def foo(self): pass

    @abstractmethod
    def bar(self): pass


class A:
    def __init__(self):
        self.a = 'foo'

    def foo(self):
        return self.a


@proxyclass
class MyAdapter(Interface):
    a: A

    def bar(self):
        return 'bar'


def test_interface():
    adapter = MyAdapter(a=A())
    assert adapter.foo() == 'foo'
    assert adapter.bar() == 'bar'

