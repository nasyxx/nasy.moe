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
* date: Feb 20, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: _config.py
* Last modified time: Mar 2, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
import pendulum

C_BLOG = dict(
    # blog configuration
    author = "Nasy",
    title = "Nasy Land",
    description = "Nasy 的花园～栽花、养鱼以及闲聊的地方w",
    google_ana = "UA-102577027-1",
)
C_POST = dict(
    # post default configuration
    title = "",
    author = "Nasy",
    summary = "No Summary",
    language = "en",
    tags = ["blog"],
    categories = ["Blog"],
    date = {
        "year": str(pendulum.now().year),
        "month": str(pendulum.now().month),
        "day": str(pendulum.now().day)
    },
    content = "",
    content_table = "",
)
