import os.path
import sys
import pexpect
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

    def __repr__(self):
        return self.name.encode("utf-8")

    def ssh(self):
        if self.conn_type != "ssh":
            return
        child = pexpect.spawn('ssh %s@%s' % (self.username,self.ip))
        i = child.expect(["Are you sure you want to continue connecting", "password:"])
        if i == 0:
            child.sendline("yes")
            child.expect("password:")
        child.sendline (self.password)
        child.interact()

    def ftp(self):
        pass

    def telnet(self):
        pass

if __name__ == '__main__':
    print Host.all_hosts("zj")[0].ssh()