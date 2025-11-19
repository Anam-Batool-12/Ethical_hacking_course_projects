import subprocess
import re

def get_mac(interface):
    output = subprocess.check_output(["ifconfig", interface], text=True)
    match = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", output)
    return match.group(0) if match else None

def change_mac(interface, new_mac):
    subprocess.run(["sudo", "ifconfig", interface, "down"])
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["sudo", "ifconfig", interface, "up"])
    current = get_mac(interface)
    if current.lower() == new_mac.lower():
        print(f"MAC successfully changed to {current}")
    else:
        print(f"MAC change failed. Current MAC: {current}")

iface = input("Interface: ")
new_mac = input("New MAC: ")
change_mac(iface, new_mac)
