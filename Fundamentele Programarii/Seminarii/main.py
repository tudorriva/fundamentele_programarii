def swap(word):
    """Terminator -> Tormaniter"""
    vok = 'aeiou'
    voks = []
    for ch in word:
        if ch in vok:
            voks.append(ch)
    s = ''
    idx = 1
    for ch in word:
        if ch not in vok:
            s = s + ch
        else:
            s = s + voks[-idx]
            idx = idx + 1

    return s

def test_swap():
    assert swap('terminator') == 'tormantier'

def main(): pass


test_swap()
main()
