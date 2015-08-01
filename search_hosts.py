#!/usr/bin/env python
# coding=utf-8

from parse_conf import read_hosts
from finder import find_names
import os

if __name__ == '__main__':
    from sys import argv

    hosts = read_hosts()
    try:
        for name in find_names(hosts, argv[1]):
            print name.encode("utf-8")
    except Exception, e:
        print e
