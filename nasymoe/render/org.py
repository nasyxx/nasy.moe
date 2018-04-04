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
* date: Feb 20, 2018
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* filename: org.py
* Last modified time: Mar 2, 2018
* license: MIT

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
import re
import subprocess
from collections import Counter
from itertools import chain, takewhile
from pathlib import Path
from typing import Dict, Optional, Tuple, Union

import bs4
from pendulum import parse
from xxhash import xxh64

from _config import C_POST
from nasymoe.log.log import logger
from nasymoe.models.blog import Blog, Tag
from nasymoe.types import BI, BS, B, H_str, H_tag, P  # Type Alias
from nasymoe.utils.const import NWORD
from nasymoe.utils.str2path import s2p


def clean_line(line: str) -> str:
    """Clean line."""
    return line.replace("\n", "").replace("<", "").replace(">", "").replace(
        "#+", "")


def get_org_info(line: str) -> Optional[BI]:
    """Get org info."""
    k, *vs = re.split(r":\s*", clean_line(line))
    kl, v = k.lower(), "".join(vs)
    if kl in {"author", "title", "language", "summary"}:
        return kl, v

    elif kl in {"tags", "categories"}:
        return kl, sorted(re.split(r",\s*", v))

    elif kl == "date" and v:
        date = parse(v)
        return kl, {
            "year": f"{date.year:4}",
            "month": f"{date.month:02}",
            "day": f"{date.day:02}"
        }
    return None


def org2tags(path: P) -> Tag:
    """Read tags of org file."""
    if isinstance(path, str):
        path = s2p(path)
    tag = Tag(C_POST, title = path.stem)
    with path.open() as f:
        return tag(
            filter(lambda x: x, [
                get_org_info(line)
                for line in takewhile(lambda x: x != "\n", f)
                if all(map(lambda x: x in line, {"#+", ":"}))
            ]))


def emacs_daemon(do: str) -> bool:
    """Emacs daemon status.

    Args:
        `do` -- "test", "start" or "stop"

    "status" show the emacs daemon status, return `False` if not started.
    "start" start the emacs daemon.
    "stop" stop the emacs daemon.
    """
    if do == "status":
        if not subprocess.Popen(
                "emacsclient -q --socket-name=org_to_html "
                "-e '(message \"hi\")'",
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
        ).wait():
            logger.info("Already Started.")
            return True
        else:
            return False
    elif do == "start":
        if not subprocess.Popen(
                "emacs --no-desktop --daemon=org_to_html",
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
        ).wait():
            logger.info("Success start emacs daemon org_to_html")
            return True
        else:
            logger.error("Failed to start emacs daemon!")
            return False
    elif do == "stop":
        if not subprocess.Popen(
                "emacsclient --socket-name=org_to_html -e '(kill-emacs)'",
                shell = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
        ).wait():
            logger.info("Success stop emacs daemon org_to_html")
            return True
        else:
            logger.error("Failed to stop emacs daemon!")
            return False
    logger.error(
        f"Unknow Command '{do}', must be one of 'test', 'start' and 'stop'")
    raise RuntimeError(
        f"Unknow Command '{do}', must be one of 'test', 'start' and 'stop'")
    return False


def org2html_file(path: P) -> Path:
    """Reander org file to html file."""
    if isinstance(path, str):
        path = s2p(path)
    logger.info(f"exporting to html: {path}")
    subprocess.Popen(
        "emacsclient --socket-name=org_to_html "
        f"-e '(progn (find-file \"{path}\") "
        "(setq org-export-preserve-breaks nil)"
        "(setq org-export-with-emphasize t)"
        "(setq org-export-with-special-strings t)"
        "(setq org-export-with-sub-superscripts t)"
        "(setq org-export-headline-levels 4)"
        "(setq org-export-with-latex t)"
        "(setq org-export-with-fixed-width t)"
        "(setq org-export-with-section-numbers nil) "
        "(setq org-export-with-toc 3)"
        "(setq org-export-with-tables t)"
        "(org-html-export-to-html))' ",
        shell = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    ).wait()
    return path.with_suffix(".html")


def html_content_edit(raw_content: H_tag) -> Tuple[H_tag, H_tag, str]:
    """Get html content table of a html file."""
    content_table = raw_content.select("#table-of-contents")[0]
    content_notb = raw_content.replace_with(content_table)
    content_table = content_table.select("#text-table-of-contents")[0]
    content_table.name = "nav"
    content_table.attrs["class"] = content_table.attrs.pop("id")

    ccount = Counter(content_notb.text)
    wordcount = str(
        sum(ccount.values()) - sum([ccount[i] for i in ccount if i in NWORD]))

    content = str(content_notb).replace(
        "<table", "<div class='table_container'><table").replace(
            "/table>", "/table></div>")

    return content, str(content_table), wordcount


def org2html(path: P) -> Dict[str, Union[H_str, str]]:
    """Render org file to html string."""
    if isinstance(path, str):
        path = s2p(path)
    html_path = org2html_file(path)
    with html_path.open() as h, path.open() as f:
        html_str = h.read()
        org_str = f.read()

    html_path.unlink()

    return {
        k: v
        for k, v in zip(("content", "content_table", "wordcount", "hash"),
                        chain(
                            html_content_edit(
                                bs4.BeautifulSoup(html_str, "lxml")
                                .select("#content")[0]),
                            (xxh64(org_str).hexdigest(),),
                        ))
    }


def org2blog(path: P) -> Tuple[BS, B]:
    """Read org file."""
    if isinstance(path, str):
        path = s2p(path)
    tag = org2tags(path)
    blog = Blog(tag)
    if not emacs_daemon("status"):
        emacs_daemon("start")
    blog.update(org2html(path))
    tag["wordcount"] = blog["wordcount"]
    tag["blog_path"] = blog["blog_path"] = "/".join([
        tag["date"]["year"], tag["date"]["month"], tag["date"]["day"],
        tag["title"]
    ])
    tag["id"] = blog["id"] = xxh64(tag["title"]).hexdigest()
    tag["datetime"] = blog["datetime"] = parse(
        f'{tag["date"]["year"]}-{tag["date"]["month"]}-{tag["date"]["day"]}'
    ).to_atom_string()

    logger.info(str(tag))
    return tag, blog


def main() -> None:
    """Yooo, here is the main function."""
    blog = org2blog("./blog/a.org")
    print(blog[0])
    print(blog[1])


if __name__ == "__main__":
    main()
