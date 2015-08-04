#!/usr/bin/env bash

INSTALL_PATH=`pwd`

tmux bind-key S command-prompt -p "[SearchHost]:" "run-shell -b '${INSTALL_PATH}/operations.py search_and_list \"%1\">/dev/null'"
tmux bind-key v split-window -v "${INSTALL_PATH}/operations.py clone_conn"
tmux bind-key V split-window -h "${INSTALL_PATH}/operations.py clone_conn"
tmux bind-key F run-shell -b "${INSTALL_PATH}/operations.py extern_ftp > /dev/null"

tmux rename-window LOCAL