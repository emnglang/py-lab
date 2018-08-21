class BuiltinsMixin:
    def reroute(self, attr, *args, **kargs):
        return self.__class__.__getattr__(self, attr)(*args, **kargs)

    def __add__(self, other):                                             
        return self.reroute('__add__', other)         
    def __str__(self):
        return self.reroute('__str__')        
    def __getitem__(self, index):
        return self.reroute('__getitem__', index)
    def __call__(self, *args, **kargs):
        return self.reroute('__call__', *args, **kargs)

    # Plus any others used by wrapped objects in 3.X only
