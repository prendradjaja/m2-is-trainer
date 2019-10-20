def minus(a, b):
    """
    >>> minus('ABCD', 'B')
    'ACD'
    >>> minus('ABCD', 'BC')
    'AD'
    >>> minus('ABCDEF', 'CD EF')
    'AB'
    """
    return ''.join(sorted(set(a) - set(b)))
