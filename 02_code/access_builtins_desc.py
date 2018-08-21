class BuiltinsMixin:
    class ProxyDesc(object):  # object for 2.X
        def __init__(self, attrname):
            self.attrname = attrname

        def __get__(self, instance, owner):
            return getattr(instance._wrapped, self.attrname)  # Assume a _wrapped

    builtins = ['add', 'str', 'getitem', 'call']  # Plus others
    for attr in builtins:
        exec('__%s__ = ProxyDesc("__%s__")' % (attr, attr))

        # The loop does:
# __add__ = ProxyDesc("__add__")
# __str__ = ProxyDesc("__str__")
# ...
