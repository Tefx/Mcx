import json
import os
import os.path

# CONN has the form:
# {"name" : "beijing/server1",
#  "conn_type" : "ssh",
#  "auth_type" : "password",
#  "username"  : "tefx"
#  "password"  : "123456"}
def read_hosts_from_dir(dir):
    conns = {}
    for (base, dirs, files) in os.walk(dir):
        for path in files:
            with open(os.path.join(base, path)) as f:
                conns.update(json.load(f))
    return conns


def read_hosts():
    conns = {}
    for item in CONF_DIRS:
        dir = os.path.join(item, CONN_DIR)
        if os.path.exists(dir):
            conns.update(read_hosts_from_dir(dir))
    return conns


if __name__ == '__main__':
    print read_hosts();
