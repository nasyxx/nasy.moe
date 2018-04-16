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
# from nasymoe.render.org import emacs_daemon
# from nasymoe.render.render import render_blogs
from nasymoe.stores.deploy import deploy_static


def deploy() -> None:
    """Deploy blog."""
    deploy_static()


if __name__ == '__main__':
    deploy()
