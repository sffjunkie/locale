class CaseInsensitiveDict(dict):
    __transform__ = str.upper
    
    def __init__(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[CaseInsensitiveDict.__transform__(k)] = v

    def __contains__(self, key):
        return dict.__contains__(self, CaseInsensitiveDict.__transform__(key))

    def __getitem__(self, key):
        val = dict.__getitem__(self, CaseInsensitiveDict.__transform__(key))
        return val

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)
