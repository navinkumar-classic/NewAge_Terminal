from data_structures import HashMap
import os

hash_database = HashMap(50)
alias_arr = []
alias_hash = HashMap(50)

def hello(command):
    return "hi"

def cd(command):
    folder = command[3:]
    try:
        os.chdir(os.getcwd() + "\\" + folder)
    except:
        return "File does not exist"
    else:
        return "Operation success"
    
def mcd(command):
    folder_list = list(command.split())[1:]
    try:
        for folder in folder_list:
            os.chdir(os.getcwd() + "\\" + folder)
    except:
        return "File does not exist"
    else:
        return "Operation success"

def alias(command):
    sub_cmd = list(command.split())
    if len(sub_cmd) == 1:
        string = "Alias List\n"
        for i in alias_arr:
            act_cmd,bool = alias_hash.get(i)
            string = string + "\nalias " + i + " - " + act_cmd

        return string
    
    else:
        try:
            alias_arr.append(sub_cmd[1])
            alias_hash.set(sub_cmd[1],' '.join(sub_cmd[2:]))
        except:
            return "Inappropriate Arguments"
        else:
            return "Alias set"
       
def main():
    hash_set = [["hello",hello],["cd",cd],["mcd",mcd],["alias",alias]]
    for hash  in hash_set:
        hash_database.set(hash[0],hash[1])

main()
