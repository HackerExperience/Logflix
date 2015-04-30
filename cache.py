__cached__ = {}
__logs__ = {}
__list__ = []
consumer = None
con = None


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
