import os

from checker import all_checkers


def find_names(host_dict, pattern):
    for name in host_dict.iterkeys():
        tags = name.split("/")
        subpattern = pattern.split("/")
        if len(subpattern) > len(tags):
            continue
        passed = True
        for t, s in zip(tags, subpattern):
            if not any(c(t, s) for c in all_checkers):
                passed = False
                break
        if passed:
            yield name
