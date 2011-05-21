
_safe = (
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    'abcdefghijklmnopqrstuvwxyz'
    '0123456789' 
    '_.-'
)

_mapping = {}

for i, c in zip(xrange(256), str(bytearray(xrange(256)))):
    _mapping[c] = '%{:02X}'.format(i)


def encode(s, safe=""):
    full_safe = _safe + safe
    mapping = _mapping.copy()
    mapping.update(dict([(x, x) for x in full_safe]))
    
    return "".join([mapping[c] for c in s])
