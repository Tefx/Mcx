import sys
import subprocess

name = raw_input().strip()
subprocess.check_output(["tmux", "new-window", "-n", name, ("echo 'conncetiong to %s and do sth.';read" % name)])
