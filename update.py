import subprocess

print(50*"=", "pytesting")
subprocess.run(["pytest"]).check_returncode()

# print(50*"=", "autopep8ing client")
# subprocess.run(["py", "-m", "autopep8", "--in-place", "client.py"])

# print(50*"=", "pylinting client")
# subprocess.run(["pylint", "client.py"]).check_returncode()

print(50*"=", "autopep8ing main")
subprocess.run(["py", "-m", "autopep8", "--in-place", "main.py"])

print(50*"=", "pylinting main")
subprocess.run(["pylint", "main.py"]).check_returncode()

print(50*"=", "autopep8ing cmds")
subprocess.run(["py", "-m", "autopep8", "--recursive", "--in-place", "cmds"])

print(50*"=", "pylinting cmds")
subprocess.run(["pylint", "cmds"]).check_returncode()

print(50*"=", "autopep8ing tests")
subprocess.run(["py", "-m", "autopep8", "--recursive", "--in-place", "tests"])

print(50*"=", "pylinting tests")
subprocess.run(["pylint", "tests"]).check_returncode()