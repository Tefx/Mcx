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
                conns.update(read_host(f))
    return conns

def read_host(f):
    fields = f.readline().strip().split(",")
    prefix = None
    hosts = {}
    defaults = {}
    for line in f:
        line = line.strip()
        if not line:continue
        if line[0] == "[" and line[-1] == "]":
            prefix = line[1:-1]
        elif line[0] == "#":
            k, v = [x.strip() for x in line[1:].split("=")]
            defaults[k] = eval(v)
        else:
            name,values = [x.strip() for x in line.split(":")]
            if prefix:
                name = "%s/%s" % (prefix.decode("utf-8"), name.decode("utf-8"))
            else:
                name = name.decode("utf-8")
            values = [x.strip() for x in values.split(",")]
            hosts[name] = copy.deepcopy(defaults)
            hosts[name].update({k:v for (k,v) in zip(fields, values)})
    return hosts

configuration = Configuration()

if __name__ == '__main__':
    print configuration.hosts
