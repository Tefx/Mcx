import os.path
import sys
import pexpect
import subprocess
import functools
import struct, fcntl, termios, signal
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from configure import configuration
from namechecker import check_name
del sys.path[-1]

class Host(object):
    def __init__(self, name, conf):
        self.name = name
        for k, v in conf.iteritems():
            self.__setattr__(k, v)

    def match(self, pattern):
        return check_name(self.name, pattern)

    @staticmethod
    def all_hosts(pattern=None):
        hs = [Host(k,v) for k,v in configuration.hosts.iteritems()]
        if pattern:
            return [h for h in hs if h.match(pattern)]
        else:
            return hs

    @staticmethod
    def get_by_name(name):
        return Host(name, configuration.hosts[name])

    def ssh(self):
        child = pexpect.spawn('ssh %s@%s' % (self.username,self.ip))
        if self.auth_type == "password":
            self.ssh_password(child)
        elif self.auth_type == "key":
            self.ssh_key(child)
        interact_resizable(child)

    def ssh_password(self, child):
        i = child.expect(["Are you sure you want to continue connecting", "password:"])
        if i == 0:
            child.sendline("yes")
            self.ssh_password(child)
        elif i == 1:
            child.sendline(self.password)

    def ssh_key(self, child):
        i = child.expect(["Are you sure you want to continue connecting",
                          "Enter passphrase for key",
                          "\$|\#"])
        if i == 0:
            child.sendline("yes")
            self.ssh_key(child)
        elif i == 1:
            child.sendline(self.passphrase)
            self.ssh_key(child)
        elif i == 2:
            child.sendline("clear;echo 'Connected to %s. Welcome.'" % self.name)


    def ftp(self):
        url = "ftp://%s:%s@%s" % (self.username, self.password, self.ip)
        subprocess.call([configuration.ftp_tool, url])

    def telnet(self):
        child = pexpect.spawn('telnet %s' % self.ip)
        child.expect("login: ")
        child.sendline(self.username)
        child.expect("Password: ")
        child.sendline(self.password)
        interact_resizable(child)

    def connect(self):
        self.__getattribute__(self.conn_type)()

def getwinsize():
    s = struct.pack("HHHH", 0, 0, 0, 0)
    a = struct.unpack('hhhh', fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ , s))
    return a[:2]

def sigwinch_passthrough(child, sig, data):
    a = getwinsize()
    child.setwinsize(a[0],a[1])

def interact_resizable(child):
    signal.signal(signal.SIGWINCH, functools.partial(sigwinch_passthrough, child))
    a = getwinsize()
    child.setwinsize(a[0], a[1])
    child.interact()

if __name__ == '__main__':
    Host.all_hosts()[0].connect()