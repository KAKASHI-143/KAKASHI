import os, sys
os.system("git pull")
try:
    __import__("ARIYANBHAI").ARIYAN()
except Exception as e:
    exit(str(e))
