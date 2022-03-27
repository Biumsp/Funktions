from typing import Callable


class Funk():

    def __init__(self, x=None):

        if isinstance(x, (int, float)):
            def f(value): return x
            self.call = f

        elif isinstance(x, Callable):
            self.call = x.__call__

    @staticmethod
    def call(other):
        return other

    def __call__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if isinstance(other, (int, float)):
            return self.call(other)

        def f(value): return self.call(other(value))
        return Funk(f)

    def __mul__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            return 0

        if other == 1:
            return self

        if isinstance(other, (int, float)):
            def f(value): return self.call(value)*other
        else:
            def f(value): return self.call(value)*other(value)

        return Funk(f)

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            raise ZeroDivisionError

        if isinstance(other, (int, float)):
            def f(value): return self.call(value)/other
        else:
            def f(value): return self.call(value)/other(value)

        return Funk(f)

    def __rtruediv__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            return 0

        def f(value): return other/self.call(value)
        return Funk(f)

    def __pow__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            return 1

        if other == 1:
            return self

        if isinstance(other, (int, float)):
            def f(value): return self.call(value)**other
        else:
            def f(value): return self.call(value)**other(value)

        return Funk(f)

    def __rpow__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            return 0

        if other == 1:
            return 1

        if isinstance(other, (int, float)):
            def f(value): return other**self.call(value)
        else:
            def f(value): return other(value)**self.call(value)

        return Funk(f)

    def __xor__(self, other):
        return self**other

    def __rxor__(self, other):
        return other**self

    def __add__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            return self

        if isinstance(other, (int, float)):
            def f(value): return self.call(value)+other
        else:
            def f(value): return self.call(value)+other(value)

        return Funk(f)

    def __radd__(self, other):
        return self+other

    def __sub__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            return self

        if isinstance(other, (int, float)):
            def f(value): return self.call(value)-other
        else:
            def f(value): return self.call(value)-other(value)

        return Funk(f)

    def __rsub__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            return -self

        if isinstance(other, (int, float)):
            def f(value): return other-self.call(value)
        else:
            def f(value): return other(value)-self.call(value)

        return Funk(f)

    def __neg__(self):
        def f(value): return -self.call(value)

        return Funk(f)

    def __pos__(self):
        return self

    def __mod__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            raise ZeroDivisionError

        if isinstance(other, (int, float)):
            def f(value): return self.call(value) % other
        else:
            def f(value): return self.call(value) % other(value)

        return Funk(f)

    def __rmod__(self, other):
        assert isinstance(other, (int, float, Funk, Callable))

        if other == 0:
            return 0

        if isinstance(other, (int, float)):
            def f(value): return other % self.call(value)
        else:
            def f(value): return other(value) % self.call(value)

        return Funk(f)
