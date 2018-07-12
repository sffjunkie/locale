# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import warnings

test_path = os.path.dirname(__file__)
p = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, p)

import pytest
from mogul.locale import bcp47

def test_bcp47_New():
    tag = bcp47.BCP47LanguageTag()
    assert tag.language == 'und'


def test_bcp47_Str():
    tag = bcp47.BCP47LanguageTag.fromstring('en-Latn-GB')
    assert str(tag) == 'en-Latn-GB'

    tag = bcp47.BCP47LanguageTag.fromstring('En-lATn-Gb')
    assert str(tag) == 'en-Latn-GB'


def test_bcp47_FromStringLanguage():
    tag = bcp47.BCP47LanguageTag.fromstring('en')
    assert tag.language == 'en'


def test_bcp47_FromStringLanguageRegion():
    tag = bcp47.BCP47LanguageTag.fromstring('en-GB')
    assert tag.language == 'en'
    assert tag.region == 'GB'


def test_bcp47_FromStringLanguageRegionScript():
    tag = bcp47.BCP47LanguageTag.fromstring('en-Latn-GB')
    assert tag.language == 'en'
    assert tag.script == 'Latn'
    assert tag.region == 'GB'


def test_bcp47_WellFormed():
    fname = os.path.join(test_path, 'test_bcp47_wellformed.utf8')
    with open(fname, encoding='utf-8') as fs:
        for line in fs.readlines():
            line = line.strip(' \n')
            pos = line.find('#')
            if pos != -1:
                line = line[:pos].rstrip()
            if not line:
                continue
                
            tag = bcp47.BCP47LanguageTag.fromstring(line)
            assert str(tag).lower() == line.lower() 


def atesta_bcp47_NotWellFormed():
    warnings.simplefilter('error', bcp47.BCP47NotWellFormed)

    fname = os.path.join(test_path, 'test_bcp47_notwellformed.utf8')
    with open(fname, encoding='utf-8') as fs:
        for line in fs.readlines():
            line = line.strip(' \n')
            pos = line.find('#')
            if pos != -1:
                line = line[:pos].rstrip()
            if not line:
                continue
            
            with pytest.raises(bcp47.BCP47NotWellFormed):
                tag = bcp47.BCP47LanguageTag.fromstring(line)

    warnings.simplefilter('default', bcp47.BCP47NotWellFormed)


def test_bcp47_Valid():
    fname = os.path.join(test_path, 'test_bcp47_valid.utf8')
    with open(fname, encoding='utf-8') as fs:
        for line in fs.readlines():
            line = line.strip(' \n')
            pos = line.find('#')
            if pos != -1:
                line = line[:pos].rstrip()
            if not line:
                continue

            tag = bcp47.BCP47LanguageTag.fromstring(line)
            assert tag.isvalid()
