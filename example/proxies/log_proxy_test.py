import logging
from src.proxyclass import proxyclass

class Concrete:
    def __init__(self, a):
        self.a = a

    def foo(self):
        return self.a


@proxyclass
class LogProxy:
    origin: Concrete

    def __init__(self, a):
        self.origin = Concrete(a)

    def _method_decorator(self, fn):
        def impl(*args, **kwargs):
            res = fn(*args, **kwargs)
            logging.getLogger().info(f'Logged output: {res}')
            return res
        return impl


def test_Log_proxy():
    p = LogProxy(1)
    assert p.origin is not None
    assert p.foo() == 1





