from src import proxyclass


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

    def buz(self):
        return 1


def test_inject_new_method():
    adapter = MyAdapter(A(1))
    assert adapter.foo(x=1) == 1
    assert adapter.foo(1) == 1
    assert adapter.bar() == 1
    assert adapter.buz() == 1
