from tmux.selection import list_selection
from tmux.helper import tmux_cmd
from hosts import Host

def search_hosts(pattern):
    return [h.name for h in Host.all_hosts(pattern)]

def connect(name):
    tmux_cmd("new-window -n %s" % name,
             "python %s --conn '%s'" % (__file__, name))

if __name__ == '__main__':
    import sys
    if sys.argv[1] == "--conn":
        Host.get_by_name(sys.argv[2].decode("utf-8")).connect()
    else:
        list_selection(__file__, sys.argv, search_hosts, connect)