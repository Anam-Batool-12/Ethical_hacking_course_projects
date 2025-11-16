import subprocess

print("MAC Changer")

interface = "eth0"  
new_mac = "00:11:22:22:11:11"  

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])

subprocess.call(["sudo", "ifconfig", interface, "up"])
print(f"MAC address for {interface} changed to {new_mac}")
