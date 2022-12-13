#this module is used to run external commands from Python
import subprocess 
"""
The try-except blocks are used to catch any errors that may occur while running the scripts.
The subprocess.run() function is used to run the scripts. It takes a list of strings as an argument, 
where the first string is the command to run (in this case, "python", python 3.7) and the second string is the name of the script to run.
"""
try:
    subprocess.run(["python", "run.py"])
except Exception as e:
    print("Error in run.py: ", e)

try:
    subprocess.run(["python", "analysis.py"])
except Exception as e:
    print("Error in analysis.py: ", e)

try:
    subprocess.run(["python", "anomalies_detection.py"])
except Exception as e:
    print("Error in anomalies_detection.py: ", e)
