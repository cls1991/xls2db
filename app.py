# coding: utf8

"""
    core logic for export xls sheet to mysql table.
"""

import tablib
from model.models import SampleModel


def main():
    """
    create/read/delete data from mysql table.
    :return:
    """
    # sample = SampleModel()
    # sample.content = 'sample test!'
    # sample.shortcut = 'oops'
    # sample.save()
    #
    # for sample in SampleModel.select():
    #     print(sample.content, sample.shortcut)
    with open('data/sample.xls', 'rb') as f:
        data_book = tablib.import_book(f.read())
        for ds in data_book.sheets():
            if 'Sheet1' == ds.title:
                print(ds.dict)
        f.close()

if __name__ == '__main__':
    main()
