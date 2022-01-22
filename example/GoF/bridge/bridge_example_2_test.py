from abc import ABC, abstractmethod

from src.proxyclass import proxyclass


class Interface(ABC):
    @abstractmethod
    def foo(self, type_):
        pass


class Implementation(Interface):
    def foo(self, type_):
        return f"I'm {type_}"


@proxyclass
class Abstraction(Interface):
    implementation: Implementation()

    def foo(self):
        return self.implementation.foo(self.type)


class A(Abstraction):
    def __init__(self):
        super().__init__()
        self.type = 'A'


class B(A):
    def __init__(self):
        super().__init__()
        self.type = 'B'


def test_overwrite_in_parent():
    a = A()
    b = B()
    assert a.foo() == "I'm A"
    assert b.foo() == "I'm B"
