import _thread
import time

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


sample_data = {
    "name": "mbuild1",
    "port": 1,
    "yes": True
}


for i in sample_data:
    print(sample_data[i])