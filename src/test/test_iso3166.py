# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
p = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import sys
sys.path.insert(0, p)

from pytest import raises
from mogul.locale import iso3166


def test_iso3166_Alpha2UpperCase():
    assert iso3166.Regions['AI'] is not None


def test_iso3166_Alpha2LowerCase():
    assert iso3166.Regions['as'] is not None


def test_iso3166_Alpha2MixedCase():
    assert iso3166.Regions['As'] is not None


def test_iso3166_Name():
    assert iso3166.Regions['AU'].name == 'Australia'


def test_iso3166_NativeName():
    assert iso3166.Regions['AT'].native_name == 'Österreich'


def test_iso3166_Alpha3UpperCase():
    assert iso3166.Regions['AUT'] is not None


def test_iso3166_Alpha3LowerCase():
    assert iso3166.Regions['brb'] is not None


def test_iso3166_Alpha3MixedCase():
    assert iso3166.Regions['BmU'] is not None
