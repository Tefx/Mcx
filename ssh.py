from tmux.selection import list_selection
from tmux.helper import tmux_cmd, exec_py
from hosts import Host
import time

def search_hosts(pattern):
    return [h.name for h in Host.all_hosts(pattern)]

def connect_ssh(name):
    tmux_cmd("new-window -n %s" % name,
             "python %s --ssh '%s'" % (__file__, name))

if __name__ == '__main__':
    import sys
    if sys.argv[1] == "--ssh":
        Host.get_by_name(sys.argv[2].decode("utf-8")).ssh()
    else:
        list_selection(__file__, sys.argv, search_hosts, connect_ssh)