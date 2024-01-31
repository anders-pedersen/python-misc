import ipaddress
ip_subnet = ipaddress.ip_network('192.168.0.0/24')

count = 1
top_limit = 10
for ip in ip_subnet.hosts():
    print(f"IP address: {ip}, Hostname: host{count:0>2}")
    count += 1
    if count > top_limit:
        break
