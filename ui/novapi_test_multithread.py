import novapi
import machine
import _thread
import time
import os

# important function
print("""
  _   _ ______ _______ _        ___  _   _  _____ 
 | \ | |  ____|__   __| |      | \ \| \ | |/ ____|
 |  \| | |__     | |  | |_ ___ | || |  \| | (___  
 | . ` |  __|    | |  | __/ _ \| || | . ` |\___ \ 
 | |\  | |____   | |  | || (_) |_|| | |\  |____) |
 |_| \_|______|  |_|   \__\___/(_)| |_| \_|_____/ 
                                 /_/              
                                                  """)
print("--- NETto!_NS Runtime ---\n[i] This runtime is compiled for NovaPi V1_3\n[W] For testing purposes!\n---------")
print("machine:\n{}".format(dir(machine)))
print("---\nnovapi:\n{}".format(dir(novapi)))
print("---\nthreading:\n{}".format(dir(_thread)))

print("done")