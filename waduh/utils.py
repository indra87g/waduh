import subprocess
from datetime import datetime


def greet(name: str):
    return f"Hello, {name}!"


def get_time(type: str):
    now = datetime.now()
    if type == "second":
        return now.second
    elif type == "minute":
        return now.minute
    elif type == "hour":
        return now.hour


def check_package(package_name: str):
    try:
        subprocess.check_call(["pip", "show", package_name])
        print(f"{package_name} is installed.")
    except subprocess.CalledProcessError:
        print(f"{package_name} is not installed.")
