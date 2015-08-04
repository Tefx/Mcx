#!/usr/bin/env bash

INSTALL_PATH=`pwd`
OPS=${INSTALL_PATH}/operations.py

tmux setw -g automatic-rename off
tmux setw -g allow-rename off

tmux bind-key S command-prompt -p "[SearchHost]:" "run-shell -b '$OPS search_and_list \"%1\">/dev/null'"
tmux bind-key v split-window -v "$OPS clone_conn"
tmux bind-key V split-window -h "$OPS clone_conn"
tmux bind-key F run-shell -b "$OPS extern_ftp > /dev/null"
tmux bind-key C run-shell -b "$OPS switch_conns > /dev/null"

tmux rename-window LOCAL
