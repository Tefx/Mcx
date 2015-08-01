#!coding:utf-8

from parse_conf import read_hosts
from finder import find_names

if __name__ == '__main__':
    hosts = read_hosts()
    for name in find_names(hosts, u"*/n/@xx"):
        print name
