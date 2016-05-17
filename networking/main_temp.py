from ipscan import find_mac_on_network

TARGET_MAC = '00:90:0B:1E:B9:52'

target_ip = find_mac_on_network(TARGET_MAC)

print("Result: " + target_ip)
