from __future__ import annotations


@lambda c: c()
class __annotations__:
    def __setitem__(self, name, value):
        globals()[value] = globals()[name]


var: i = 5
print(i)
