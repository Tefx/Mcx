#!/usr/bin/env python
import os.path

from tmux.selection import list_selection
from tmux.helper import tmux_cmd, tmux_send_keys
from hosts import Host

search_hosts = lambda *argv:[h.name for h in Host.all_hosts(*argv)]
create_conn = lambda name:tmux_cmd("new-window -n %s" % name, "%s new_conn '%s'" % (__file__, name))
list_conns = lambda:[l.decode("utf-8") for l in tmux_cmd("list-windows -F", "#I:#W").splitlines()]
select_conn = lambda name:tmux_cmd("select-window -t %s", name.split(":")[0])

def current_host():
    for l in tmux_cmd("list-windows -F",
                      "#{window_name} #{window_active}").splitlines():
        name, active = l.strip().split()
        if active == "1":
            return Host.get_by_name(name.decode("utf-8"))

def new_conn(name):
    Host.get_by_name(name.decode("utf-8")).connect()

def search_and_list(*argv):
    prefix_cmd = "%s %s" % (__file__, "search_and_list")
    list_selection(prefix_cmd, argv, search_hosts, {"Enter":create_conn})

def clone_conn():
    current_host().connect()

def extern_ftp():
    current_host().ftp()

def kill_conn(name):
    tmux_cmd("kill-window -t", name.split(":")[0])
    switch_conns()

def paste_to_local():
    uid = current_host().uid
    tmux_cmd("send-keys -t LOCAL -l", " "+uid)
    tmux_cmd("select-window -t LOCAL")
    tmux_send_keys("C-a")

def switch_conns(*argv):
    prefix_cmd = "%s %s" % (__file__, "switch_conns")
    list_selection(prefix_cmd, argv, list_conns, {"Enter":select_conn,
                                                  "d":kill_conn})

if __name__ == '__main__':
    import sys
    op_name = sys.argv[1]
    argv = sys.argv[2:]
    func = globals()[op_name]
    func(*argv)