Nested Namespace
================

Simple nested namespaces.

.. code:: python

    In [1]: from nested_namespace import NestedNamespace

    In [2]: x = NestedNamespace()

    In [3]: x.some_attr = {'a': 'dict', 'will': 'be transformed'}

    In [4]: x
    Out[4]: NestedNamespace(some_attr=NestedNamespace(a='dict', will='be transformed'))
