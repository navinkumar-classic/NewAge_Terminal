import subprocess
import re
from Hash import *

def get_fcmd(command):
    l = list(command.split())
    if len(l) > 0: return l[0]
    else: return ""

def find_alias(command):
    for i in alias_arr:
        bool_x = re.search(i, command)
        if bool_x:
            command = command.replace(i,alias_hash.get(i)[0])
            break
    
    return command
    
# Run the command and capture the output
def run_cmd(command):
    
    command = find_alias(command)
    func,bool_2 = hash_database.get(get_fcmd(command))
    
    if bool_2: 
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

def get_shrt_dir(dir):
    dir_list = dir.split('\\')
    #return dir_list[0] + "\\...\\" + dir_list[-1]
    return dir_list[-1]
    
