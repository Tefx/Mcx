import pinyin

simple_checker = lambda name, pattern: pattern.lower() in name.lower()
wildcard = lambda _, pattern: pattern == "*"

all_checkers = [simple_checker, wildcard, pinyin.checker]

def check_name(name, pattern):
    tags = name.split("/")
    subpattern = pattern.split("/")
    if len(subpattern) > len(tags):
        return False
    for t, s in zip(tags, subpattern):
        if not any(c(t, s) for c in all_checkers):
            return False
    return True