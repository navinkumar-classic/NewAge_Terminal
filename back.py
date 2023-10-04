import subprocess
import re
from Hash import *

def get_fcmd(command):
    l = list(command.split())
    return l[0]
# Run the command and capture the output
def run_cmd(command):

    func,bool = hash_database.get(get_fcmd(command))
    
    if bool: 
        return func(command)
    else:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Check if the command was successful (return code 0)
        if result.returncode == 0:
            output = result.stdout
            return output
        else:
            error = result.stderr
            return error
    
def clean_cmd(command):
    x = re.findall("\$.+", command)
    return x[0][1:].strip()
