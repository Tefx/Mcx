import pinyin

simple_checker = lambda name, pattern: pattern.lower() in name.lower()
wildcard = lambda _, pattern: pattern == "*"

all_checkers = [simple_checker, wildcard, pinyin.checker]
