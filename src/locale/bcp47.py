# Copyright (c) 2015 Simon Kennedy <sffjunkie+code@gmail.com>

from __future__ import unicode_literals
import io
import os.path
import pkgutil
import string
import warnings
from collections import namedtuple

#import unm49
#import iso369
#import iso3166
#import iso15924


class BCP47NotWellFormed(Warning):
    pass


_ascii_lower_trans = str.maketrans(string.ascii_uppercase, string.ascii_lowercase)
_ascii_upper_trans = str.maketrans(string.ascii_lowercase, string.ascii_uppercase)


bcp47_registry = None
def load_registry(reload=False):
    global bcp47_registry
    if bcp47_registry is not None:
        if reload:
            del bcp47_registry
        else:
            return bcp47_registry

    entry = None
    try:
        data = pkgutil.get_data('bcp47', 'bcp47_registry.utf8').decode('UTF-8')
        stream = io.StringIO(data)
    except:
        fname = os.path.join(os.path.dirname(__file__), 'bcp47_registry.utf8')
        stream = open(fname, encoding="utf-8")

    bcp47_registry = {
        'language': {},
        'script': {},
        'region': {},
        'variant': {},
        'grandfathered': {},
        'redundant': {},
        'extlang': {},
    }

    name = None    
    for line in stream.readlines():
        line = line.rstrip('\n')
        if len(line) == 0 or line.startswith('File-Date:'):
            continue
        if line == '%%':
            if entry:
                t = entry.pop('type')
                try:
                    if t == 'grandfathered' or t == 'redundant':
                        key = entry.pop('tag')
                    else:
                        key = entry.pop('subtag')
                except:
                    pass
                bcp47_registry[t][key] = entry
            entry = {}
        else:
            if line[0] == ' ' and name:
                if isinstance(entry[name], list):
                    entry[name][-1].append(line)
                else:
                    entry[name] += line
            else:
                name, value = line.split(':', maxsplit=1)
                name = name.strip().lower()
                value = value.strip()
                if name not in entry:
                    entry[name] = value
                else:
                    if not isinstance(entry[name], list):
                        entry[name] = [entry[name]]
                    entry[name].append(value)

    return bcp47_registry


class BCP47LanguageTag(namedtuple('_BCP47LanguageTag',
                                  ['language', 'script',
                                   'region', 'variant',
                                   'extension', 'private'])):
    __slots__ = ()
    
    def __new__(cls, language:str=None, script:str=None,
                region:str=None, variant:str=None,
                extension:dict=None, private:list=None):
        if language is None:
            language = 'und'
        return super(BCP47LanguageTag, cls).__new__(cls, language, script, region, variant, extension, private)

    @classmethod
    def fromstring(cls, bcp47_string):
        language = None
        script = None
        region = None
        variant = None
        extension = None
        private = None
        
        _singleton = ''
        _grandfathered = False

        cls._registry = load_registry()
        
        if bcp47_string.translate(_ascii_lower_trans) in cls._registry['grandfathered']:
            language = bcp47_string
            return super(BCP47LanguageTag, cls).__new__(cls, language, script,
                                                        region, variant,
                                                        extension, private)

        subtags = bcp47_string.split('-')
        process_extension = False
        for idx, subtag in enumerate(subtags):
            subtag_len = len(subtag)
            if subtag_len == 0:
                warnings.warn('Zero length subtag found', BCP47NotWellFormed)
                continue
            
            if process_extension:
                if subtag == 'x':
                    process_extension = False
                else:
                    if _singleton not in extension:
                        extension[_singleton] = subtag
                    else:
                        if not isinstance(extension[_singleton], list):
                            extension[_singleton] = [extension[_singleton]]
                        extension[_singleton].append(subtag)
                    continue

            if subtag == 'x':
                for ptag in subtags[idx + 1:]:
                    if private is None:
                        private = ptag
                    else:
                        if not isinstance(private, list):
                            private = [private]
                        private.append(ptag)
                    if len(ptag) > 8:
                        warnings.warn('Private subtag %s length > 8' % subtag,
                                      BCP47NotWellFormed)
                break

            if subtag_len == 1:
                if language is None:
                    warnings.warn('extension subtag %s found before primary language subtag' % subtag,
                                  BCP47NotWellFormed)
                
                if extension is None:
                    extension = {}

                if subtag in extension:
                    warnings.warn('Repeated extension %s' % subtag,
                                  BCP47NotWellFormed)
                else:
                    _singleton = subtag
                    process_extension = True
                continue

            # language
            if language is None:
                if subtag_len > 8:
                    warnings.warn('Language tag %s length > 8 characters' % subtag,
                                  BCP47NotWellFormed)
                language = BCP47LanguageTag._format_language(subtag)
                continue

            all_digits = all([ch in '0123456789' for ch in subtag])

            # extlang
            if language is not None and subtag_len == 3 and not all_digits:
                extlang = BCP47LanguageTag._format_language(subtag)
                language = language + ('-%s' % extlang)
                continue

            # script
            if script is None and subtag_len == 4 and not all_digits:
                script = BCP47LanguageTag._format_script(subtag)
                continue

            # region
            if region is None and (subtag_len == 2 or (subtag_len == 3 and all_digits)):
                region = BCP47LanguageTag._format_region(subtag)
                continue

            if variant is None:
                variant = []
            variant.append(subtag)

        return super(BCP47LanguageTag, cls).__new__(cls, language, script,
                                                    region, variant,
                                                    extension, private)

    def __str__(self):
        tag = ''
        if self.language:
            tag = BCP47LanguageTag._format_language(self.language)
        if self.script:
            if tag:
                tag = tag + '-'
            tag = tag + BCP47LanguageTag._format_script(self.script)
        if self.region:
            if tag:
                tag = tag + '-'
            tag = tag + BCP47LanguageTag._format_region(self.region)
        if self.variant:
            if tag:
                tag = tag + '-'
            tag = tag + '%s' % '-'.join(self.variant)
        if self.extension:
            if tag:
                tag = tag + '-'
            order = list(self.extension.keys())
            order.sort(key=lambda s: s.translate(_ascii_lower_trans))
            for ext in order:
                value = self.extension[ext]
                if isinstance(value, list):
                    value = '-'.join(value)
                tag = tag + '%s-%s' % (ext, value)
        if self.private:
            if tag:
                tag = tag + '-'
            try:
                if isinstance(self.private, list):
                    value = '-'.join(self.private)
                else:
                    value = self.private
            except TypeError:
                pass
            tag = tag + 'x-%s' % value
            
        return tag

    def __eq__(self, tag):
        self_lower = str(self).translate(_ascii_lower_trans)
        tag_lower = str(tag).translate(_ascii_lower_trans)
        return self_lower == tag_lower

    def isvalid(self):
        if self.language:
            if self.language in self._registry['grandfathered']:
                return True
            
            lang_elems = self.language.split('-')
            if lang_elems[0] not in self._registry['language']:
                return False

            if len(lang_elems) > 4:
                return False
    
            if len(lang_elems) > 1:
                for elem in lang_elems[1:]:
                    if len(elem) > 3:
                        return False
                    
                    entry = self._registry['extlang'].get(elem, None)
                    if entry is None:
                        return False
                    
                    if entry['prefix'] != lang_elems[0]:
                        return False

        if self.script and self.script not in self._registry['script']:
            return False

        if self.region and self.region not in self._registry['region']:
            return False

        return True
    
    @staticmethod
    def _valid_subtag(subtag):
        valid_chars = string.ascii_letters + string.digits + '-'
        return all([x in valid_chars for x in subtag])

    @staticmethod
    def _format_language(subtag):
        return subtag.strip().translate(_ascii_lower_trans)

    @staticmethod
    def _format_script(subtag):
        subtag = subtag.strip()
        return subtag[0].translate(_ascii_upper_trans) + subtag[1:].translate(_ascii_lower_trans)

    @staticmethod
    def _format_region(subtag):
        return subtag.strip().translate(_ascii_upper_trans)
    