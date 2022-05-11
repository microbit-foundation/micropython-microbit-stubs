import os

def test_uname():
    sysname: str = os.uname().sysname
    nodename: str = os.uname().nodename
    release: str = os.uname().release
    version: str = os.uname().version
    machine: str = os.uname().machine
    (sysname, nodename, release, version, machine) = os.uname()

test_uname()
