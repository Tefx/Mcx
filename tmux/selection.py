#!coding=utf-8
import os.path

from helper import tmux_cmd, tmux_send_keys
import time

def start_list_selection(prefix_cmd, arg):
    tmux_cmd("split-window -h -l 30", prefix_cmd % ("-s %s" % arg))
    time.sleep(0.2)
    tmux_cmd("copy-mode")
    set_bindings(prefix_cmd)
    tmux_send_keys("M-R C-a C-Space C-e")

def jump_prev():
    tmux_send_keys("C-g Up C-a C-Space C-e")

def jump_next():
    tmux_send_keys("C-g Down C-a C-Space C-e")

def list_show(res):
    for res in res:
        print res.encode("utf-8")

def with_selection(func):
    tmux_send_keys("Enter")
    selection = raw_input()
    unset_bindings()
    func(selection)

def set_bindings(prefix_cmd):
    tmux_cmd("bind-key -n Up run-shell -b", prefix_cmd % "-k Up")
    tmux_cmd("bind-key -n Down run-shell -b", prefix_cmd % "-k Down")
    tmux_cmd("bind-key -t emacs-copy Escape copy-pipe", prefix_cmd % "-k Escape")
    tmux_cmd("bind-key -t emacs-copy Enter copy-pipe", prefix_cmd % "-c")

def unset_bindings():
    tmux_cmd("unbind-key -n Up")
    tmux_cmd("unbind-key -n Down")
    tmux_cmd("unbind-key -t emacs-copy Escape")
    tmux_cmd("unbind-key -t emacs-copy Enter")

def list_selection(prefix, argv, list_func, callback):
    prefix_cmd = prefix + " %s"
    if argv[0] == "-s":
        res = list_func(*argv[1:])
        list_show(res)
        raw_input()
    elif argv[0] == "-c":
        with_selection(callback)
    elif argv[0] == "-k":
        if argv[1] == "Up":
            jump_prev()
        elif argv[1] == "Down":
            jump_next()
        elif argv[1] == "Escape":
            tmux_send_keys("Enter")
    else:
        start_list_selection(prefix_cmd, argv[0])

if __name__ == '__main__':
    import sys
    example_list = lambda _: ["aaaaa", "bbbbbb", "ccccccc"]
    example_do = lambda arg: tmux_cmd("new-window -n %s" % arg)
    list_selection(__file__, sys.argv[1:], example_list, example_do)



