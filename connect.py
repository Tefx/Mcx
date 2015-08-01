import subprocess

subprocess.check_output(["tmux", "send-keys", "C-Space"])
subprocess.check_output(["tmux", "send-keys", "C-e"])
subprocess.check_output(["tmux", "send-keys", "Escape"])
subprocess.check_output(["tmux", "send-keys", "Enter"])