# coding: utf8

"""
    mysql data table model, mapping with xls sheet.
"""

import peewee

database = peewee.MySQLDatabase('xls2db', host='127.0.0.1', port=3306, user="root", passwd="flyfishdb")


class BaseModel(peewee.Model):
    """
    A base model that will use mysql database.
    """

    class Meta:
        database = database


class SampleModel(BaseModel):
    """
    A sample model for test.
    """
    sid = peewee.PrimaryKeyField()
    content = peewee.CharField(max_length=64)
    shortcut = peewee.CharField(max_length=16)

    class Meta:
        db_table = 'tb_sample_template'


database.connect()
