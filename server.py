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
* date: Feb 25, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: server.py
* Last modified time: Mar 2, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
from typing import Any

from sanic import Sanic, request
from sanic.response import json

from server.render.render import render_blogs
from server.stores.stores import (ldict2blog, load_store_blog, load_store_tag,
                                  save_store_blog, save_store_tag)

# from xxhash import xxh64

app = Sanic("NasyLand")


@app.listener("before_server_start")
async def setup_db(app: Sanic, loop: Any) -> None:
    """Load blog infomations before server start."""
    tag, blog = render_blogs(2, "blog")
    app.blog = ldict2blog(load_store_blog(blog))
    app.tag = load_store_tag(tag)


@app.listener("after_server_stop")
async def close_db(app: Sanic, loop: Any) -> None:
    """Save blog infomations after server stop."""
    save_store_blog(app.blog)
    save_store_tag(app.tag)


@app.route("/tag")
async def tag_api(request: request) -> json:
    """Handle tag."""
    return json(app.tag)


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 1314)
