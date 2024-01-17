import ipaddress
ip1 = ipaddress.ip_address('192.168.0.1')
ip2 = ipaddress.ip_address('192.168.0.2')
subnet0 = ipaddress.ip_network('192.168.0.0/28')
subnet16 = ipaddress.ip_network('192.168.0.16/28')

print(f"type(ip1): {type(ip1)}")
print(f"ip1.is_private: {ip1.is_private}")
print(f"ip2.is_private: {ip2.is_private}")
print()
print(f"type(subnet0): {type(subnet0)}")
print(f"subnet0.is_private: {subnet0.is_private}")
print(f"subnet16.is_private: {subnet16.is_private}")
print()
print(f"subnet0.broadcast_address: {subnet0.broadcast_address}")
print(f"subnet16.broadcast_address: {subnet16.broadcast_address}")
print()
print(f"ip1 in subnet0: {ip1 in subnet0}")
print(f"ip1 in subnet16: {ip1 in subnet16}")
print()
print(f"ip1 == ip2: {ip1 == ip2}")
print(f"ip1 > ip2: {ip1 > ip2}")
print(f"ip1 < ip2: {ip1 < ip2}")
print()
print(f"ip1 + 1: {ip1 + 1}")
