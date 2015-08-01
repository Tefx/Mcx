import sh
import subprocess

class Window(object):
    def __init__(self, name):
        self.name = name

class Session(object):
    def __init__(self, name):
        self.name = name

    def list_window(self):
        ws = sh.tmux("list-windows", t=self.name, F="#{window_name}")
        return [l.strip() for l in ws]

    def new_window(self, name, cmd='/usr/bin/htop'):
        ws = self.list_window()
        if name not in ws:
            subprocess.check_output(["tmux", "new-window", "-n", name, cmd])
        return Window(name)

    def delete_window(self, w):
        if w.name in self.list_window():
            sh.tmux.killw(t=w.name)
        del w

if __name__ == '__main__':
    s = Session("MCM")
    print s.list_window()
    w = s.new_window("local")
    print s.list_window()
