import ipaddress
ip_subnet = ipaddress.ip_network('192.168.0.0/24')

print(f"The subnet mask is: {ip_subnet.netmask}")
