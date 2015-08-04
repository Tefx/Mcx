#!/usr/bin/env python

from tmux.selection import list_selection
from tmux.helper import tmux_cmd
from hosts import Host

def current_host():
    for l in tmux_cmd("list-windows -F",
                      "#{window_name} #{window_active}").splitlines():
        name, active = l.strip().split()
        if active == "1":
            return Host.get_by_name(name.decode("utf-8"))

def new_conn(name):
    Host.get_by_name(name.decode("utf-8")).connect()

def search_and_list(*argv):
    search_hosts = lambda pattern:[h.name for h in Host.all_hosts(pattern)]
    connect = lambda name:tmux_cmd("new-window -n %s" % name, "%s new_conn '%s'" % (__file__, name))
    prefix_cmd = "%s %s" % (__file__, "search_and_list")
    list_selection(prefix_cmd, argv, search_hosts, connect)

def clone_conn():
    current_host().connect()

def extern_ftp():
    current_host().ftp()

if __name__ == '__main__':
    import sys
    op_name = sys.argv[1]
    argv = sys.argv[2:]
    func = globals()[op_name]
    func(*argv)