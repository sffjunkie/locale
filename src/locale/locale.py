# Copyright (c) 2015 Simon Kennedy <sffjunkie+code@gmail.com>

import sys
from collections import namedtuple, abc

from mogul.locale.iso639 import Languages
from mogul.locale.iso15924 import Scripts
from mogul.locale.iso3166 import Regions

if 'win32' in sys.platform:
    import mogul.locale._win as plat_locale


locale_name = plat_locale.user_locale_name


class LocaleIdentifier(namedtuple('LocaleIdentifier', 'language script region')):
    """The LocaleIdentifier class encapsulates a set of
    ISO language, script and region codes.
    
    Language codes are those defined in ISO 639-3 (3 character codes)
    Script codes are those defined in ISO 15924
    Region codes are those defined in ISO 3166
    
    Language codes can be set as 2 character codes as defined in the original
    ISO 639 but are converted to their ISO 639-3 equivalents
    """

    __slots__ = ()
    
    def __new__(cls, language, script=None, region=None):
        """Construct a Locale object
        
        :param language:   A 3 character language code from ISO 639-3
        :type language:    string
        :param script:    A script code from ISO 15924
        :type script:     string
        :param region:    A 2 character region code from ISO 3166-1
        :type region:     string
        """
        
        super(LocaleIdentifier, cls).__new__(cls, language, script, region)
        
    language_info = property(lambda self: Languages.iso639_3[self.language])
    country_info = property(lambda self: Regions[self.region.upper()])
    
    def __str__(self):
        if self.script:
            return "%s-%s-%s')" % (self.language, self.script, self.region)
        else:
            return "%s-%s" % (self.language, self.region)

    def __repr__(self):
        if self.script:
            return "('%s', '%s', '%s')" % (self.language, self.script, self.region)
        else:
            return "('%s', '%s')" % (self.language, self.region)

    def __eq__(self, l):
        return self.language == l.language and \
            self.script.lower() == l.script.lower() and \
            self.region.upper() == l.region.upper()

    def best_match(self, l1, l2):
        """Returns the Locale that best matches this Locale"""

        l1_match = 0
        if self.language == l1.language or self.language == 'und':
            l1_match = 3
            
        if self.region == l1.region or self.region == None:
            l1_match += 2
            
        if self.script == l1.script or self.script == None:
            l1_match += 1
        
        l2_match = 0
        if self.language == l2.language or self.language == 'und':
            l2_match = 3
            
        if self.region == l2.region or self.region == None:
            l2_match += 2
            
        if self.script == l2.script or self.script == None:
            l2_match += 1
            
        if l1_match >= l2_match:
            return l1
        else:
            return l2



# TODO: Make this work
class LocaleBag(object):
    """A wrapper for an iterable that picks one with the closest locale"""
    
    def __init__(self, name, iterable):
        if not isinstance(iterable, abc.Iterable):
            raise ValueError('iterable parameter not an iterable')
        
        self.name = name
        self.iterable = iterable
        
    def get(self, locale=None):
        """Return the default item or the item whose locale best matches
        ``locale``
        """

        best_match = None
        first_without_locale = None
        for item in iter(self.iterable):
            locale = getattr(item, 'locale', None)
            if not locale:
                first_without_locale = item

            if not best_match:
                best_match = item
            else:
                if item > best_match:
                    best_match = item
        
        if best_match:
            return best_match
        else:
            return first_without_locale
            