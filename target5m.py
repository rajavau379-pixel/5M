# -*- coding: utf-8 -*-
# Decode By DEEP-XD         
import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
import platform
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# ==========================================
# 🔐 SECURITY LOCK SYSTEM (USERNAME & PASSWORD)
# ==========================================
def login_lock():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
        
    # ASCII Art with Color (Light Green)
    print("""\033[1;32m
8888888b.            d8b               888     888                  
888   Y88b           Y8P               888     888                  
888    888                             888     888                  
888   d88P  8888b.  8888  8888b.       Y88b   d88P 8888b.  888  888 
8888888P"      "88b "888     "88b       Y88b d88P     "88b 888  888 
888 T88b   .d888888  888 .d888888        Y88o88P  .d888888 888  888 
888  T88b  888  888  888 888  888         Y888P   888  888 Y88b 888 
888   T88b "Y888888  888 "Y888888          Y8P    "Y888888  "Y88888 
                     888                                            
                    d88P                                            
                  888P"
\033[0m""")

    # Security Banner
    print("\033[1;36m════════════════════════════════════════════════════════════\033[0m")
    print(" \033[1;33m[!] THIS TOOL IS PROTECTED WITH USERNAME & PASSWORD\033[0m")
    print("\033[1;36m════════════════════════════════════════════════════════════\033[0m")
    
    # Login Prompts
    username = input(" \033[1;32m[?] ENTER USERNAME : \033[0m")
    password = input(" \033[1;32m[?] ENTER PASSWORD : \033[0m")
    
    # Credential Verification
    if username == 'Raja' and password == 'Vau':
        print("\n \033[1;32m[✓] LOGIN SUCCESSFUL! STARTING TOOL...\033[0m")
        time.sleep(1)
    else:
        print("\n \033[1;31m[x] INCORRECT USERNAME OR PASSWORD!\033[0m")
        sys.exit()

# Start the script
if __name__ == "__main__":
    login_lock()
    
    # Add your main tool logic below this line
    # print("\033[1;36m[+] Welcome to the main menu...\033[0m")
