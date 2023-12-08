import subprocess
import os
bash_command = "pwd"

# Run the Bash command
process = subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the process to finish and get the output and errors
output, errors = process.communicate()

# Print the output and errors
print("Output:", output.decode('utf-8'))
print("Errors:", errors.decode('utf-8'))

# Get the return code of the process
return_code = process.returncode
print("Return Code:", return_code)

# run this command without expecting any output
print(os.system(bash_command))