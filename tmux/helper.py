#!coding=utf-8

import subprocess
import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from configure import configuration
del sys.path[-1]

def tmux_cmd(s, other=None):
    cmds = ["tmux"] + s.strip().split()
    if other:
        cmds.append(other)
    with open("tmp", "a") as f:
        print >>f, cmds
    subprocess.check_output(cmds)

def tmux_send_keys(keys):
    for k in keys.strip().split():
        subprocess.check_output(["tmux", "send-keys", k])

def exec_py(path):
    ins_path = configuration.install_path
    return "python %s" % (os.path.join(ins_path, path))