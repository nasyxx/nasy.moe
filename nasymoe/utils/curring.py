#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              '
    |         =\  -  /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

* author: Nasy https://nasy.moe <Nasy>
* date: Feb 19, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: curring.py
* Last modified time: Mar 3, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
from functools import wraps
from typing import Any, Callable


def curry(func: Callable[..., Any]) -> Callable[..., Any]:
    """Currying the function."""
    assert func

    @wraps(func)
    def curried(*args: Any, **kwargs: Any) -> Any:
        """Currying function wrap."""
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)

        @wraps(func)
        def new_curried(*args2: Any, **kwargs2: Any) -> Any:
            """Curring function wrap's wrap."""
            return curried(*(args + args2), **dict(kwargs, **kwargs2))

        return new_curried

    return curried
