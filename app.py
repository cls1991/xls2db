# coding: utf8

"""
    core logic for export xls sheet to mysql table.
"""

import tablib

from resources.base import BaseResource


def main():
    """
    create/read/delete data from mysql table.
    :return:
    """
    with open('data/sample.xls', 'rb') as f:
        data_book = tablib.import_book(f.read())
        BaseResource('sample', 'sid').import_data(data_book)
        f.close()


if __name__ == '__main__':
    main()
