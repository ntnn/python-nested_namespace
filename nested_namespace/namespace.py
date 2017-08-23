""" Recursively set namespace. """

from types import SimpleNamespace


class NestedNamespace(SimpleNamespace):
    """ Simple class to transform nested dicts to nested namespaces. """
    def __init__(self, **kwargs):
        self.__dict__.update(
            {k: self.transform(kwargs[k])
             for k in kwargs}
        )

    def __setattr__(self, name, value):
        SimpleNamespace.__setattr__(self, name, self.transform(value))

    @staticmethod
    def transform(target):
        """ Helper function to correctly transform values. """
        if isinstance(target, dict):
            return NestedNamespace(**target)
        if isinstance(target, list):
            return [NestedNamespace(**_) for _ in target]
        return target
