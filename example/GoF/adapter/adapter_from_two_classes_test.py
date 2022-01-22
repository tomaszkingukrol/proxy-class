from src import proxyclass


class A:
    def __init__(self):
        self.a = 'A'


class B:
    def __init__(self):
        self.b = 'B'


@proxyclass
class MyAdapter:
    a: A
    b: B


def test_init_from_two_different_classes_as_kwargs():
    adapter = MyAdapter(a=A(), b=B())
    assert adapter.a.a == 'A'
    assert adapter.b.b == 'B'


def test_init_from_two_different_classes_as_args():
    adapter = MyAdapter(A(), B())
    assert adapter.a.a == 'A'
    assert adapter.b.b == 'B'
