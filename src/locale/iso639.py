# -*- coding: utf-8 -*-
#
# This source code is made available under the
# Creative Commons Attribution-Share-Alike License 3.0 or later
# http://creativecommons.org/licenses/by-sa/3.0/
#
# ISO 639 data taken from the following Wikipedia page
# http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

# and Library of Congress
# http://www-01.sil.org/iso639-3/codes.asp
# http://www-01.sil.org/iso639-3/download.asp

from __future__ import unicode_literals
from collections import namedtuple

__all__ = ['Languages']

Iso639Info = namedtuple('Iso639Info', ['iso639_1',
                                       'iso639_2T', 'iso639_2B',
                                       'iso639_3',
                                       'name', 'native_name'])

ISO639_INFO = [
    Iso639Info(None, None,  None,  'aaa', 'Ghotuo', ('Otwa', 'Otuo')),
    Iso639Info(None, None,  None,  'aab', 'Alumu-Tesu', None),
    Iso639Info(None, None,  None,  'aac', 'Ari', None),
    Iso639Info(None, None,  None,  'aad', 'Amal', None),
    Iso639Info(None, None,  None,  'aae', 'Arbëreshë Albanian', None),
    Iso639Info(None, None,  None,  'aaf', 'Aranadan', None),
    Iso639Info(None, None,  None,  'aag', 'Ambrak', None),
    Iso639Info(None, None,  None,  'aah', 'Abu\' Arapesh', None),
    Iso639Info(None, None,  None,  'aai', 'Arifama-Miniafia', None),
    Iso639Info(None, None,  None,  'aak', 'Ankave', None),
    Iso639Info(None, None,  None,  'aal', 'Afade', None),
    Iso639Info(None, None,  None,  'aan', 'Anambé', None),
    Iso639Info(None, None,  None,  'aao', 'Algerian Saharan Arabic', None),
    Iso639Info(None, None,  None,  'aap', 'Pará Arára', None),
    Iso639Info(None, None,  None,  'aaq', 'Eastern Abnaki', None),
    Iso639Info('aa', 'aar', 'aar', 'aar', 'Afar', 'Afaraf'),
    Iso639Info(None, None,  None,  'aas', 'Aasáx', None),
    Iso639Info(None, None,  None,  'aat', 'Arvanitika Albanian', None),
    Iso639Info(None, None,  None,  'aau', 'Abau', None),
    Iso639Info(None, None,  None,  'aaw', 'Solong', None),
    Iso639Info(None, None,  None,  'aax', 'Mandobo Atas', None),
    Iso639Info(None, None,  None,  'aaz', 'Amarasi', None),
    Iso639Info(None, None,  None,  'aba', 'Abé', None),
    Iso639Info(None, None,  None,  'abb', 'Bankon', None),
    Iso639Info(None, None,  None,  'abc', 'Ambala Ayta', None),
    Iso639Info(None, None,  None,  'abd', 'Manide', None),
    Iso639Info(None, None,  None,  'abe', 'Western Abnaki', None),
    Iso639Info(None, None,  None,  'abf', 'Abai Sungai', None),
    Iso639Info(None, None,  None,  'abg', 'Abaga', None),
    Iso639Info(None, None,  None,  'abh', 'Tajiki Arabic', None),
    Iso639Info(None, None,  None,  'abi', 'Abidji', None),
    Iso639Info(None, None,  None,  'abj', 'Aka-Bea', None),
    Iso639Info('ab', 'abk', 'abk', 'abk', 'Abkhazian', 'аҧсуа бызшәа, аҧсшәа'),
    Iso639Info(None, None,  None,  'abl', 'Lampung Nyo', None),
    Iso639Info(None, None,  None,  'abm', 'Abanyom', None),
    Iso639Info(None, None,  None,  'abn', 'Abua', None),
    Iso639Info(None, None,  None,  'abo', 'Abon', None),
    Iso639Info(None, None,  None,  'abp', 'Abellen Ayta', None),
    Iso639Info(None, None,  None,  'abq', 'Abaza', None),
    Iso639Info(None, None,  None,  'abr', 'Abron', None),
    Iso639Info(None, None,  None,  'abs', 'Ambonese Malay', None),
    Iso639Info(None, None,  None,  'abt', 'Ambulas', None),
    Iso639Info(None, None,  None,  'abu', 'Abure', None),
    Iso639Info(None, None,  None,  'abv', 'Baharna Arabic', None),
    Iso639Info(None, None,  None,  'abw', 'Pal', None),
    Iso639Info(None, None,  None,  'abx', 'Inabaknon', None),
    Iso639Info(None, None,  None,  'aby', 'Aneme Wake', None),
    Iso639Info(None, None,  None,  'abz', 'Abui', None),
    Iso639Info(None, None,  None,  'aca', 'Achagua', None),
    Iso639Info(None, None,  None,  'acb', 'Áncá', None),
    Iso639Info(None, None,  None,  'acd', 'Gikyode', None),
    Iso639Info(None, 'ace', None,  'ace', 'Acehnese', ('Bahsa', 'Basa Acèh')),
    Iso639Info(None, None,  None,  'acf', 'Saint Lucian Creole French', None),
    Iso639Info(None, 'ach', None,  'ach', 'Acoli', None),
    Iso639Info(None, None,  None,  'aci', 'Aka-Cari', None),
    Iso639Info(None, None,  None,  'ack', 'Aka-Kora', None),
    Iso639Info(None, None,  None,  'acl', 'Aka-Bale', None),
    Iso639Info(None, None,  None,  'acm', 'Mesopotamian Arabic', None),
    Iso639Info(None, None,  None,  'acn', 'Achang', None),
    Iso639Info(None, None,  None,  'acp', 'Eastern Acipa', None),
    Iso639Info(None, None,  None,  'acq', 'Ta\'izzi-Adeni Arabic', None),
    Iso639Info('af', 'afr', 'afr', 'afr', 'Afrikaans', 'Afrikaans'),
    Iso639Info('ak', 'aka', 'aka', 'aka', 'Akan', 'Akan'),
    Iso639Info('am', 'amh', 'amh', 'amh', 'Amharic', 'አማርኛ'),
    Iso639Info('ar', 'ara', 'ara', 'ara', 'Arabic', 'العربية'),
    Iso639Info('an', 'arg', 'arg', 'arg', 'Aragonese', 'aragonés'),
    Iso639Info('as', 'asm', 'asm', 'asm', 'Assamese', 'অসমীয়া'),
    Iso639Info('av', 'ava', 'ava', 'ava', 'Avaric', ('авар мацӀয়', 'магӀарул мацӀ')),
    Iso639Info('ae', 'ave', 'ave', 'ave', 'Avestan', 'avesta'),
    Iso639Info('ay', 'aym', 'aym', 'aym', 'Aymara', 'aymar ar'),
    Iso639Info('az', 'aze', 'aze', 'aze', 'Azerbaijani', 'azərbaycan dili'),
    Iso639Info('ba', 'bak', 'bak', 'bak', 'Bashkir', 'башҡорт теле'),
    Iso639Info('bm', 'bam', 'bam', 'bam', 'Bambara', 'bamanankan'),
    Iso639Info('be', 'bel', 'bel', 'bel', 'Belarusian', 'беларуская мова'),
    Iso639Info('bn', 'ben', 'ben', 'ben', 'Bengali', 'বাংলা'),
    Iso639Info('bi', 'bih', 'bih', 'bih', 'Bihari', 'भोजपुरीলা'),
    Iso639Info('bi', 'bis', 'bis', 'bis', 'Bislama', 'Bislama'),
    Iso639Info('bd', 'bod', 'tib', 'bod', ('Tibetan Standard', 'Tibetan Central'), 'བོད་ཡིག'),
    Iso639Info('bs', 'bos', 'bos', 'bos', 'Bosnian', 'bosanski jezik'),
    Iso639Info('be', 'bre', 'bre', 'bre', 'Breton', 'brezhoneg'),
    Iso639Info('bg', 'bul', 'bul', 'bul', 'Bulgarian', 'български език'),
    Iso639Info('ca', 'cat', 'cat', 'cat', ('Catalan', 'Valencian'), ('català', 'valencià')),
    Iso639Info('cs', 'ces', 'cze', 'ces', 'Czech', ('čeština', 'český jazyk')),
    Iso639Info('ch', 'cha', 'cha', 'cha', 'Chamorro', 'Chamor'),
    Iso639Info('ce', 'che', 'che', 'che', 'Chechen', 'нохчийн мотт'),
    Iso639Info('cu', 'chu', 'chu', 'chu', ('Old Church Slavonic', 'Church Slavic', 'Church Slavonic', 'Old Bulgarian', 'Old Slavonic'), 'ѩзыкъ словѣньскъ'),
    Iso639Info('cv', 'chv', 'chv', 'chv', 'Chuvash', 'чӑваш чӗлхи'),
    Iso639Info('kw', 'cor', 'cor', 'cor', 'Cornish', 'Kernewek'),
    Iso639Info('cr', 'cre', 'cre', 'cre', 'Cree', 'ᓀᐦᐃᔭᐍᐏᐣ'),
    Iso639Info('co', 'cos', 'cos', 'cos', 'Corsican', ('cors', 'lingua corsa')),
    Iso639Info('we', 'cym', 'wel', 'cym', 'Welsh', 'Cymraeg'),
    Iso639Info('da', 'dan', 'dan', 'dan', 'Danish', 'dansk'),
    Iso639Info('de', 'deu', 'ger', 'deu', 'German', 'Deutsch'),
    Iso639Info('dv', 'div', 'div', 'div', ('Divehi', 'Dhivehi', 'Maldivian'), 'ދިވެހި'),
    Iso639Info('dz', 'dzo', 'dzo', 'dzo', 'Dzongkha', 'རྫོང་ཁ'),
    Iso639Info('el', 'ell', 'gre', 'ell', 'Greek', ('ελληνική γλώσσα', 'ελληνικά')),
    Iso639Info('en', 'eng', 'eng', 'eng', 'English', 'English'),
    Iso639Info('eo', 'epo', 'epo', 'epo', 'Esperanto', 'Esperanto'),
    Iso639Info('et', 'est', 'est', 'est', 'Estonian', ('eesti', 'eesti keel')),
    Iso639Info('eu', 'eus', 'baq', 'eus', 'Basque', ('euskara', 'euskera')),
    Iso639Info('ee', 'ewe', 'ewe', 'ewe', 'Ewe', 'Eʋegbe'),
    Iso639Info('fo', 'fao', 'fao', 'fao', 'Faroese', 'føroyskt'),
    Iso639Info('fa', 'fas', 'per', 'fas', 'Persian', 'فارسی'),
    Iso639Info('fj', 'fij', 'fij', 'fij', 'Fijian', 'vosa Vakaviti'),
    Iso639Info('fi', 'fin', 'fin', 'fin', 'Finnish', ('suomi', 'suomen kieli')),
    Iso639Info('fr', 'fre', 'fra', 'fre', 'French', ('français', 'langue française')),
    Iso639Info('ff', 'ful', 'ful', 'ful', ('Fula', 'Fulah', 'Pulaar', 'Pular'), ('Fulfulde', 'Pulaar', 'Pular')),
    Iso639Info('gd', 'gla', 'gla', 'gla', ('Scottish Gaelic', 'Gaelic'), 'Gàidhlig'),
    Iso639Info('ga', 'gle', 'gle', 'gle', 'Irish', 'Gaeilge'),
    Iso639Info('gl', 'glg', 'glg', 'glg', 'Galician', 'galego'),
    Iso639Info('gv', 'glv', 'glv', 'glv', 'Manx', ('Gaelg', 'Gailck')),
    Iso639Info('gn', 'grn', 'grn', 'grn', 'Guaraní', 'Avañe\'ẽ'),
    Iso639Info('gu', 'guj', 'guj', 'guj', 'Gujarati', 'ગુજરાતી'),
    Iso639Info('ht', 'hat', 'hat', 'hat', ('Haitian', 'Haitian Creole'), 'Kreyòl ayisyen'),
    Iso639Info('ha', 'hau', 'hau', 'hau', 'Hausa', ('هَوُسَ', 'Hausa')),
    Iso639Info('he', 'heb', 'heb', 'heb', 'Hebrew', 'עברית'),
    Iso639Info('hz', 'her', 'her', 'her', 'Herero', 'Otjiherero'),
    Iso639Info('hi', 'hin', 'hin', 'hin', 'Hindi', ('हिन्दी', 'हिंदी')),
    Iso639Info('ho', 'hmo', 'hmo', 'hmo', 'Hiri Mot', 'Hiri Mot'),
    Iso639Info('hr', 'hrv', 'hrv', 'hrv', 'Croatian', 'hrvatski jezik'),
    Iso639Info('hu', 'hun', 'hun', 'hun', 'Hungarian', 'Magyar'),
    Iso639Info('hy', 'hye', 'arm', 'hye', 'Armenian', 'Հայերեն'),
    Iso639Info('ig', 'ibo', 'ibo', 'ibo', 'Igbo', 'Asụsụ Igbo'),
    Iso639Info('io', 'ido', 'ido', 'ido', 'Ido', 'Ido'),
    Iso639Info('ii', 'iii', 'iii', 'iii', 'Nuos', 'ꆈꌠ꒿ Nuosuhxop'),
    Iso639Info('iu', 'iku', 'iku', 'iku', 'Inuktitut', 'ᐃᓄᒃᑎᑐᑦ'),
    Iso639Info('ie', 'ile', 'ile', 'ile', 'Interlingue', ('Occidental', 'Interlingue')),
    Iso639Info('ia', 'ina', 'ina', 'ina', 'Interlingua', 'Interlingua'),
    Iso639Info('id', 'ind', 'ind', 'ind', 'Indonesian', 'Bahasa Indonesia'),
    Iso639Info('ik', 'ipk', 'ipk', 'ipk', 'Inupiaq', ('Iñupiaq', 'Iñupiatun')),
    Iso639Info('is', 'isl', 'ice', 'isl', 'Icelandic', 'Íslenska'),
    Iso639Info('it', 'ita', 'ita', 'ita', 'Italian', 'Italiano'),
    Iso639Info('jv', 'jav', 'jav', 'jav', 'Javanese', 'basa Jawa'),
    Iso639Info('ja', 'jpn', 'jpn', 'jpn', 'Japanese', '日本語'),
    Iso639Info('kl', 'kal', 'kal', 'kal', ('Kalaallisut', 'Greenlandic'), ('kalaallisut', 'kalaallit oqaasii')),
    Iso639Info('kn', 'kan', 'kan', 'kan', 'Kannada', 'ಕನ್ನಡ'),
    Iso639Info('ks', 'kas', 'kas', 'kas', 'Kashmiri', ('कश्मीरी', 'كشميري‎')),
    Iso639Info('ka', 'kat', 'geo', 'kat', 'Georgian', 'ქართული'),
    Iso639Info('kr', 'kau', 'kau', 'kau', 'Kanuri', 'Kanuri'),
    Iso639Info('kk', 'kaz', 'kaz', 'kaz', 'Kazakh', 'қазақ тілі'),
    Iso639Info('km', 'khm', 'khm', 'khm', 'Khmer', 'ខ្មែរ, ខេមរភាសា, ភាសាខ្មែរ'),
    Iso639Info('ki', 'kik', 'kik', 'kik', ('Kikuy', 'Gikuy'), 'Gĩkũyũ'),
    Iso639Info('rw', 'kin', 'kin', 'kin', 'Kinyarwanda', 'Ikinyarwanda'),
    Iso639Info('ky', 'kir', 'kir', 'kir', ('Kirghiz', 'Kyrgyz'), 'кыргыз тили'),
    Iso639Info('kv', 'kom', 'kom', 'kom', 'Komi', 'коми кыв'),
    Iso639Info('kg', 'kon', 'kon', 'kon', 'Kongo', 'KiKongo'),
    Iso639Info('ko', 'kor', 'kor', 'kor', 'Korean', ('한국어 (韓國語)', '조선어 (朝鮮語)')),
    Iso639Info('kj', 'kua', 'kua', 'kua', ('Kwanyama', 'Kuanyama'), 'Kuanyama'),
    Iso639Info('ku', 'kur', 'kur', 'kur', 'Kurdish', ('Kurdî', 'كوردی‎')),
    Iso639Info('lo', 'lao', 'lao', 'lao', 'Lao', 'ພາສາລາວ'),
    Iso639Info('la', 'lat', 'lat', 'lat', 'Latin', ('latine', 'lingua latina')),
    Iso639Info('lv', 'lav', 'lav', 'lav', 'Latvian', 'latviešu valoda'),
    Iso639Info('li', 'lim', 'lim', 'lim', ('Limburgish', 'Limburgan', 'Limburger'), 'Limburgs'),
    Iso639Info('ln', 'lin', 'lin', 'lin', 'Lingala', 'Lingála'),
    Iso639Info('lt', 'lit', 'lit', 'lit', 'Lithuanian', 'lietuvių kalba'),
    Iso639Info('lb', 'ltz', 'ltz', 'ltz', ('Luxembourgish', 'Letzeburgesch'), 'Lëtzebuergesch'),
    Iso639Info('lu', 'lub', 'lub', 'lub', 'Luba-Katanga', 'Luba-Katanga'),
    Iso639Info('lg', 'lug', 'lug', 'lug', 'Luganda', 'Luganda'),
    Iso639Info('mh', 'mah', 'mah', 'mah', 'Marshallese', 'Kajin M̧ajeļ'),
    Iso639Info('ml', 'mal', 'mal', 'mal', 'Malayalam', 'മലയാളം'),
    Iso639Info('mr', 'mar', 'mar', 'mar', 'Marāṭhī', 'मराठी'),
    Iso639Info('mk', 'mkd', 'mac', 'mkd', 'Macedonian', 'македонски јазик'),
    Iso639Info('mg', 'mlg', 'mlg', 'mlg', 'Malagasy', 'Malagasy fiteny'),
    Iso639Info('mt', 'mlt', 'mlt', 'mlt', 'Maltese', 'Malti'),
    Iso639Info('mn', 'mon', 'mon', 'mon', 'Mongolian', 'монгол'),
    Iso639Info('mi', 'mri', 'mao', 'mri', 'Māori', 'te reo Māori'),
    Iso639Info('ms', 'msa', 'may', 'msa', 'Malay', ('bahasa Melay', 'بهاس ملايو‎')),
    Iso639Info('my', 'mya', 'bur', 'mya', 'Burmese', 'ဗမာစာ'),
    Iso639Info('na', 'nau', 'nau', 'nau', 'Naur', 'Ekakairũ Naoero'),
    Iso639Info('nv', 'nav', 'nav', 'nav', ('Navajo', 'Navaho'), ('Diné bizaad', 'Dinékʼehǰí')),
    Iso639Info('nr', 'nbl', 'nbl', 'nbl', 'South Ndebele', 'isiNdebele'),
    Iso639Info('nd', 'nde', 'nde', 'nde', 'North Ndebele', 'isiNdebele'),
    Iso639Info('ng', 'ndo', 'ndo', 'ndo', 'Ndonga', 'Owambo'),
    Iso639Info('ne', 'nep', 'nep', 'nep', 'Nepali', 'नेपाली'),
    Iso639Info('nl', 'nld', 'dut', 'nld', 'Dutch', ('Nederlands', 'Vlaams')),
    Iso639Info('nn', 'nno', 'nno', 'nno', 'Norwegian Nynorsk', 'Norsk nynorsk'),
    Iso639Info('nb', 'nob', 'nob', 'nob', 'Norwegian Bokmål', 'Norsk bokmål'),
    Iso639Info('no', 'nor', 'nor', 'nor', 'Norwegian', 'Norsk'),
    Iso639Info('ny', 'nya', 'nya', 'nya', ('Chichewa', 'Chewa', 'Nyanja'), ('chiCheŵa', 'chinyanja')),
    Iso639Info('oc', 'oci', 'oci', 'oci', 'Occitan', ('occitan', 'lenga d\òc')),
    Iso639Info('oj', 'oji', 'oji', 'oji', ('Ojibwe', 'Ojibwa'), 'ᐊᓂᔑᓈᐯᒧᐎᓐ'),
    Iso639Info('or', 'ori', 'ori', 'ori', 'Oriya', 'ଓଡ଼ିଆ'),
    Iso639Info('om', 'orm', 'orm', 'orm', 'Oromo', 'Afaan Oromoo'),
    Iso639Info('os', 'oss', 'oss', 'oss', ('Ossetian', 'Ossetic'), 'ирон æвзаг'),
    Iso639Info('pa', 'pan', 'pan', 'pan', ('Panjabi', 'Punjabi'), ('ਪੰਜਾਬੀ', 'پنجابی‎')),
    Iso639Info('pi', 'pli', 'pli', 'pli', 'Pāli', 'पाऴि'),
    Iso639Info('pl', 'pol', 'pol', 'pol', 'Polish', ('język polski', 'polszczyzna')),
    Iso639Info('pt', 'por', 'por', 'por', 'Portuguese', 'português'),
    Iso639Info('ps', 'pus', 'pus', 'pus', ('Pashto', 'Pushto'), 'پښتو'),
    Iso639Info('qu', 'que', 'que', 'que', 'Quechua', ('Runa Simi', 'Kichwa')),
    Iso639Info('rm', 'ron', 'rum', 'ron', ('Romanian', 'Moldavian', 'Moldovan'), ('imba română', 'limba moldovenească')),
    Iso639Info('ru', 'rus', 'rus', 'rus', 'Russian', 'русский язык'),
    Iso639Info('sg', 'sag', 'sag', 'sag', 'Sango', 'yângâ tî sängö'),
    Iso639Info('sa', 'san', 'san', 'san', 'Sanskrit (Saṁskṛta)', 'संस्कृतम्'),
    Iso639Info('si', 'sin', 'sin', 'sin', ('Sinhala', 'Sinhalese'), 'සිංහල'),
    Iso639Info('sk', 'slk', 'slo', 'slk', 'Slovak', ('slovenčina', 'slovenský jazyk')),
    Iso639Info('sl', 'slv', 'slv', 'slv', 'Slovene', ('slovenski jezik', 'slovenščina')),
    Iso639Info('se', 'sme', 'sme', 'sme', 'Northern Sami', 'Davvisámegiella'),
    Iso639Info('sm', 'smo', 'smo', 'smo', 'Samoan', 'gagana fa\'a Samoa'),
    Iso639Info('sn', 'sna', 'sna', 'sna', 'Shona', 'chiShona'),
    Iso639Info('sd', 'snd', 'snd', 'snd', 'Sindhi', ('सिन्धी', 'سنڌي، سندھی‎')),
    Iso639Info('so', 'som', 'som', 'som', 'Somali', ('Soomaaliga', 'af Soomaali')),
    Iso639Info('st', 'sot', 'sot', 'sot', 'Southern Sotho', 'Sesotho'),
    Iso639Info('es', 'spa', 'spa', 'spa', ('Spanish', 'Castilian'), ('español', 'castellano')),
    Iso639Info('sq', 'sqi', 'alb', 'sqi', 'Albanian', 'gjuha shqipe'),
    Iso639Info('sc', 'srd', 'srd', 'srd', 'Sardinian', 'sard'),
    Iso639Info('sr', 'srp', 'srp', 'srp', 'Serbian', 'српски језик'),
    Iso639Info('ss', 'ssw', 'ssw', 'ssw', 'Swati', 'SiSwati'),
    Iso639Info('su', 'sun', 'sun', 'sun', 'Sundanese', 'Basa Sunda'),
    Iso639Info('sw', 'swa', 'swa', 'swa', 'Swahili', 'Kiswahili'),
    Iso639Info('sv', 'swe', 'swe', 'swe', 'Swedish', 'svenska'),
    Iso639Info('ty', 'tah', 'tah', 'tah', 'Tahitian', 'Reo Tahiti'),
    Iso639Info('ta', 'tam', 'tam', 'tam', 'Tamil', 'தமிழ்'),
    Iso639Info('tt', 'tat', 'tat', 'tat', 'Tatar', ('татар теле', 'tatar tele')),
    Iso639Info('te', 'tel', 'tel', 'tel', 'Telug', 'తెలుగు'),
    Iso639Info('tg', 'tgk', 'tgk', 'tgk', 'Tajik', ('тоҷикӣ', 'toğikī', 'تاجیکی‎')),
    Iso639Info('tl', 'tgl', 'tgl', 'tgl', 'Tagalog', ('Wikang Tagalog', 'ᜏᜒᜃᜅ᜔ ᜆᜄᜎᜓᜄ᜔')),
    Iso639Info('th', 'tha', 'tha', 'tha', 'Thai', 'ไทย'),
    Iso639Info('ti', 'tir', 'tir', 'tir', 'Tigrinya', 'ትግርኛ'),
    Iso639Info('to', 'ton', 'ton', 'ton', 'Tonga', 'faka Tonga'),
    Iso639Info('tn', 'tsn', 'tsn', 'tsn', 'Tswana', 'Setswana'),
    Iso639Info('ts', 'tso', 'tso', 'tso', 'Tsonga', 'Xitsonga'),
    Iso639Info('tk', 'tuk', 'tuk', 'tuk', 'Turkmen', ('Türkmen', 'Түркмен')),
    Iso639Info('tr', 'tur', 'tur', 'tur', 'Turkish', 'Türkçe'),
    Iso639Info('tw', 'twi', 'twi', 'twi', 'Twi', 'Twi'),
    Iso639Info('ug', 'uig', 'uig', 'uig', ('Uighur', 'Uyghur'), ('Uyƣurqə', 'ئۇيغۇرچە‎')),
    Iso639Info('uk', 'ukr', 'ukr', 'ukr', 'Ukrainian', 'українська мова'),
    Iso639Info('ur', 'urd', 'urd', 'urd', 'Urd', 'اردو'),
    Iso639Info('uz', 'uzb', 'uzb', 'uzb', 'Uzbek', ('O\'zbek', 'Ўзбек', 'أۇزبېك‎')),
    Iso639Info('ve', 'ven', 'ven', 'ven', 'Venda', 'Tshivenḓa'),
    Iso639Info('vi', 'vie', 'vie', 'vie', 'Vietnamese', 'Tiếng Việt'),
    Iso639Info('vo', 'vol', 'vol', 'vol', 'Volapük', 'Volapük'),
    Iso639Info('wa', 'wln', 'wln', 'wln', 'Walloon', 'walon'),
    Iso639Info('fy', 'wol', 'wol', 'wol', 'Western Frisian', 'Frysk'),
    Iso639Info('wo', 'wol', 'wol', 'wol', 'Wolof', 'Wollof'),
    Iso639Info('xh', 'xho', 'xho', 'xho', 'Xhosa', 'isiXhosa'),
    Iso639Info('yi', 'yid', 'yid', 'yid', 'Yiddish', 'ייִדיש'),
    Iso639Info('yo', 'yor', 'yor', 'yor', 'Yoruba', 'Yorùbá'),
    Iso639Info('za', 'zha', 'zha', 'zha', ('Zhuang', 'Chuang'), ('Saɯ cueŋƅ', 'Saw cuengh')),
    Iso639Info('zh', 'zho', 'chi', 'zho', 'Chinese', ('中文', '汉语', '漢語')),
    Iso639Info('zu', 'zul', 'zul', 'zul', 'Zulu', 'isiZulu'),
]


class Iso639Languages(object):
    def __init__(self):
        self._iso639_1 = None
        self._iso639_2T = None
        self._iso639_2B = None
        self._iso639_3 = None
    
    def __getitem__(self, key):
        if len(key) == 2:
            return self.iso639_1[key.lower()]
        else:
            return self.iso639_3[key.lower()]
    
    @property
    def iso639_1(self):
        if self._iso639_1 is not None:
            return self._iso639_1
        else:
            self._iso639_1 = {}
            for info in ISO639_INFO:
                self._iso639_1[info.iso639_1] = info
            return self._iso639_1

    @property    
    def iso639_2T(self):
        if self._iso639_2T is not None:
            return self._iso639_2T
        else:
            self._iso639_2T = {}
            for info in ISO639_INFO:
                self._iso639_2T[info.iso639_2T] = info
            return self._iso639_2T

    @property
    def iso639_2B(self):
        if self._iso639_2B is not None:
            return self._iso639_2B
        else:
            self._iso639_2B = {}
            for info in ISO639_INFO:
                self._iso639_2B[info.iso639_2B] = info
            return self._iso639_2B

    @property    
    def iso639_3(self):
        if self._iso639_3 is not None:
            return self._iso639_3
        else:
            self._iso639_3 = {}
            for info in ISO639_INFO:
                self._iso639_3[info.iso639_3] = info
            return self._iso639_3

Languages = Iso639Languages()

Dialects = {
    'aka': {
        'fat': 'Fanti',
        'twi': 'Twi',
    },
    'ara': {
        'aao': 'Algerian Saharan Arabic',
        'abh': 'Tajiki Arabic',
        'abv': 'Baharna Arabic',
        'acm': 'Mesopotamian Arabic',
        'acq': 'Ta\'izzi-Adeni Arabic',
        'acw': 'Hijazi Arabic',
        'acx': 'Omani Arabic',
        'acy': 'Cypriot Arabic',
        'adf': 'Dhofari Arabic',
        'aeb': 'Tunisian Arabic',
        'aec': 'Saidi Arabic',
        'afb': 'Gulf Arabic',
        'ajp': 'South Levantine Arabic',
        'apc': 'North Levantine Arabic',
        'apd': 'Sudanese Arabic',
        'arb': 'Standard Arabic',
        'arq': 'Algerian Arabic',
        'ars': 'Najdi Arabic',
        'ary': 'Moroccan Arabic',
        'arz': 'Egyptian Arabic',
        'auz': 'Uzbeki Arabic',
        'avl': 'Eastern Egyptian Bedawi Arabic',
        'ayh': 'Hadrami Arabic',
        'ayl': 'Libyan Arabic',
        'ayn': 'Sanaani Arabic',
        'ayp': 'North Mesopotamian Arabic',
        'bbz': 'Babalia Creole Arabic',
        'pga': 'Sudanese Creole Arabic',
        'sh': 'Chadian Arabic',
        'ssh': 'Shihhi Arabic',
    },
    'aym': {
        'ayr': 'Central Aymara',
        'ayc': 'Southern Aymara',
    },
    'aze': {
        'azj': 'North Azerbaijani',
        'azb': 'South Azerbaijani',
    },
    'bal': {
        'bgp': 'Eastern Balochi',
        'bcc': 'Southern Balochi',
        'bgn': 'Western Balochi',
    },
    'bik': {
        'bcl': 'Central Bicolano',
        'bto': 'Iriga Bicolano',
        'cts': 'Northern Catanduanes Bicolano',
        'bln': 'Southern Catanduanes Bicolano',
        'fbl': 'West Albay Bikol',
        'lbl': 'Libon Bikol',
        'rbl': 'Miraya Bikol',
        'ubl': 'Buhi\non Bikol',
    },
    'bnc': {
        'ebk': 'Eastern Bontok',
        'lbk': 'Central Bontok',
        'obk': 'Southern Bontok',
        'rbk': 'Northern Bontok',
        'vbk': 'Southwestern Bontok',
    },
    'bua': {
        'bx': 'China Buriat',
        'bxm': 'Mongolia Buriat',
        'bxr': 'Russia Buriat',
    },
    'chm': {
        'mhr': 'Eastern Mari',
        'mrj': 'Western Mari',
    },
    'cre': {
        'crm': 'Moose Cree',
        'crl': 'Northern East Cree',
        'crk': 'Plains Cree',
        'crj': 'Southern East Cree',
        'csw': 'Swampy Cree',
        'cwd': 'Woods Cree',
        'nsk': 'Naskapi',
        'moe': 'Montagnais',
        'atj': 'Atikamekw',
        'crg': 'Michif language',
        'ojs': 'Ojibwa, Severn',
        'ojw': 'Ojibwa, Western',
    },
    'del': {
        'um': 'Munsee',
        'unm': 'Unami',
    },
    'den': {
        'scs': 'North Slavey',
        'xsl': 'South Slavey',
    },
    'din': {
        'dip': 'Northeastern Dinka',
        'diw': 'Northwestern Dinka',
        'dib': 'South Central Dinka',
        'dks': 'Southeastern Dinka',
        'dik': 'Southwestern Dinka',
    },
    'doi': {
        'dgo': 'Dogri',
        'xnr': 'Kangri',
    },
    'est': {
        'ekk': 'Estonian (Standard Estonian)',
        'vro': 'Võro',
    },
    'fas': {
        'prs': 'Dari Persian',
        'pes': 'Western Persian',
    },
    'ful': {
        'fub': 'Adamawa Fulfulde',
        'fui': 'Bagirmi Fulfulde',
        'fue': 'Borgu Fulfulde',
        'fuq': 'Central-Eastern Niger Fulfulde',
        'ffm': 'Maasina Fulfulde',
        'fuv': 'Nigerian Fulfulde',
        'fuc': 'Pulaar',
        'fuf': 'Pular',
        'fuh': 'Western Niger Fulfulde',
    },
    'gba': {
        'bdt': 'Bokoto',
        'gbp': 'Gbaya-Bossangoa',
        'gbq': 'Gbaya-Bozoum',
        'gmm': 'Gbaya-Mbodomo',
        'gya': 'Northwest Gbaya',
        'mdo': 'Southwest Gbaya (Retired 2008-01-14)',
        'gso': 'Southwest Gbaya',
    },
    'gon': {
        'gno': 'Northern Gondi',
        'ggo': 'Southern Gondi',
    },
    'grb': {
        'gry': 'Barclayville Grebo',
        'grv': 'Central Grebo',
        'gec': 'Gboloo Grebo',
        'gbo': 'Northern Grebo',
        'grj': 'Southern Grebo',
    },
    'grn': {
        'nhd': 'Chiripá',
        'gui': 'Eastern Bolivian Guaraní',
        'gun': 'Mbyá Guaraní',
        'gug': 'Paraguayan Guaraní',
        'gnw': 'Western Bolivian Guaraní',
    },
    'hai': {
        'hdn': 'Northern Haida',
        'hax': 'Southern Haida',
    },
    'hbs': {
        'bos': 'Bosnian',
        'hrv': 'Croatian',
        'srp': 'Serbian',
    },
    'hmn': {
        'hmc': 'Central Huishui Hmong',
        'hmm': 'Central Mashan Hmong',
        'cqd': 'Chuanqiandian Cluster Miao',
        'hme': 'Eastern Huishui Hmong',
        'hmq': 'Eastern Qiandong Hmong',
        'muq': 'Eastern Xiangxi Hmong',
        'hmj': 'Ge',
        'mww': 'Hmong Daw',
        'hnj': 'Hmong Njua',
        'hrm': 'Horned Miao',
        'hmd': 'Large Flowery Miao',
        'hml': 'Luopohe Hmong',
        'huj': 'Northern Guiyang Hmong',
        'hmi': 'Northern Huishui Hmong',
        'hmp': 'Northern Mashan Hmong',
        'hea': 'Northern Qiandong Miao',
        'sfm': 'Small Flowery Miao',
        'hmy': 'Southern Guiyang Hmong',
        'hma': 'Southern Mashan Hmong',
        'hms': 'Southern Qiandong Miao',
        'hmg': 'Southwestern Guiyang Hmong',
        'hmh': 'Southwestern Huishui Hmong',
        'hmw': 'Western Mashan Hmong',
        'mmr': 'Western Xiangxi Miao',
    },
    'ik': {
        'ike': 'Eastern Canadian Inuktitut',
        'ikt': 'Western Canadian Inuktitut',
    },
    'ipk': {
        'esi': 'North Alaskan Inupiatun',
        'esk': 'Northwest Alaska Inupiatun',
    },
    'jrb': {
        'yhd': 'Judeo-Iraqi Arabic',
        'aj': 'Judeo-Moroccan Arabic',
        'yud': 'Judeo-Tripolitanian Arabic',
        'ajt': 'Judeo-Tunisian Arabic',
        'jye': 'Judeo-Yemeni Arabic',
    },
    'ka': {
        'knc': 'Central Kanuri',
        'kby': 'Manga Kanuri',
        'krt': 'Tumari Kanuri',
    },
    'kln': {
        'eyo': 'Keiyo',
        'sgc': 'Kipsigis',
        'enb': 'Markweeta',
        'niq': 'Nandi',
        'oki': 'Okiek',
        'pko': 'Pökoot',
        'spy': 'Sabaot',
        'tec': 'Terik',
        'tuy': 'Tugen',
    },
    'kok': {
        'gom': 'Goan Konkani',
        'knn': 'Maharashtrian Konkani',
    },
    'kom': {
        'koi': 'Komi-Permyak',
        'kpv': 'Komi-Zyrian',
    },
    'kon': {
        'kng': 'Koongo',
        'ldi': 'Laari',
        'kwy': 'San Salvador Kongo',
    },
    'kpe': {
        'gkp': 'Guinea Kpelle',
        'xpe': 'Liberia Kpelle',
    },
    'kur': {
        'ckb': 'Central Kurdish',
        'kmr': 'Northern Kurdish',
        'sdh': 'Southern Kurdish',
    },
    'lah': {
        'jat': 'Jakati',
        'xhe': 'Khetrani',
        'pm': 'Mirpur Panjabi',
        'hno': 'Northern Hindko',
        'phr': 'Pahari-Potwari',
        'skr': 'Saraiki',
        'hnd': 'Southern Hindko',
        'pnb': 'Western Panjabi',
    },
    'lav': {
        'ltg': 'Latgalian',
        'lvs': 'Standard Latvian',
    },
    'luy': {
        'bxk': 'Bukus',
        'nle': 'East Nyala',
        'ida': 'Idakho (Idakho-Isukha-Tiriki)',
        'lkb': 'Kabras',
        'lko': 'Khayo',
        'lks': 'Kisa',
        'rag': 'Logooli',
        'lri': 'Marachi',
        'lrm': 'Marama',
        'nyd': 'Nyore',
        'lsm': 'Saamia',
        'lts': 'Tachoni',
        'lto': 'Tsotso',
        'lwg': 'Wanga',
    },
    'man': {
        'emk': 'Eastern Maninkakan',
        'myq': 'Forest Maninka',
        'mwk': 'Kita Maninkakan',
        'mk': 'Konyanka Maninka',
        'mnk': 'Mandinka',
        'msc': 'Sankaran Maninka',
        'mlq': 'Western Maninkakan',
    },
    'mlg': {
        'xmv': 'Antankarana Malagasy',
        'bhr': 'Bara Malagasy',
        'msh': 'Masikoro Malagasy',
        'bmm': 'Northern Betsimisaraka Malagasy',
        'plt': 'Plateau Malagasy',
        'skg': 'Sakalava Malagasy',
        'bjq': 'Southern Betsimisaraka Malagasy (Retired 2011-05-18)',
        'bzc': 'Southern Betsimisaraka Malagasy',
        'tkg': 'Tesaka Malagasy',
        'tdx': 'Tandroy-Mahafaly Malagasy',
        'txy': 'Tanosy Malagasy',
        'xmw': 'Tsimihety Malagasy',
    },
    'mon': {
        'khk': 'Halh Mongolian',
        'mvf': 'Peripheral Mongolian',
    },
    'msa': {
        'btj': 'Bacanese Malay',
        'bve': 'Berau Malay',
        'bv': 'Bukit Malay',
        'coa': 'Cocos Islands Malay',
        'jax': 'Jambi Malay',
        'meo': 'Kedah Malay',
        'mqg': 'Kota Bangun Kutai Malay',
        'mly': 'Malay (specific)',
        'xmm': 'Manado Malay',
        'max': 'North Moluccan Malay',
        'mfa': 'Pattani Malay',
        'msi': 'Sabah Malay',
        'vkt': 'Tenggarong Kutai Malay',
    },
    'mwr': {
        'dhd': 'Dhundari',
        'rwr': 'Marwari (India)',
        'mve': 'Marwari (Pakistan)',
        'wry': 'Merwari',
        'mtr': 'Mewari',
        'swv': 'Shekhawati',
    },
    'nor': {
        'nob': 'Norwegian Bokmål',
        'nno': 'Norwegian Nynorsk',
    },
    'oji': {
        'ciw': 'Chippewa (Ojibwa, Southwestern)',
        'ojb': 'Ojibwa, Northwestern',
        'ojc': 'Ojibwa, Central',
        'ojg': 'Ojibwa, Mississaga (Ojibwa, Eastern)',
        'ojs': 'Ojibwa, Severn (Ojibwa, Northern)',
        'ojw': 'Ojibwa, Western',
        'otw': 'Ottawa',
    },
    'orm': {
        'gax': 'Borana-Arsi-Guji Oromo',
        'hae': 'Eastern Oromo',
        'orc': 'Orma',
        'gaz': 'West Central Oromo',
    },
    'pus': {
        'pst': 'Central Pashto',
        'pb': 'Northern Pashto',
        'pbt': 'Southern Pashto',
    },
    'que': {
        'qva': 'Ambo-Pasco Quechua',
        'qx': 'Arequipa-La Unión Quechua',
        'quy': 'Ayacucho Quechua',
        'qvc': 'Cajamarca Quechua',
        'qvl': 'Cajatambo North Lima Quechua',
        'qud': 'Calderón Highland Quichua',
        'qxr': 'Cañar Highland Quichua',
        'quk': 'Chachapoyas Quechua',
        'cq': 'Chilean Quechua',
        'qug': 'Chimborazo Highland Quichua',
        'qxc': 'Chincha Quechua',
        'qxa': 'Chiquián Ancash Quechua',
        'qwc': 'Classical Quechua',
        'qwa': 'Corongo Ancash Quechua',
        'quz': 'Cusco Quechua',
        'qve': 'Eastern Apurímac Quechua',
        'qub': 'Huallaga Huánuco Quechua',
        'qvh': 'Huamalíes-Dos de Mayo Huánuco Quechua',
        'qwh': 'Huaylas Ancash Quechua',
        'qvw': 'Huaylla Wanca Quechua',
        'qvi': 'Imbabura Highland Quichua',
        'qxw': 'Jauja Wanca Quechua',
        'quf': 'Lambayeque Quechua',
        'qvj': 'Loja Highland Quichua',
        'qvm': 'Margos-Yarowilca-Lauricocha Quechua',
        'qvo': 'Napo Lowland Quechua',
        'qul': 'North Bolivian Quechua',
        'qvn': 'North Junín Quechua',
        'qxn': 'Northern Conchucos Ancash Quechua',
        'qvz': 'Northern Pastaza Quichua',
        'qvp': 'Pacaraos Quechua',
        'qxh': 'Panao Huánuco Quechua',
        'qxp': 'Puno Quechua',
        'qxl': 'Salasaca Highland Quichua',
        'qvs': 'San Martín Quechua',
        'qxt': 'Santa Ana de Tusi Pasco Quechua',
        'qus': 'Santiago del Estero Quichua',
        'qws': 'Sihuas Ancash Quechua',
        'quh': 'South Bolivian Quechua',
        'qxo': 'Southern Conchucos Ancash Quechua',
        'qup': 'Southern Pastaza Quechua',
        'quw': 'Tena Lowland Quichua',
        'qur': 'Yanahuanca Pasco Quechua',
        'qux': 'Yauyos Quechua',
    },
    'raj': {
        'bgq': 'Bagri',
        'gda': 'Gade Lohar',
        'gj': 'Gujari',
        'hoj': 'Hadothi',
        'mup': 'Malvi',
        'wbr': 'Wagdi',
    },
    'rom': {
        'rmn': 'Balkan Romani',
        'rml': 'Baltic Romani',
        'rmc': 'Carpathian Romani',
        'rmf': 'Kalo Finnish Romani',
        'rmo': 'Sinte Romani',
        'rmy': 'Vlax Romani',
        'rmw': 'Welsh Romani',
    },
    'sqi': {
        'aae': 'Arbëreshë Albanian',
        'aat': 'Arvanitika Albanian',
        'aln': 'Gheg Albanian',
        'als': 'Tosk Albanian',
    },
    'srd': {
        'sro': 'Campidanese',
        'sdn': 'Gallurese',
        'src': 'Logudorese',
        'sdc': 'Sassarese',
    },
    'swa': {
        'swc': 'Congo Swahili',
        'swh': 'Swahili',
    },
    'syr': {
        'aii': 'Assyrian Neo-Aramaic',
        'cld': 'Chaldean Neo-Aramaic',
    },
    'tmh': {
        'thv': 'Tahaggart Tamahaq',
        'taq': 'Tamasheq',
        'ttq': 'Tawallammat Tamajaq',
        'thz': 'Tayart Tamajeq',
    },
    'uzb': {
        'uzn': 'Northern Uzbek language',
        'uzs': 'Southern Uzbek language',
    },
    'yid': {
        'ydd': 'Eastern Yiddish',
        'yih': 'Western Yiddish',
    },
    'zap': {
        'zaq': 'Aloápam Zapotec',
        'zpo': 'Amatlán Zapotec',
        'zoo': 'Asunción Mixtepec Zapotec',
        'zaf': 'Ayoquesco Zapotec',
        'zad': 'Cajonos Zapotec',
        'zpv': 'Chichicapan Zapotec',
        'zpc': 'Choapan Zapotec',
        'zca': 'Coatecas Altas Zapotec',
        'zps': 'Coatlán Zapotec',
        'zpp': 'El Alto Zapotec',
        'zte': 'Elotepec Zapotec',
        'zpg': 'Guevea De Humboldt Zapotec',
        'zt': 'Güilá Zapotec',
        'zai': 'Isthmus Zapotec',
        'zpa': 'Lachiguiri Zapotec',
        'zpl': 'Lachixío Zapotec',
        'ztl': 'Lapaguía-Guivini Zapotec',
        'ztp': 'Loxicha Zapotec',
        'zpy': 'Mazaltepec Zapotec',
        'zam': 'Miahuatlán Zapotec',
        'zaw': 'Mitla Zapotec',
        'zpm': 'Mixtepec Zapotec',
        'zac': 'Ocotlán Zapotec',
        'zao': 'Ozolotepec Zapotec',
        'zpe': 'Petapa Zapotec',
        'zpj': 'Quiavicuzas Zapotec',
        'ztq': 'Quioquitani-Quierí Zapotec',
        'zar': 'Rincón Zapotec',
        'ztm': 'San Agustín Mixtepec Zapotec',
        'zpx': 'San Baltazar Loxicha Zapotec',
        'zab': 'San Juan Guelavía Zapotec',
        'zpf': 'San Pedro Quiatoni Zapotec',
        'zpt': 'San Vicente Coatlán Zapotec',
        'ztn': 'Santa Catarina Albarradas Zapotec',
        'zpn': 'Santa Inés Yatzechi Zapotec',
        'zpi': 'Santa María Quiegolani Zapotec',
        'zpr': 'Santiago Xanica Zapotec',
        'zas': 'Santo Domingo Albarradas Zapotec',
        'zaa': 'Sierra de Juárez Zapotec',
        'zpd': 'Southeastern Ixtlán Zapotec',
        'zsr': 'Southern Rincon Zapotec',
        'zat': 'Tabaa Zapotec',
        'ztt': 'Tejalapan Zapotec',
        'zpz': 'Texmelucan Zapotec',
        'zts': 'Tilquiapan Zapotec',
        'zpk': 'Tlacolulita Zapotec',
        'zph': 'Totomachapan Zapotec',
        'zax': 'Xadani Zapotec',
        'ztg': 'Xanaguía Zapotec',
        'zp': 'Yalálag Zapotec',
        'zae': 'Yareni Zapotec',
        'zty': 'Yatee Zapotec',
        'zav': 'Yatzachi Zapotec',
        'zpb': 'Yautepec Zapotec',
        'ztx': 'Zaachila Zapotec',
        'zpw': 'Zaniza Zapotec',
        'zpq': 'Zoogocho Zapotec',
    },
    'zha': {
        'zch': 'Central Hongshuihe Zhuang',
        'zhd': 'Dai Zhuang',
        'zeh': 'Eastern Hongshuihe Zhuang',
        'zgb': 'Guibei Zhuang',
        'zgn': 'Guibian Zhuang',
        'zln': 'Lianshan Zhuang',
        'zlj': 'Liujiang Zhuang',
        'zlq': 'Liuqian Zhuang',
        'zgm': 'Minz Zhuang',
        'zhn': 'Nong Zhuang',
        'zqe': 'Qiubei Zhuang',
        'zyg': 'Yang Zhuang',
        'zyb': 'Yongbei Zhuang',
        'zyn': 'Yongnan Zhuang',
        'zyj': 'Youjiang Zhuang',
        'zzj': 'Zuojiang Zhuang',
    },
    'zho': {
        'cdo': 'Min Dong',
        'cjy': 'Jin',
        'cmn': 'Mandarin',
        'cpx': 'Puxian Min',
        'czh': 'Huizho',
        'czo': 'Min Zhong',
        'gan': 'Gan',
        'hak': 'Hakka',
        'hsn': 'Xiang',
        'mnp': 'Min Bei',
        'nan': 'Min Nan',
        'wuu': 'Wu',
        'yue': 'Yue (Cantonese)',
    },
    'zza': {
        'diq': 'Dimli',
        'ki': 'Kirmanjki',
    },
}