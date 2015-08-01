import subprocess
import sys
import time

subprocess.check_output(["tmux", "split-window", "-h", "-l", "50", ("python ~/MultiConnManager/search_hosts.py %s ;read" % sys.argv[1])])
time.sleep(0.5)
subprocess.check_output(["tmux", "copy-mode"])
subprocess.check_output(["tmux", "send-keys", "M-R"])
subprocess.check_output(["tmux", "send-keys", "C-a"])