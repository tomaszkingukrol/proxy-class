from src.proxyclass import proxyclass

class Concrete:
    def __init__(self, a):
        self.a = a

    def foo(self):
        return self.a


@proxyclass
class LazyProxy:
    origin: Concrete

    def __init__(self, a):
        self.origin = None
        self.a = a

    def _method_decorator(self, fn):
        def impl(*args, **kwargs):
            if not self.origin: 
                self.origin = Concrete(self.a)
            res = fn(*args, **kwargs)
            return res
        return impl


def test_lazy_proxy():
    p = LazyProxy(1)
    assert p.origin is None
    p.foo()
    assert p.origin is not None

