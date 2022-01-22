from abc import ABC, abstractmethod

from src import proxyclass


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


class A(Abstraction):
    def __init__(self):
        super().__init__()
        self.type = 'A'


def test_simple_bridge():
    ab = Abstraction()
    a = A()
    assert ab.foo('AB') == "I'm AB"
    assert a.foo(a.type) == "I'm A"

