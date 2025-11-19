import subprocess
import optparse

def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print(f"MAC address for {interface} changed to {new_mac}")

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface")
parser.add_option("-m", "--mac", dest="new_mac")
(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)
