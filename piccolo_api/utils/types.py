"""
Utils for extracting information from complex, nested types.
"""

from __future__ import annotations

import typing as t

try:
    # Python 3.10 and above
    from types import UnionType  # type: ignore
except ImportError:

    class UnionType:  # type: ignore
        ...


def get_type(type_: t.Type) -> t.Type:
    """
    Extract the inner type from an optional if necessary, otherwise return
    the type as is.

    For example::

        >>> get_type(Optional[int])
        int

        >>> get_type(int | None)
        int

        >>> get_type(int)
        int

        >>> _get_type(list[str])
        list[str]

    """
    origin = t.get_origin(type_)

    # Note: even if `t.Optional` is passed in, the origin is still a
    # `t.Union` or `UnionType` depending on the Python version.
    if any(origin is i for i in (t.Union, UnionType)):
        union_args = t.get_args(type_)

        NoneType = type(None)

        if len(union_args) == 2 and NoneType in union_args:
            return [i for i in union_args if i is not NoneType][0]

    return type_


def is_multidimensional_array(type_: t.Type) -> bool:
    """
    Returns ``True`` if ``_type`` is ``list[list]``.
    """
    if t.get_origin(type_) is list:
        args = t.get_args(type_)
        if args and t.get_origin(args[0]) is list:
            return True
    return False


def get_array_base_type(type_: t.Type[t.List]) -> t.Type:
    """
    Extracts the base type from an array. For example::

        >>> get_array_base_type(t.List[str])
        str

        >>> get_array_base_type(t.List(t.List[str]))
        str

    """
    args = t.get_args(type_)
    if args:
        if t.get_origin(args[0]) is list:
            return get_array_base_type(args[0])
        else:
            return args[0]
    return type_


__all__ = ("get_type", "is_multidimensional_array", "get_array_base_type")
