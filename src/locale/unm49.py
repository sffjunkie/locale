# -*- coding: utf-8 -*-
#
# This source code is made available under the
# Creative Commons Attribution-Share-Alike License 3.0 or later
# http://creativecommons.org/licenses/by-sa/3.0/
#
# UN M.49 data taken from the following Wikipedia page
# https://en.wikipedia.org/wiki/UN_M.49

from __future__ import unicode_literals
from collections import namedtuple

__all__ = ['Regions']

UNM49 = namedtuple('UNM49', ['number', 'name'])


UNM49_INFO = [
    UNM49(11, 'Western Africa'),
    UNM49(13, 'Central America'),
    UNM49(142, 'Asia'),
    UNM49(143, 'Central Asia'),
    UNM49(145, 'Western Asia'),
    UNM49(14, 'Eastern Africa'),
    UNM49(150, 'Europe'),
    UNM49(150, 'Europe'),
    UNM49(151, 'Eastern Europe'),
    UNM49(154, 'Northern Europe'),
    UNM49(155, 'Western Europe'),
    UNM49(15, 'Northern Africa'),
    UNM49(172, 'Commonwealth of Independent States'),
    UNM49(17, 'Middle Africa'),
    UNM49(18, 'Southern Africa'),
    UNM49(199, 'Least developed countries'),
    UNM49(19, 'Americas'),
    UNM49(1, 'World'),
    UNM49(21, 'Northern America'),
    UNM49(21, 'Northern America'),
    UNM49(29, 'Caribbean'),
    UNM49(2, 'Africa'),
    UNM49(30, 'Eastern Asia'),
    UNM49(34, 'Southern Asia'),
    UNM49(35, 'South-Eastern Asia'),
    UNM49(376, 'Israel'),
    UNM49(392, 'Japan'),
    UNM49(39, 'Southern Europe'),
    UNM49(3, 'North America'),
    UNM49(419, 'Latin America and the Caribbean'),
    UNM49(432, 'Landlocked developing countries'),
    UNM49(53, 'Australia and New Zealand'),
    UNM49(54, 'Melanesia'),
    UNM49(57, 'Micronesia'),
    UNM49(5, 'South America'),
    UNM49(61, 'Polynesia'),
    UNM49(722, 'Small island developing states'),
    UNM49(778, 'Transition countries'),
    UNM49(9, 'Oceania'),
]


class UNM49Regions():
    def __init__(self):
        self._number = None

    def __getitem__(self, key):
        n = int(key)
        return self.number[key]

    @property
    def number(self):
        if self._number is None:
            self._number = {}
            for info in UNM49_INFO:
                self._number[info.number] = info
            return self._number
        else:
            return self._number


Regions = UNM49Regions()
