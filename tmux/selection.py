#!coding=utf-8
from helper import tmux_cmd, tmux_send_keys

def start_list_selection(prefix_cmd, argv):
    tmux_cmd("split-window -h -l 30", prefix_cmd % ("-s %s" % " ".join(argv)))

def jump_prev():
    tmux_send_keys("C-g Up C-a C-Space C-e")

def jump_next():
    tmux_send_keys("C-g Down C-a C-Space C-e")

def list_show(res):
    for res in sorted(res):
        print res.encode("utf-8")

def with_selection(func, keys):
    tmux_send_keys("Enter")
    selection = raw_input()
    unset_bindings(keys)
    func(selection)

def set_bindings(prefix_cmd, keys):
    tmux_cmd("bind-key -n Up run-shell -b", prefix_cmd % "-k Up")
    tmux_cmd("bind-key -n Down run-shell -b", prefix_cmd % "-k Down")
    tmux_cmd("bind-key -t emacs-copy Escape copy-pipe", prefix_cmd % "-k Escape")
    for k in keys:
        tmux_cmd("bind-key -t emacs-copy %s copy-pipe" % k, prefix_cmd % ("-c %s" % k))

def unset_bindings(keys):
    tmux_cmd("unbind-key -n Up")
    tmux_cmd("unbind-key -n Down")
    tmux_cmd("unbind-key -t emacs-copy Escape")
    for k in keys:
        tmux_cmd("unbind-key -t emacs-copy %s" % k)

def list_selection(prefix, argv, list_func, callback):
    prefix_cmd = prefix + " %s"
    if argv:
        if argv[0] == "-s":
            res = list_func(*argv[1:])
            list_show(res)
            tmux_cmd("copy-mode")
            set_bindings(prefix_cmd, callback.keys())
            tmux_send_keys("M-R C-a C-Space C-e")
            raw_input()
        elif argv[0] == "-c":
            with_selection(callback[argv[1]], callback.keys())
        elif argv[0] == "-k":
            if argv[1] == "Up":
                jump_prev()
            elif argv[1] == "Down":
                jump_next()
            elif argv[1] == "Escape":
                tmux_send_keys("Enter")
        else:
            start_list_selection(prefix_cmd, argv)
    else:
        start_list_selection(prefix_cmd, argv)



