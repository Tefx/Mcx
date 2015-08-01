import subprocess

subprocess.check_output(["tmux", "send-keys", "C-a"])
subprocess.check_output(["tmux", "send-keys", "C-Space"])
subprocess.check_output(["tmux", "send-keys", "C-q"])