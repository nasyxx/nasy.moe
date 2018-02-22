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
* file: server/models/blog.py
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
from server.types import BS

from .model import Model

try:
    json = __import__("ujson")
except ModuleNotFoundError:
    json = __import__("json")


class Tag(Model):
    """Tag model."""

    def clean(self) -> "Tag":
        """Delete useless keys."""
        for i in set(
            k for k in self.keys() if k not in {
                "author", "title", "language", "summary", "tags", "categories",
                "date", "year", "month", "day", "id", "wordcount"
            }
        ):
            del self[i]
        return self

    @property
    def out(self) -> BS:
        """Out put."""
        return {k: v for k, v in self.clean().items()}


class Blog(Model):
    """Blog Model."""

    def clean(self) -> "Blog":
        """Delete useless keys."""
        for i in set(
            k for k in self.keys() if k not in {
                "author", "title", "language", "summary", "tags", "categories",
                "date", "year", "month", "day", "content", "content_table",
                "id", "wordcount"
            }
        ):
            del self[i]

        return self

    @property
    def out(self) -> BS:
        """Out put."""
        return {k: v for k, v in self.clean().items()}
