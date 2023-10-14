print("-- Setup! --")
print("This setup program will guide on how to properly setup your MakeX robot for basic functionality")
print("Press [A] to Continue Or [Q] to quit and return to shell prompt")
print("-------------------------")
prompt = input("setup > ")

# Bluetooth
print("[i] 1: Bluetooth")
print("Bring your bluetooth module and connect it to mbuild port 5")
print("""
                                    >-< HERE
   left <--- | [M1] [1] [2] [3] [4] [5]   ---> right
             |                   [batt]
        batt |                     [M2]
         usb |                     [M3]
             |                     [M4]
             --- [gpio] ----- [M6] [M5]
      """)
print("-------------------------")
print("Once done. Pair it to your gamepad, and press [1] on your gamepad to test")
prompt = input("setup > ")

# Wheels
print("[i] 2: Wheels\n-------------------------\nThis setup will work best for\n[1] Mecanum wheel\n[2] Holonomic X Drive\n[3] Standard drive train equipped robot. Other configurations will result in an unplayable robot\n-------------------------")

def print_wheel_fl():
    print(""" is your 1st wheel a front left wheel?
                    
 HERE -->  [wheel-1]                 [wheel-2]
          


          

           [wheel-3]                 [wheel-4]
-------------------------
""")
def print_wheel_fr():
    print(""" is your 2nd wheel a front right wheel?
                    
           [wheel-1]                 [wheel-2]  <-- HERE
          


          
          
           [wheel-3]                 [wheel-4]
-------------------------
""")
def print_wheel_rl():
    print(""" is your 3rd wheel a rear left wheel?
                    
           [wheel-1]                 [wheel-2]  
          


          
          
 HERE -->  [wheel-3]                 [wheel-4]
-------------------------
""")
def print_wheel_rr():
    print(""" is your 4th wheel a rear right wheel?
                    
           [wheel-1]                 [wheel-2]  
          


          
          
           [wheel-3]                 [wheel-4] <-- HERE
-------------------------
""")

print_wheel_fl()
input("setup > ")
print_wheel_fr()
input("setup > ")
print_wheel_rl()
input("setup > ")
print_wheel_rr()
input("setup > ")