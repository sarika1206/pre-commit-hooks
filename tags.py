import argparse
import importlib
import inspect
import logging
import os
import re
import subprocess
import sys
import textwrap
import warnings
from datetime import datetime
from pathlib import Path
from pprint import pformat
from typing import Any, Callable



if __name__ == "__main__":

    
    _VERSION_PATTERN = r"""
        v?
        (?:
            (?:(?P<epoch>[0-9]+)!)?                           # epoch
            (?P<release>[0-9]+(?:\.[0-9]+)*)                  # release segment
            (?P<pre>                                          # pre-release
                [-_\.]?
                (?P<pre_l>(a|b|c|rc|alpha|beta|pre|preview))
                [-_\.]?
                (?P<pre_n>[0-9]+)?
            )?
            (?P<post>                                         # post release
                (?:-(?P<post_n1>[0-9]+))
                |
                (?:
                    [-_\.]?
                    (?P<post_l>post|rev|r)
                    [-_\.]?
                    (?P<post_n2>[0-9]+)?
                )
            )?
            (?P<dev>                                          # dev release
                [-_\.]?
                (?P<dev_l>dev)
                [-_\.]?
                (?P<dev_n>[0-9]+)?
            )?
        )
        (?:\+(?P<local>[a-z0-9]+(?:[-_\.][a-z0-9]+)*))?       # local version
    """

    VERSION_PATTERN = _VERSION_PATTERN
    

    _regex = re.compile(r"^\s*" + VERSION_PATTERN + r"\s*$", re.VERBOSE | re.IGNORECASE)
    cmd = "git tag --sort=creatordate --merged"
    stdout = subprocess.check_output(cmd, shell=True, text=True, cwd="/Users/gsarika/test/abcd") #os.PathLike)
    lines = stdout.splitlines()
    tags = [line.rstrip() for line in lines if line.rstrip()] 
    print(tags[-1])
    tag = tags[-1]
    version = tag
    match = _regex.search(version)

    if not match:
        print(f"Invalid version: '{version}'")
        exit()
    else:
        print(f"Valid version: '{version}'")



