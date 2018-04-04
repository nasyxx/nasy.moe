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

* author: Nasy https://nasy.moe <nasyxx>
* date: Feb 20, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: __init__.py
* Last modified time: Mar 2, 2018
* license: MIT

In fact, I am not really sure what is a NewType or TypeVar should be. Is it
    just like the readable and meaningful type aliases?

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
from pathlib import Path
from typing import Dict, Iterable, List, Tuple, Union

import bs4

# Blog Tags & Content
BT = Union[str, List[str], Dict[str, str]]
# Blog complete
B = Dict[str, BT]
# Blog info
BI = Tuple[str, BT]
# Blog Simple
BS = Dict[str, BT]
# Blogs
BL = Union[Dict[str, B], Dict[str, BS]]
BLS = Tuple[BL, BL]
# Blogs Store
BST = List[Dict[str, BT]]
# Config
C = Union[str, List[str], Dict[str, str]]
# Html Tag
H_tag = bs4.element.Tag
# Html String
H_str = str
# Path
P = Union[str, Path]
# Paths: List of Paths
LP = Union[List[P], Iterable[P]]
