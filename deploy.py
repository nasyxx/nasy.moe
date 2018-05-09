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
from nasymoe.render.render import add_last_next, render_blogs
from nasymoe.stores.deploy import deploy_all
from nasymoe.stores.stores import load_store_blog, load_store_blogs
from nasymoe.utils.dict_list import blog2ldict, ldict2blog


def deploy() -> None:
    """Deploy blog."""
    rblogs, rblog = render_blogs(2, "blog")
    blogs, blog = add_last_next((
        ldict2blog(load_store_blogs(rblogs)),
        ldict2blog(load_store_blog(rblog)),
    ))
    deploy_all((blog2ldict(blog), blog2ldict(blogs)))


if __name__ == '__main__':
    deploy()
