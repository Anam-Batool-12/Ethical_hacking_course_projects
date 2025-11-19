import subprocess
import optparse
import re

def get_current_mac(interface):
    result = subprocess.check_output(["ifconfig", interface]).decode()
    mac_address = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", result)
    if mac_address:
        return mac_address.group(0)
    return None

def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    current_mac = get_current_mac(interface)
    if current_mac.lower() == new_mac.lower():
        print(f"MAC address for {interface} successfully changed to {current_mac}")
    else:
        print(f"Failed to change MAC address for {interface}. Current MAC: {current_mac}")

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface")
parser.add_option("-m", "--mac", dest="new_mac")
(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)
