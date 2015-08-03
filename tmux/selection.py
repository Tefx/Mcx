#!coding=utf-8
import os.path

from helper import *
import time

def show_list(self_loc, arg):
    tmux_cmd("split-window -h -l 30",
             exec_py(self_loc % ("-l %s" % arg)))
    time.sleep(0.2)
    tmux_cmd("copy-mode")
    set_bindings(self_loc)
    tmux_send_keys("M-R C-a C-Space C-e")

def jump_prev():
    tmux_send_keys("C-g Up C-a C-Space C-e")

def jump_next():
    tmux_send_keys("C-g Down C-a C-Space C-e")

def get_res(func, argv):
    for res in func(*argv):
        print res.encode("utf-8")

def do_selected(func):
    selection = raw_input()
    unset_bindings()
    tmux_send_keys("Enter")
    func(selection)

def set_bindings(self_loc):
    tmux_cmd("bind-key -n Up run-shell -b",
             exec_py(self_loc % "-k Up"))
    tmux_cmd("bind-key -n Down run-shell -b",
             exec_py(self_loc % "-k Down"))
    tmux_cmd("bind-key -t emacs-copy Enter copy-pipe",
             exec_py(self_loc % "-c"))

def unset_bindings():
    tmux_cmd("unbind-key -n Up")
    tmux_cmd("unbind-key -n Down")
    tmux_cmd("unbind-key -t emacs-copy Enter")

def list_selection(loc, argv, list_func, callback):
    loc += " %s"
    if sys.argv[1] == "-l":
        get_res(list_func, argv[2:])
        raw_input()
    elif argv[1] == "-c":
        do_selected(callback)
    elif argv[1] == "-k":
        if argv[2] == "Up":
            jump_prev()
        elif argv[2] == "Down":
            jump_next()
    else:
        show_list(loc, argv[1])

if __name__ == '__main__':
    import sys
    example_list = lambda _: ["aaaaa", "bbbbbb", "ccccccc"]
    example_do = lambda arg: tmux_cmd("new-window -n %s" % arg)
    list_selection(__file__, sys.argv, example_list, example_do)



