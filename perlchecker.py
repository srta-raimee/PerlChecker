__author__ = 'Larissa Raimee Gomes'
__date__ = '2024-05'
__copyright__ = 'Copyright (c) Larissa Raimee 2024 All Rights Reserved.'

import os
import subprocess
import platform

def perl_checker(file, output_file):
    # Run a syntax check on the specified Perl file
    result = subprocess.Popen(["perl", "-c", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    
    # If the return code is 0, the syntax is OK
    if result.returncode == 0:
        output_file.write("<h2>Syntax OK: </h2><p>{}</p>\n".format(file))
    # Else, there is a syntax error
    else:
        output_file.write("<h2>Syntax error: </h2><p>{}</p>\n".format(file))
        output_file.write(error.decode("utf-8") + "\n")

# Function to recursively search through folders and check Perl files
def folders(folder, output_file):
    for item in os.listdir(folder):
        itemPath = os.path.join(folder, item)
        # If the item is a directory, recursively check its contents
        if os.path.isdir(itemPath):
            folders(itemPath, output_file)
        # If the item is a Perl file, check its syntax
        elif os.path.isfile(itemPath) and item.lower().endswith(('.pl', '.plx')):
            perl_checker(itemPath, output_file)

# Define the current folder and the path for the output file
current_folder = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_folder, "output.html")

# Open the output file and start checking the current folder
with open(output_path, "w") as output_file:
    output_file.write("<html><head><title>Perl Checker Results</title></head><body>\n")
    output_file.write("<h1>Perl Analysis Report</h1>\n")

    folders(current_folder, output_file)

    output_file.write("</body></html>")

print("The HTML report was written to the file: {}".format(output_path))

# Determine the operating system to find and remove all pycache directories
if platform.system() == "Linux": 
    result = subprocess.Popen(["find", ".", "-type", "d", "-name", "__pycache__"], stdout=subprocess.PIPE)
    output, _ = result.communicate()
    pycache_directories = output.splitlines()

    for directory in pycache_directories:
        subprocess.Popen(["rm", "-rf", directory])

elif platform.system() == "Windows":
    # On Windows, use PowerShell to find and remove pycache
    subprocess.Popen(["powershell", "-Command",  "Get-ChildItem -Path . -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"])