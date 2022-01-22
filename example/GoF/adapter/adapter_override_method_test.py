from src.proxyclass import proxyclass


class A:
    def __init__(self, a):
        self.a = a

    def foo(self, x):
        return x

    def bar(self):
        return self.a


@proxyclass
class MyAdapter():
    a: A

    def bar(self):
        return self.a.bar() * 2


def test_override_method():
    adapter = MyAdapter(a=A(1))
    assert adapter.foo(x=1) == 1
    assert adapter.foo(1) == 1
    assert adapter.bar() == 2

