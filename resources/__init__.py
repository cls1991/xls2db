# coding: utf8

""" model-resource mappings.
"""

from _base import BaseResource

from model import models

sources = {
    'sample': BaseResource('sample', 'id'),
}

models = {
    'sample': models.SampleModel
}
