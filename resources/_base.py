# coding: utf8

"""
    Base Data Source.
"""

from . import models


class BaseResource(object):
    def __init__(self, sheet_name, unique_key, header_index=0, content_index=1):
        """
        The class `BaseResource` object is heart of xls2db, It provides all core functionality.
        :param sheet_name: name of data sheet
        :param unique_key: unique key of data model
        :param header_index: (optional) header start index for data sheet
        :param content_index: (optional) content start index for data sheet
        :return:
        """
        self._sheet_name = sheet_name
        self._unique_key = unique_key
        self._header_index = header_index
        self._content_index = content_index

    def import_data(self, data_book):
        """
        Import data from xls data sheet to mysql database.
        :param data_book: xls data sheet
        :return:
        """
        data_set = None
        for sheet in data_book.sheets():
            if self._sheet_name == sheet.title:
                data_set = sheet
                break
        if data_set is None:
            raise "sheet %s not found" % self._sheet_name
        headers = None
        for ix, dt in enumerate(data_set.dict):
            if ix == self._header_index:
                headers = dt.keys()
            elif ix >= self._content_index:
                t = models[self._sheet_name].get(dt[self._unique_key])
                if not t:
                    t = models[self._sheet_name]()
                for header in headers:
                    t[header] = dt[header]
                t.save()
