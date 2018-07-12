# -*- coding: utf-8 -*-
#
# This source code is made available under the
# Creative Commons Attribution-Share-Alike License 3.0 or later
# http://creativecommons.org/licenses/by-sa/3.0/
#
# ISO 15924 data taken from the following page
# http://unicode.org/iso15924/iso15924-codes.html

from __future__ import unicode_literals
from collections import namedtuple

__all__ = ['Scripts']

Iso15924Info = namedtuple('Iso15924Info', ['code', 'number', 'name'])


ISO15924_INFO = [
    Iso15924Info('Adlm', 166, 'Adlam'),
    Iso15924Info('Afak', 439, 'Afaka'),
    Iso15924Info('Aghb', 239, 'Caucasian Albanian'),
    Iso15924Info('Ahom', 338, 'Ahom, Tai Ahom'),
    Iso15924Info('Arab', 160, 'Arabic'),
    Iso15924Info('Aran', 161, 'Arabic (Nastaliq variant)'),
    Iso15924Info('Armi', 124, 'Imperial Aramaic'),
    Iso15924Info('Armn', 230, 'Armenian'),
    Iso15924Info('Avst', 134, 'Avestan'),
    Iso15924Info('Bali', 360, 'Balinese'),
    Iso15924Info('Bamu', 435, 'Bamum'),
    Iso15924Info('Bass', 259, 'Bassa Vah'),
    Iso15924Info('Batk', 365, 'Batak'),
    Iso15924Info('Beng', 325, 'Bengali'),
    Iso15924Info('Bhks', 334, 'Bhaiksuki'),
    Iso15924Info('Blis', 550, 'Blissymbols'),
    Iso15924Info('Bopo', 285, 'Bopomofo'),
    Iso15924Info('Brah', 300, 'Brahmi'),
    Iso15924Info('Brai', 570, 'Braille'),
    Iso15924Info('Bugi', 367, 'Buginese'),
    Iso15924Info('Buhd', 372, 'Buhid'),
    Iso15924Info('Cakm', 349, 'Chakma'),
    Iso15924Info('Cans', 440, 'Unified Canadian Aboriginal Syllabics'),
    Iso15924Info('Cari', 201, 'Carian'),
    Iso15924Info('Cham', 358, 'Cham'),
    Iso15924Info('Cher', 445, 'Cherokee'),
    Iso15924Info('Cirt', 291, 'Cirth'),
    Iso15924Info('Copt', 204, 'Coptic'),
    Iso15924Info('Cprt', 403, 'Cypriot'),
    Iso15924Info('Cyrl', 220, 'Cyrillic'),
    Iso15924Info('Cyrs', 221, 'Cyrillic (Old Church Slavonic variant)'),
    Iso15924Info('Deva', 315, 'Devanagari (Nagari)'),
    Iso15924Info('Dsrt', 250, 'Deseret (Mormon)'),
    Iso15924Info('Dupl', 755, 'Duployan shorthand, Duployan stenography'),
    Iso15924Info('Egyd', 70, 'Egyptian demotic`'),
    Iso15924Info('Egyh', 60, 'Egyptian hieratic'),
    Iso15924Info('Egyp', 50, 'Egyptian hieroglyphs'),
    Iso15924Info('Elba', 226, 'Elbasan'),
    Iso15924Info('Ethi', 430, 'Ethiopic (Geʻez)'),
    Iso15924Info('Geok', 241, 'Khutsuri (Asomtavruli and Nuskhuri)'),
    Iso15924Info('Geor', 240, 'Georgian (Mkhedruli)'),
    Iso15924Info('Glag', 225, 'Glagolitic'),
    Iso15924Info('Goth', 206, 'Gothic'),
    Iso15924Info('Gran', 343, 'Grantha'),
    Iso15924Info('Grek', 200, 'Greek'),
    Iso15924Info('Gujr', 320, 'Gujarati'),
    Iso15924Info('Guru', 310, 'Gurmukhi'),
    Iso15924Info('Hang', 286, 'Hangul (Hangŭl), Hangeul)'),
    Iso15924Info('Hani', 500, 'Han (Hanzi), Kanji), Hanja)'),
    Iso15924Info('Hano', 371, 'Hanunoo (Hanunóo)'),
    Iso15924Info('Hans', 501, 'Han (Simplified variant)'),
    Iso15924Info('Hant', 502, 'Han (Traditional variant)'),
    Iso15924Info('Hatr', 127, 'Hatran'),
    Iso15924Info('Hebr', 125, 'Hebrew'),
    Iso15924Info('Hira', 410, 'Hiragana'),
    Iso15924Info('Hluw', 80, 'Anatolian Hieroglyphs (Luwian Hieroglyphs), Hittite Hieroglyphs)'),
    Iso15924Info('Hmng', 450, 'Pahawh Hmong'),
    Iso15924Info('Hrkt', 412, 'Japanese syllabaries (alias for Hiragana + Katakana)'),
    Iso15924Info('Hung', 176, 'Old Hungarian (Hungarian Runic)'),
    Iso15924Info('Inds', 610, 'Indus (Harappan)'),
    Iso15924Info('Ital', 210, 'Old Italic (Etruscan), Oscan), etc.)'),
    Iso15924Info('Java', 361, 'Javanese'),
    Iso15924Info('Jpan', 413, 'Japanese (alias for Han + Hiragana + Katakana)'),
    Iso15924Info('Jurc', 510, 'Jurchen'),
    Iso15924Info('Kali', 357, 'Kayah Li'),
    Iso15924Info('Kana', 411, 'Katakana'),
    Iso15924Info('Khar', 305, 'Kharoshthi'),
    Iso15924Info('Khmr', 355, 'Khmer'),
    Iso15924Info('Khoj', 322, 'Khojki'),
    Iso15924Info('Kitl', 505, 'Khitan large script'),
    Iso15924Info('Kits', 288, 'Khitan small script'),
    Iso15924Info('Knda', 345, 'Kannada'),
    Iso15924Info('Kore', 387, 'Korean (alias for Hangul + Han)'),
    Iso15924Info('Kpel', 436, 'Kpelle'),
    Iso15924Info('Kthi', 317, 'Kaithi'),
    Iso15924Info('Lana', 351, 'Tai Tham (Lanna)'),
    Iso15924Info('Laoo', 356, 'Lao'),
    Iso15924Info('Latf', 217, 'Latin (Fraktur variant)'),
    Iso15924Info('Latg', 216, 'Latin (Gaelic variant)'),
    Iso15924Info('Latn', 215, 'Latin'),
    Iso15924Info('Leke', 364, 'Leke'),
    Iso15924Info('Lepc', 335, 'Lepcha (Róng)'),
    Iso15924Info('Limb', 336, 'Limbu'),
    Iso15924Info('Lina', 400, 'Linear A'),
    Iso15924Info('Linb', 401, 'Linear B'),
    Iso15924Info('Lisu', 399, 'Lisu (Fraser)'),
    Iso15924Info('Loma', 437, 'Loma'),
    Iso15924Info('Lyci', 202, 'Lycian'),
    Iso15924Info('Lydi', 116, 'Lydian'),
    Iso15924Info('Mahj', 314, 'Mahajani'),
    Iso15924Info('Mand', 140, 'Mandaic, Mandaean'),
    Iso15924Info('Mani', 139, 'Manichaean'),
    Iso15924Info('Marc', 332, 'Marchen'),
    Iso15924Info('Maya', 90, 'Mayan hieroglyphs'),
    Iso15924Info('Mend', 438, 'Mende Kikakui'),
    Iso15924Info('Merc', 101, 'Meroitic Cursive'),
    Iso15924Info('Mero', 100, 'Meroitic Hieroglyphs'),
    Iso15924Info('Mlym', 347, 'Malayalam'),
    Iso15924Info('Modi', 324, 'Modi, Moḍī'),
    Iso15924Info('Mong', 145, 'Mongolian'),
    Iso15924Info('Moon', 218, 'Moon (Moon code, Moon script, Moon type)'),
    Iso15924Info('Mroo', 199, 'Mro, Mru'),
    Iso15924Info('Mtei', 337, 'Meitei Mayek (Meithei), Meetei)'),
    Iso15924Info('Mult', 323, 'Multani'),
    Iso15924Info('Mymr', 350, 'Myanmar (Burmese)'),
    Iso15924Info('Narb', 106, 'Old North Arabian (Ancient North Arabian)'),
    Iso15924Info('Nbat', 159, 'Nabataean'),
    Iso15924Info('Nkgb', 420, 'Nakhi Geba (\'Na-\'Khi ²Ggŏ-¹baw), Naxi Geba)'),
    Iso15924Info('Nkoo', 165, 'N’Ko'),
    Iso15924Info('Nshu', 499, 'Nüshu'),
    Iso15924Info('Ogam', 212, 'Ogham'),
    Iso15924Info('Olck', 261, 'Ol Chiki (Ol Cemet’, Ol, Santali)'),
    Iso15924Info('Orkh', 175, 'Old Turkic, Orkhon Runic'),
    Iso15924Info('Orya', 327, 'Oriya'),
    Iso15924Info('Osge', 219, 'Osage'),
    Iso15924Info('Osma', 260, 'Osmanya'),
    Iso15924Info('Palm', 126, 'Palmyrene'),
    Iso15924Info('Pauc', 263, 'Pau Cin Ha'),
    Iso15924Info('Perm', 227, 'Old Permic'),
    Iso15924Info('Phag', 331, 'Phags-pa'),
    Iso15924Info('Phli', 131, 'Inscriptional Pahlavi'),
    Iso15924Info('Phlp', 132, 'Psalter Pahlavi'),
    Iso15924Info('Phlv', 133, 'Book Pahlavi'),
    Iso15924Info('Phnx', 115, 'Phoenician'),
    Iso15924Info('Plrd', 282, 'Miao (Pollard)'),
    Iso15924Info('Prti', 130, 'Inscriptional Parthian'),
    Iso15924Info('Rjng', 363, 'Rejang (Redjang), Kaganga)'),
    Iso15924Info('Roro', 620, 'Rongorongo'),
    Iso15924Info('Runr', 211, 'Runic'),
    Iso15924Info('Samr', 123, 'Samaritan'),
    Iso15924Info('Sara', 292, 'Sarati'),
    Iso15924Info('Sarb', 105, 'Old South Arabian'),
    Iso15924Info('Saur', 344, 'Saurashtra'),
    Iso15924Info('Sgnw', 95, 'SignWriting'),
    Iso15924Info('Shaw', 281, 'Shavian (Shaw)'),
    Iso15924Info('Shrd', 319, 'Sharada, Śāradā'),
    Iso15924Info('Sidd', 302, 'Siddham, Siddhaṃ, Siddhamātṛkā'),
    Iso15924Info('Sind', 318, 'Khudawadi), Sindhi'),
    Iso15924Info('Sinh', 348, 'Sinhala'),
    Iso15924Info('Sora', 398, 'Sora Sompeng'),
    Iso15924Info('Sund', 362, 'Sundanese'),
    Iso15924Info('Sylo', 316, 'Syloti Nagri'),
    Iso15924Info('Syrc', 135, 'Syriac'),
    Iso15924Info('Syre', 138, 'Syriac (Estrangelo variant)'),
    Iso15924Info('Syrj', 137, 'Syriac (Western variant)'),
    Iso15924Info('Syrn', 136, 'Syriac (Eastern variant)'),
    Iso15924Info('Tagb', 373, 'Tagbanwa'),
    Iso15924Info('Takr', 321, 'Takri, Ṭākrī, Ṭāṅkrī'),
    Iso15924Info('Tale', 353, 'Tai Le'),
    Iso15924Info('Talu', 354, 'New Tai Lue'),
    Iso15924Info('Taml', 346, 'Tamil'),
    Iso15924Info('Tang', 520, 'Tangut'),
    Iso15924Info('Tavt', 359, 'Tai Viet'),
    Iso15924Info('Telu', 340, 'Telugu'),
    Iso15924Info('Teng', 290, 'Tengwar'),
    Iso15924Info('Tfng', 120, 'Tifinagh (Berber)'),
    Iso15924Info('Tglg', 370, 'Tagalog (Baybayin), Alibata)'),
    Iso15924Info('Thaa', 170, 'Thaana'),
    Iso15924Info('Thai', 352, 'Thai'),
    Iso15924Info('Tibt', 330, 'Tibetan'),
    Iso15924Info('Tirh', 326, 'Tirhuta'),
    Iso15924Info('Ugar', 40, 'Ugaritic'),
    Iso15924Info('Vaii', 470, 'Vai'),
    Iso15924Info('Visp', 280, 'Visible Speech'),
    Iso15924Info('Wara', 262, 'Warang Citi (Varang Kshiti)'),
    Iso15924Info('Wole', 480, 'Woleai'),
    Iso15924Info('Xpeo', 30, 'Old Persian'),
    Iso15924Info('Xsux', 20, 'Cuneiform, Sumero-Akkadian'),
    Iso15924Info('Yiii', 460, 'Yi'),
    Iso15924Info('Zinh', 994, 'Code for inherited script'),
    Iso15924Info('Zmth', 995, 'Mathematical notation'),
    Iso15924Info('Zsym', 996, 'Symbols'),
    Iso15924Info('Zxxx', 997, 'Code for unwritten documents'),
    Iso15924Info('Zyyy', 998, 'Code for undetermined script'),
    Iso15924Info('Zzzz', 999, 'Code for uncoded script'),
]


class Iso15924Scripts():
    def __init__(self):
        self._code = None
        self._number = None
    
    def __getitem__(self, key):
        try:
            n = int(key)
            if self._number_isprivate(n):
                code = 'Qa%s%s' % (chr(int((n - 900) / 26) + ord('a')),
                                   chr(((n - 900) % 26) + ord('a')))
                return Iso15924Info(code, n, 'Reserved for private use')
            else:
                return self.number[key]
        except ValueError:
            if self._code_isprivate(key):
                num = 900 + ((ord(key[2]) - ord('a')) * 26) + (ord(key[3]) - ord('a'))
                return Iso15924Info(key, num, 'Reserved for private use')
            else:
                return self.code[self._transform_key(key)]

    def __contains__(self, key):
        if self._is_private(key):
            return True
        return self.code.__contains__(self._transform_key(key))

    def _is_private(self, key):
        try:
            cp = self._code_isprivate(str(key))
        except:
            cp = False

        try:
            np = self._number_isprivate(int(key))
        except:
            np = False
        
        return cp or np

    def _code_isprivate(self, code):
        code = str(code).lower()
        if code[:2] != 'qa':
            return False
        else:
            return code[2:] >= 'aa' and code[2:] <= 'bx'

    def _number_isprivate(self, number):
        return number >= 900 and number <= 949
    
    def _transform_key(self, key):
        return key[0].upper() + key[1:].lower()

    @property
    def code(self):
        if self._code is None:
            self._code = {}
            for info in ISO15924_INFO:
                self._code[info.code] = info
            return self._code
        else:
            return self._code

    @property
    def number(self):
        if self._number is None:
            self._number = {}
            for info in ISO15924_INFO:
                self._number[info.number] = info
            return self._number
        else:
            return self._number
    

Scripts = Iso15924Scripts()
