def rev(s):
    """Reverse word-order in string, preserving spaces."""

    words = s.split(' ')

    words = words[::-1]

    return ' '.join(words)
