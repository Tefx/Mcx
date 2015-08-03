#!coding=utf-8

import subprocess
import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import configure
del sys.path[-1]

conf = configure.Configuration()

def tmux_cmd(s, other=None):
    cmds = ["tmux"] + s.strip().split()
    if other:
        cmds.append(other)
    subprocess.check_output(cmds)

def tmux_send_keys(keys):
    for k in keys.strip().split():
        subprocess.check_output(["tmux", "send-keys", k])

def exec_py(path):
    ins_path = conf.install_path
    return "python %s" % (os.path.join(ins_path, path))