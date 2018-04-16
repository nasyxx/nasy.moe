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
* date: Apr 12, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: dict_list.py
* Last modified time: Apr 12, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
from operator import itemgetter

from nasymoe.types import BL, BST


def blog2ldict(blog: BL) -> BST:
    """Transform blog dict to list of dict."""
    return sorted(blog.values(), key = itemgetter("blog_path"))


def ldict2blog(lblog: BST) -> BL:
    """Transform list of dict to blog dict."""
    return {str(blog["id"]): blog for blog in lblog if blog}
