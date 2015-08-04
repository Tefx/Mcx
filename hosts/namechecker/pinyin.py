import pypinyin


def checker_initials(name, pattern):
    initials = pypinyin.pinyin(name, style=pypinyin.INITIALS)
    return pattern.lower() in u"".join(x[0] for x in initials).lower()


def checker_first_letters(name, pattern):
    initials = pypinyin.pinyin(name, style=pypinyin.FIRST_LETTER)
    return pattern.lower() in u"".join(x[0] for x in initials).lower()


def checker_full(name, pattern):
    initials = pypinyin.pinyin(name, style=pypinyin.NORMAL)
    return pattern.lower() in u"".join(x[0] for x in initials).lower()


_checkers_ = [
    checker_first_letters,
    checker_initials,
    # checker_full,
]

checker = lambda n, p: any(c(n, p) for c in _checkers_)
