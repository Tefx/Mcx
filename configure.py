#!coding=utf-8
import os
import toml
import copy

CONF_LOCATIONS = ["/etc/mcx", "~/.mcx"]
CONF_FILE = "config.toml"
HOSTS_DIRS = "hosts.d"

class Configuration(object):
    def __init__(self):
        for item in CONF_LOCATIONS:
            conf_path = os.path.expanduser(os.path.join(item, CONF_FILE))
            if os.path.exists(conf_path):
                with open(conf_path) as f:
                    for k,v in toml.load(f).iteritems():
                        self.__setattr__(k, v)
        self.hosts = {}
        self.get_hosts()

    def get_hosts(self):
        for item in CONF_LOCATIONS:
            d = os.path.expanduser(os.path.join(item, HOSTS_DIRS))
            if os.path.exists(d):
                self.hosts.update(read_hosts_from_dir(d))


# CONN has the form:
# {"name" : "beijing/server1",
#  "conn_type" : "ssh",
#  "auth_type" : "password",
#  "username"  : "tefx"
#  "password"  : "123456"}
def read_hosts_from_dir(dir):
    conns = {}
    for (base, _, files) in os.walk(dir):
        for path in files:
            with open(os.path.join(base, path)) as f:
                d = toml.load(f)
            default_conf = d["Default"]
            for key, conf in d.iteritems():
                if key != "Default":
                    host = copy.copy(default_conf)
                    host.update(conf)
                    conns.update({key.decode("utf-8"):host})
    return conns

configuration = Configuration()

if __name__ == '__main__':
    print configuration.ftp_tool
