""" Tests for the nested Namespace """

from nested_namespace import NestedNamespace


class TestNestedNamespace:
    def test__init__simple(self):
        d = {'a': 1, 'b': 2}
        ns = NestedNamespace(**d)

        assert ns.a == d['a']
        assert ns.b == d['b']

    def test__init__recursive(self):
        d = {
            'a': 1,
            'b': {
                'c': 2,
                'd': 3,
            },
        }
        ns = NestedNamespace(**d)

        assert ns.a == d['a']
        assert ns.b.c == d['b']['c']
        assert ns.b.d == d['b']['d']

    def test__init__list_member(self):
        d = {'a': [{'b': 1}], 'b': 2}
        ns = NestedNamespace(**d)

        assert ns.a[0].__dict__ == d['a'][0]
        assert ns.b == d['b']
