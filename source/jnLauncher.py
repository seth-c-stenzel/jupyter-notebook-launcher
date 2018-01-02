# Simple Application for Launching ipython/jupyter notbooks
# 1. Install Pyinstaller: cmd -> pip3 install pyinstaller
# 2. Compile with pipinstaller: cmd-> pipinstaller --onefile --icon=rocket.ico jnLauncher.py
# 3. Place executable somewhere, like your documents.
# 4. Set filetypes .ipynb opened with new exe


import os
import sys
import time


try:
    if len(sys.argv) > 1:
        print(sys.argv[1])
        dirpath = os.path.dirname(sys.argv[1])
        print(dirpath)
        os.system("cd \"" + str(dirpath) + "\" & jupyter notebook \"" + str(sys.argv[1]) + "\"")
    else:
        print("Use this application by setting it as the default\open program for the IPYNB extention.\n\n")
        print("No Jupyter notebook argument given....")
        print("Closing.......")
        time.sleep(5)
except:
    print("Something went very wrong :(")
