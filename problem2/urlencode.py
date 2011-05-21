
_safe = (
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    'abcdefghijklmnopqrstuvwxyz'
    '0123456789' 
    '_.-'
)

_mapping = {}

for i, c in zip(xrange(256), str(bytearray(xrange(256)))):
    _mapping[c] = '%{:02X}'.format(i)

_reverse_mapping = dict((y[1:], x) for x, y in _mapping.items())

def encode(s, safe=""):
    full_safe = _safe + safe
    mapping = _mapping.copy()
    mapping.update(dict([(x, x) for x in full_safe]))
    
    return "".join([mapping[c] for c in s])

def decode(s):
    tokens = s.split("%")
    s = tokens[0]
    if len(tokens)>1:
        for token in tokens[1:]:
            try:
                s = s + _reverse_mapping[token[:2]] + token[2:]
            except KeyError:
                s = s + "%" + token
    return s
        