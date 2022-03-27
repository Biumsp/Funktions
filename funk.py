from typing import Callable


class Funk():

    @staticmethod
    def evaluate(other: int or float):
        return other

    def __init__(self, x=None):

        if isinstance(x, (int, float)):
            def f(value): return x
            self.evaluate = f

        elif isinstance(x, Funk):
            self.evaluate = x.call

        elif isinstance(x, Callable):
            self.evaluate = x

    def __call__(self, other):
        assert isinstance(other, (int, float, Callable))

        if isinstance(other, (int, float)):
            return self.evaluate(other)
        elif isinstance(other, Funk):
            def f(value): return self.evaluate(other.evaluate(value))
        else:
            def f(value): return self.evaluate(other(value))

        return Funk(f)

    def __mul__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            return 0

        if other == 1:
            return self

        if isinstance(other, (int, float)):
            def f(value): return self.evaluate(value)*other
        elif isinstance(other, Funk):
            def f(value): return self.evaluate(value)*other.evaluate(value)
        else:
            def f(value): return self.evaluate(value)*other(value)

        return Funk(f)

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            raise ZeroDivisionError

        if isinstance(other, (int, float)):
            def f(value): return self.evaluate(value)/other
        elif isinstance(other, Funk):
            def f(value): return self.evaluate(value)/other.evaluate(value)
        else:
            def f(value): return self.evaluate(value)/other(value)

        return Funk(f)

    def __rtruediv__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            return 0

        if isinstance(other, (int, float)):
            def f(value): return other/self.evaluate(value)
        elif isinstance(other, Funk):
            def f(value): return other.evaluate(value)/self.evaluate(value)
        else:
            def f(value): return other(value)/self.evaluate(value)

        return Funk(f)

    def __pow__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            return 1

        if other == 1:
            return self

        if isinstance(other, (int, float)):
            def f(value): return self.evaluate(value)**other
        elif isinstance(other, Funk):
            def f(value): return self.evaluate(value)**other.evaluate(value)
        else:
            def f(value): return self.evaluate(value)**other(value)

        return Funk(f)

    def __rpow__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            return 0

        if other == 1:
            return 1

        if isinstance(other, (int, float)):
            def f(value): return other**self.evaluate(value)
        elif isinstance(other, Funk):
            def f(value): return other.evaluate(value)**self.evaluate(value)
        else:
            def f(value): return other(value)**self.evaluate(value)

        return Funk(f)

    def __add__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            return self

        if isinstance(other, (int, float)):
            def f(value): return self.evaluate(value)+other
        elif isinstance(other, Funk):
            def f(value): return self.evaluate(value)+other.evaluate(value)
        else:
            def f(value): return self.evaluate(value)+other(value)

        return Funk(f)

    def __radd__(self, other):
        return self+other

    def __sub__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            return self

        if isinstance(other, (int, float)):
            def f(value): return self.evaluate(value)-other
        elif isinstance(other, Funk):
            def f(value): return self.evaluate(value)-other.evaluate(value)
        else:
            def f(value): return self.evaluate(value)-other(value)

        return Funk(f)

    def __rsub__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            return -self

        if isinstance(other, (int, float)):
            def f(value): return other-self.evaluate(value)
        elif isinstance(other, Funk):
            def f(value): return other.evaluate(value)-self.evaluate(value)
        else:
            def f(value): return other(value)-self.evaluate(value)

        return Funk(f)

    def __neg__(self):
        def f(value): return -self.evaluate(value)
        return Funk(f)

    def __pos__(self):
        return self

    def __mod__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            raise ZeroDivisionError

        if isinstance(other, (int, float)):
            def f(value): return self.evaluate(value) % other
        elif isinstance(other, Funk):
            def f(value): return self.evaluate(value) % other.evaluate(value)
        else:
            def f(value): return self.evaluate(value) % other(value)

        return Funk(f)

    def __rmod__(self, other):
        assert isinstance(other, (int, float, Callable))

        if other == 0:
            return 0

        if isinstance(other, (int, float)):
            def f(value): return other % self.evaluate(value)
        elif isinstance(other, Funk):
            def f(value): return other.evaluate(value) % self.evaluate(value)
        else:
            def f(value): return other(value) % self.evaluate(value)

        return Funk(f)
