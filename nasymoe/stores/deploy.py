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
* date: Apr 5, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: deploy.py
* Last modified time: Apr 5, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
import os
import shutil
from pathlib import Path

from nasymoe.types import BB, BST, P

try:
    json = __import__("ujson")
except ModuleNotFoundError:
    json = __import__("json")
except ImportError:
    json = __import__("json")


def delete_dir(path: P) -> None:
    """Delete a dir."""
    if isinstance(path, str):
        path = Path(path)
    for p in path.iterdir():
        if p.is_dir():
            delete_dir(p)
        else:
            p.unlink()
    path.rmdir()


def deploy_static() -> None:
    """Deploy static files in the website."""
    delete_dir("./public")
    shutil.copytree("./website/public", "./public")


def deploy_blog(blog: BST) -> None:
    """Deploy blog content json files."""
    path = Path("./public/blog")
    for b in blog:
        bpath = path.joinpath(str(b["blog_path"]))
        os.makedirs(bpath.parent.as_posix(), exist_ok = True)
        with bpath.open("w") as f:
            json.dump(b, f)


def deploy_blogs(blogs: BST) -> None:
    """Deploy blogs json file."""
    with Path("./public/blogs").open("w") as f:
        json.dump(blogs, f)


def deploy_all(bb: BB) -> None:
    """Deploy all."""
    deploy_static()
    deploy_blog(bb[0])
    deploy_blogs(bb[1])
