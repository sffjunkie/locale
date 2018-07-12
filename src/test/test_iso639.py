# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
p = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import sys
sys.path.insert(0, p)

from pytest import raises
from mogul.locale import iso639

def test_iso639_LowerCase2CharacterCode():
    assert iso639.Languages['en'] is not None


def test_iso639_LowerCase3CharacterCode():
    assert iso639.Languages['eng'] is not None


def test_iso639_LowerCaseInvalid2CharacterCode():
    with raises(KeyError):
        iso639.Languages['zz']


def test_iso639_LowerCaseInvalid3CharacterCode():
    with raises(KeyError):
        iso639.Languages['zzz']


def test_iso639_MixedCase3CharacterCode():
    assert iso639.Languages['eNg'] is not None


def test_iso639_Name():
    assert iso639.Languages['aa'].name == 'Afar'


def test_iso639_NativeName():
    assert iso639.Languages['bam'].native_name == 'bamanankan'


def test_iso639_iso639_1():
    assert iso639.Languages['bam'].iso639_1 == 'bm'


def test_iso639_iso639_2T():
    assert iso639.Languages['bd'].iso639_2T == 'bod'


def test_iso639_iso639_2B():
    assert iso639.Languages['bs'].iso639_2B == 'bos'


def test_iso639_iso639_3():
    assert iso639.Languages['cs'].iso639_3 == 'ces'


def test_iso639_NativeNameUnicode():
    assert iso639.Languages['bd'].native_name == 'བོད་ཡིག'
