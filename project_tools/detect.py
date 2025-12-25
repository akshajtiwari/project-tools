import os
import sys
import shutil
import platform
from config import load_config
def get_python_version():
    python=sys.version
    return python
def check_python_version(min_version): 
    required_version=min_version
    return required_version
#def tools_exists(tools):

def get_os():
    os=platform.system()
    return os

def run(): 
    cfg=load_config()

    min=cfg["python"]["min_version"]  
    sys_python_version=get_python_version()
    required=check_python_version(min_version=min)
    if required==sys_python_version:
        return 1
    else:
        print(f"project and system python version mismatch...project version : {required} system version is {sys_python_version} ")
    os=get_os()
    print(f"user is using the Operating system : {os}")

run()