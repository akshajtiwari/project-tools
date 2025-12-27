import os
import sys
import shutil
import importlib.util
import platform
from config import load_config # file in folder
def get_python_version():
    python=sys.version_info.minor
    return python
def check_python_version(min_version): 
    required_version=min_version
    return required_version

def tools_exists(tools):
    for required in tools:
     
        if shutil.which(required) is None:
            print(f"{required} was not found")
        if importlib.util.find_spec(required) is None:
            print(f"{required} is not found ")
    

def get_os():
    os=platform.system()
    return os

def run(): 
    cfg=load_config()

    min=cfg["python"]["min_version"]  
    tool=cfg['tools']['required']

    sys_python_version=get_python_version()
    required=check_python_version(min_version=min)

    if required==sys_python_version:
        return 1
    else:
        print(f"project and system python version mismatch...project version : {required} system version is {sys_python_version} ")
    
    os=get_os()
    print(f"user is using the Operating system : {os}")
    
    kk=tools_exists(tools=tool)

run()
