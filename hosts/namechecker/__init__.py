import pinyin

simple_checker = lambda name, pattern: pattern.lower() in name.lower()

all_checkers = [simple_checker, pinyin.checker]

def check_name(name, pattern):
    tags = name.split("/")
    subpattern = pattern.split("/")
    return match(tags, subpattern)

def any_match(t, p):
    return any(c(t, p) for c in all_checkers)

def match(tags, pats):
    if len(pats) > len(tags):
        return False
    if not pats:
        return True
    if any_match(tags[0], pats[0]):
        return match(tags[1:], pats[1:])
    else:
        return match(tags[1:], pats)