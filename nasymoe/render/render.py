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
* date: Feb 22, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: render.py
* Last modified time: Mar 2, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
import multiprocessing as mp
from functools import reduce
from itertools import chain

from nasymoe.render.org import emacs_daemon, org2blog
from nasymoe.types import BLS, LP, P
from nasymoe.utils.curring import curry
from nasymoe.utils.dict_list import blog2ldict, ldict2blog
from nasymoe.utils.str2path import s2p

SUFFIX = {".org": org2blog}


@curry
def find_blogs(basepath: P, suffix: str) -> LP:
    """Find all blog files in basepath."""
    if isinstance(basepath, str):
        basepath = s2p(basepath)
    return filter(lambda x: s2p(x).suffix == suffix, basepath.glob("*"))


def combine_blogs(olds: BLS, news: BLS) -> BLS:
    """Combine blogs."""
    tag, blog = news
    olds[0][str(tag["id"])] = tag  # type: ignore
    olds[1][str(blog["id"])] = blog  # type: ignore
    return olds


def add_last_next(result: BLS) -> BLS:
    """Add last and next to blogs."""
    blogs, blog = result
    lblogs = blog2ldict(blogs)

    last = ""
    last_name = ""
    for i, (l, n) in enumerate(zip(lblogs, chain(lblogs[1:], ({"": ""},)))):
        id_ = str(lblogs[i].get("id"))
        blog[id_].update({
            "last": last,
            "next": n.get("blog_path", ""),
            "last_name": last_name,
            "next_name": n.get("title", "")
        })
        lblogs[i].update({
            "last": last,
            "next": n.get("blog_path", ""),
            "last_name": last_name,
            "next_name": n.get("title", "")
        })
        last = str(l.get("blog_path", ""))
        last_name = str(l.get("title", ""))

    return ldict2blog(lblogs), blog


@curry
def render_blogs(workers: int, basepath: P) -> BLS:
    """Render all blogs into two json like dict."""
    if isinstance(basepath, str):
        basepath = s2p(basepath)
    blog_find = find_blogs(basepath)
    all_blogs = zip(SUFFIX, map(blog_find, SUFFIX))
    if workers > 1 and not emacs_daemon("status"):
        emacs_daemon("start")
    pool = mp.Pool(workers)
    result = reduce(  # type: ignore
        combine_blogs,
        chain(*(pool.map(org2blog, blog) for suffix, blog in all_blogs)),
        ({}, {}))  # type: BLS
    pool.close()
    pool.join()

    return result
