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
* date: Feb 22, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* file: server/render/render.py
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
import multiprocessing as mp
from functools import reduce
from itertools import chain

from server.render.org import emacs_daemon, org2blog
from server.types import BLS, LP, P
from server.utils.curring import curry
from server.utils.str2path import s2p

SUFFIX = {".org": org2blog}


@curry
def find_blogs(basepath: P, suffix: str) -> LP:
    """Find all blog files in basepath."""
    if isinstance(basepath, str):
        basepath = s2p(basepath)
    return filter(lambda x: x.suffix == suffix, basepath.glob("*"))


def combine_blogs(olds: BLS, news: BLS) -> BLS:
    """Combine blogs."""
    tag, blog = news
    olds[0][tag["id"]] = tag
    olds[1][blog["id"]] = blog
    return olds


@curry
def render_blogs(workers: int, basepath: P) -> BLS:
    """Render all blogs into two json like dict."""
    blog_find = find_blogs(basepath)
    all_blogs = zip(SUFFIX, map(blog_find, SUFFIX))
    if workers > 1 and not emacs_daemon("status"):
        emacs_daemon("start")
    pool = mp.Pool(workers)
    result = reduce(
        combine_blogs,
        chain(*(pool.map(org2blog, blog) for suffix, blog in all_blogs)),
        ({}, {})
    )  # type: BLS
    pool.close()
    pool.join()
    return result
