from tmux.helper import tmux_cmd
from hosts import Host


def get_cur_conn():
    for l in tmux_cmd("list-windows -F",
                      "#{window_name} #{window_active}").splitlines():
        name, active = l.strip().split()
        if active == "1":
            return name


if __name__ == '__main__':
    import sys
    name = get_cur_conn()
    Host.get_by_name(name.decode("utf-8")).connect()
