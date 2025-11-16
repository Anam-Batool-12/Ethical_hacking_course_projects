import subprocess
import optparse
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interface to change")
parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
(options, arguments) = parser.parse_args()

print("MAC Changer")
interface = options.interface
mac_addr = options.new_mac


subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_addr])
subprocess.call(["sudo", "ifconfig", interface, "up"])

print(f"MAC address for {interface} changed to {mac_addr}")
