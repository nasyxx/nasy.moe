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

* author: Nasy https://nasy.moe <Nasy>
* date: Feb 20, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: str2path.py
* Last modified time: Mar 3, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
from functools import lru_cache
from pathlib import Path

from server.types import P


@lru_cache(maxsize = 65536)
def s2p(path: P) -> Path:
    """Turn string/Path to Path."""
    assert any((isinstance(path, str), isinstance(path, Path))) is True
    if isinstance(path, str):
        return Path(path)
    return path


def main() -> None:
    """Yooo, here is the main function."""
    assert isinstance(s2p("test"), Path) is True
    assert isinstance(s2p(Path("test")), Path) is True
    print("s2p: pass")


if __name__ == "__main__":
    main()
