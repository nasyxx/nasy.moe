#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
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

* author: Nasy https://nasy.moe
* date: Feb 20, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* file: server/models/model.py
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
from typing import Any, TypeVar

A = TypeVar("A")
B = TypeVar("B")


class Model(dict):
    """Model."""

    def __call__(self, *args: A, **kwgs: B) -> "Model":
        """Call is another update."""
        self.update(*args, **kwgs)
        return self

    def __repr__(self) -> str:
        """Repr for Model."""
        self.clean()
        return "".join([
            # prefix
            f"{self._name}:\n\t",
            # value
            "\n\t".join(
                f"{i[0]}: {i[1]}" if isinstance(i[1], str) else
                f"{i[0]}: {i[1]}".replace("\n\t", "\n\t\t")
                .replace(f"{self._name}:", "") for i in self.items()
            ),
        ])

    def __init__(self, *args: A, **kwgs: B) -> None:
        """Initilize the Model."""
        self._name = self.__class__.__name__
        self.update(*args, **kwgs)
        self.clean()

    def clean(self) -> "Model":
        """Delete useless keys."""
        return self

    def update(self, *args: Any, **kwgs: Any) -> None:
        """Update Model."""
        for k, v in dict(*args, **kwgs).items():
            if isinstance(v, str) or isinstance(v, list):
                self[k] = v
            else:
                self[k] = self.__class__(v)
        self.clean()
