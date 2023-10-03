import subprocess

# Your shell command
command = "echo 'navin'"
# Run the command and capture the output
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful (return code 0)
if result.returncode == 0:
    # Access the standard output of the command
    output = result.stdout
    print("Command output:\n", output)
else:
    # Access the standard error if the command failed
    error = result.stderr
    print("Command failed with error:\n", error)
