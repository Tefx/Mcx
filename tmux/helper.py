#!coding=utf-8

import subprocess
import os
import uuid
import time


def tmux_cmd(s, other=None):
    cmds = ["tmux"] + s.strip().split()
    if other:
        cmds.append(other)
    return subprocess.check_output(cmds)

def tmux_send_keys(keys):
    for k in keys.strip().split():
        subprocess.check_output(["tmux", "send-keys", k])

def get_result(uid, cmd):
    buf = []
    while (uid not in buf):
        time.sleep(0.1)
        buf = tmux_cmd("capture-pane -p").strip().splitlines()
    i = len(buf)
    j = len(buf)-1
    while (i>0 and (cmd not in buf[i-1])): i-= 1
    while (j>=0 and buf[j] != uid): j-= 1
    return os.linesep.join(buf[i:j])

def tmux_run(line, win=None):
    uid = str(uuid.uuid1())
    cmd = ("send-keys -t %s -l" % win) if win else "send-keys -l"
    run_cmd = '%s;echo "%s"' % (line, uid)
    tmux_cmd(cmd, run_cmd)
    tmux_send_keys("Enter")
    return get_result(uid, run_cmd)

if __name__ == '__main__':
    print tmux_run("pwd")