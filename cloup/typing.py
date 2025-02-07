__all__ = ['MISSING', 'Possibly',  'Decorator', 'F']

from enum import Enum
from typing import Callable, TypeVar, Union


# PEP-blessed solution for defining a Singleton type:
# https://www.python.org/dev/peps/pep-0484/#id30
class _Missing(Enum):
    flag = 'Missing'


MISSING = _Missing.flag
"""Singleton that works as a placeholder for a missing value. Useful when None
can't be used to play the role because it represents a valid non-null value."""

_T = TypeVar('_T')
Possibly = Union[_Missing, _T]
"""Possibly[T] is meant to be used in place of Optional[T] when None can't be
used to represent a missing value."""

F = TypeVar('F', bound=Callable)
"""Type variable for a Callable."""

Decorator = Callable[[Callable], Callable]
"""Type alias for a simple function decorator."""
