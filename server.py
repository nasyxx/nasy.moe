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
from urllib.parse import unquote

from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.request import Request
from sanic.response import json, redirect
from xxhash import xxh64

from server.exceptions import BlogNotFound
from server.render.org import emacs_daemon
from server.render.render import render_blogs
from server.stores.stores import (ldict2blog, load_store_blog, load_store_tag,
                                  save_store_blog, save_store_tag)

app = Sanic("NasyLand")


@app.listener("before_server_start")
async def setup_db(app: Sanic, loop: Any) -> None:
    """Load blog infomations before server start."""
    tag, blog = render_blogs(2, "blog")
    app.blog = ldict2blog(load_store_blog(blog))
    app.tag = load_store_tag(tag)


@app.route("/tag")
async def tag_api(request: Request) -> json:
    """Handle tag."""
    return json({
        "message": "Welcome to Nasy Land!",
        "status": 200,
        "error": None,
        "results": app.tag
    })


@app.route(("/<year:[0-9]{4}>"
            "/<month:0[1-9]|1[012]>"
            "/<day:0[1-9]|[12][0-9]|3[01]>"
            "/<title>"))
async def blog_api(request: Request, year: int, month: int, day: int,
                   title: str) -> json:
    """Handle tag."""
    blog_date = {"year": year, "month": month, "day": day}
    req_blog = app.blog.get(xxh64(unquote(title)).hexdigest())
    if req_blog:
        if all(
                map(lambda x: req_blog["date"][x] == blog_date[x],
                    req_blog["date"])):
            return json(
                {
                    "message": f"Hope you enjoy \"{unquote(title)}\"",
                    "status": request.headers,
                    "error": None,
                    "results": req_blog
                },
                status = 200)
        else:
            return redirect(f"/{req_blog['blog_path']}")
    else:
        raise BlogNotFound(f"Blog \"{unquote(title)}\" Not Found!")


@app.exception(BlogNotFound)
def blog_not_found(request: Request, exception: BlogNotFound) -> json:
    """Handle blog not found."""
    return json(
        {
            "message": "Oooooops! Cannot Found the blog!",
            'status': exception.status_code,
            'error': exception.args[0],
            'results': None,
        },
        status = exception.status_code)


@app.exception(NotFound)
def not_found_404(request: Request, exception: NotFound) -> json:
    """Handle 404 not found."""
    return json(
        {
            "message": "Oooooops! Not Found!",
            'status': exception.status_code,
            'error': exception.args[0],
            'results': None,
        },
        status = exception.status_code)


@app.listener("after_server_stop")
async def close_db(app: Sanic, loop: Any) -> None:
    """Save blog infomations after server stop."""
    save_store_blog(app.blog)
    save_store_tag(app.tag)
    emacs_daemon("stop")


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 1314)
