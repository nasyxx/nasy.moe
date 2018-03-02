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
* date: Feb 24, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: stores.py
* Last modified time: Mar 2, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
from pathlib import Path

from server.types import BL, BST, P
from server.utils.curring import curry

try:
    import ujson as json
except ModuleNotFoundError:
    import json  # type: ignore


def blog2ldict(blog: BL) -> BST:
    """Transform blog dict to list of dict."""
    return list(blog.values())


def ldict2blog(lblog: BST) -> BL:
    """Transform list of dict to blog dict."""
    return {str(blog["id"]): blog for blog in lblog if blog}


def update_store(stored: BST, blog: BL) -> BST:
    """Combine store and blog."""
    return list(
        filter(
            lambda x: x,
            map(
                lambda x: blog.pop(str(x.get("id")))
                if x.get("id") in blog else x, stored
            )
        )
    ) + blog2ldict(blog)


@curry
def load_store_json(path: P, blog: BL) -> BST:
    """Load stored blog infomations and update."""
    path = Path(path)
    if path.exists():
        with path.open() as f:
            return update_store(json.load(f), blog)
    return blog2ldict(blog)


@curry
def save_store_json(path: P, blog: BST) -> None:
    """Save blog to store."""
    path = Path(path)
    path.parent.mkdir(exist_ok = True)
    with path.open("w") as f:
        json.dump(blog, f, sort_keys = True, indent = 4)


load_store_blog = load_store_json("./stores/blog.json")
load_store_tag = load_store_json("./stores/tag.json")
save_store_blog = save_store_json("./.stores/blog.json")
save_store_tag = save_store_json("./.stores/tag.json")
