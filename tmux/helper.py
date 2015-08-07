#!coding=utf-8

import subprocess
import os
import uuid

def tmux_cmd(s, other=None):
    cmds = ["tmux"] + s.strip().split()
    if other:
        cmds.append(other)
    return subprocess.check_output(cmds)

def tmux_send_keys(keys):
    for k in keys.strip().split():
        subprocess.check_output(["tmux", "send-keys", k])

def tmux_run(line, win=None):
    flag = str(uuid.uuid1())
    cmd = ("send-keys -t %s -l" % win) if win else "send-keys -l"
    tmux_cmd(cmd, "echo %s;%s" % (flag, line))
    tmux_send_keys("Enter")
    after_buffer = tmux_cmd("capture-pane -p")
    return diff_buffer(flag, after_buffer)

def diff_buffer(flag, after):
    after = after.splitlines()[:-1]
    i = len(after)
    while after[i-1] != flag: i -= 1
    return os.linesep.join(after[i:-1]).strip()

if __name__ == '__main__':
    print tmux_run("pwd")