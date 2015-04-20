__cached__ = {}
__requests__ = {}
__pending_requests__ = []
__waiting_requests__ = []
ws = None


def call(name):

    if name in __cached__:
        if callable(__cached__[name]):
            __cached__[name] = __cached__[name]()
        return __cached__[name]
    raise NotImplementedError


def register(name, klass):
    if name in __cached__:
        raise NotImplementedError
    __cached__[name] = klass
