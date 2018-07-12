# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
p = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import sys
sys.path.insert(0, p)

from pytest import raises
from mogul.locale import iso15924

def test_iso15924_CorrectCase():
    assert iso15924.Scripts['Rjng'] is not None


def test_iso15924_LowerCase():
    assert iso15924.Scripts['rjng'] is not None


def test_iso15924_UpperCase():
    assert iso15924.Scripts['RJNG'] is not None


def test_iso15924_MixedCase():
    assert iso15924.Scripts['rJnG'] is not None


def test_iso15924_InvalidCode():
    with raises(KeyError):
        iso15924.Scripts['Bads']


def test_iso15924_Name():
    assert iso15924.Scripts['Adlm'].name == 'Adlam'


def test_iso15924_PrivateCode():
    assert iso15924.Scripts['Qaaa'].name == 'Reserved for private use'
    assert iso15924.Scripts['Qabx'].name == 'Reserved for private use'


def test_iso15924_PrivateNumber():
    assert iso15924.Scripts[900].name == 'Reserved for private use'
    assert iso15924.Scripts[949].name == 'Reserved for private use'
