#!/usr/bin/env python3
""" Index Range"""


def index_range(page, page_size):
    """
    A function that returns a tuple of size two containing
    a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
