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

* author: Nasy https://nasy.moe <nasyxx>
* date: Feb 20, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: blog.py
* Last modified time: Mar 2, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
from .model import A, B, Model

try:
    json = __import__("ujson")
except ModuleNotFoundError:
    json = __import__("json")


class Tag(Model):
    """Tag model."""

    def __call__(self, *args: A, **kwgs: B) -> "Tag":
        """Call is another update."""
        self.update(*args, **kwgs)
        return self

    def clean(self) -> "Tag":
        """Delete useless keys."""
        for i in set(
                k for k in self.keys() if k not in {
                    "author", "title", "language", "summary", "tags",
                    "categories", "date", "year", "month", "day", "hash", "id",
                    "wordcount", "blog_path"
                }):
            del self[i]
        return self


class Blog(Model):
    """Blog Model."""

    def __call__(self, *args: A, **kwgs: B) -> "Blog":
        """Call is another update."""
        self.update(*args, **kwgs)
        return self

    def clean(self) -> "Blog":
        """Delete useless keys."""
        for i in set(
                k for k in self.keys() if k not in {
                    "author", "title", "language", "summary", "tags",
                    "categories", "date", "year", "month", "day", "content",
                    "content_table", "hash", "id", "wordcount", "blog_path"
                }):
            del self[i]

        return self
