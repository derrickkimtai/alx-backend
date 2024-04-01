#!/usr/bin/env python3
"""
0-simple_helper_function
"""

from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range
    """
    return ((page - 1) * page_size, page * page_size)
