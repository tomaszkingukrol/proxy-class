from src import proxyclass

class Concrete:
    def __init__(self, a):
        self.a = a

    def foo(self):
        return self.a


class PermissionError(Exception):
    pass


def check_permission():
    ...
    return True


@proxyclass
class LogProxy:
    origin: Concrete

    def __init__(self, a):
        self.origin = Concrete(a)

    def _method_decorator(self, fn):
        def impl(*args, **kwargs):
            if check_permission():
                res = fn(*args, **kwargs)
                return res
            else:
                raise PermissionError()

        return impl


def test_Log_proxy():
    p = LogProxy(1)
    assert p.origin is not None
    assert p.foo() == 1





