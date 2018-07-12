import gettext

def get_translator(domain, localedir=None):
    try:
        t = gettext.translation(domain, localedir=localedir)
        try:
            return t.ugettext
        except AttributeError:
            return t.gettext
    except:
        def __tx(text):
            return text

        return __tx
