import os, sys
os.system("git pull")
try:
    __import__("KAKASHIXN").ARIYAN()
except Exception as e:
    exit(str(e))
