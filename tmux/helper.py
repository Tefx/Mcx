#!coding=utf-8

import subprocess

def tmux_cmd(s, other=None):
    cmds = ["tmux"] + s.strip().split()
    if other:
        cmds.append(other)
    return subprocess.check_output(cmds)

def tmux_send_keys(keys):
    for k in keys.strip().split():
        subprocess.check_output(["tmux", "send-keys", k])