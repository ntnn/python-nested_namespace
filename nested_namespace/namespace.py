""" Recursively set namespace. """


class NestedNamespace(object):
    """ Simple class to transform nested dicts to nested namespaces. """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, self.transform(value))

    @staticmethod
    def transform(target):
        """ Helper function to correctly transform values. """
        if isinstance(target, dict):
            return NestedNamespace(**target)
        if isinstance(target, list):
            return [NestedNamespace(**_) for _ in target]
        return target

    @staticmethod
    def retransform(target):
        """ Opposite to transform. """
        if isinstance(target, NestedNamespace):
            return target.as_dict()
        if isinstance(target, list):
            return [_.as_dict() for _ in target]
        return target

    def as_dict(self):
        """ Return namespace as dictionary. """
        result = {}
        for key, value in self.__dict__.items():
            result[key] = self.retransform(value)
        return result
