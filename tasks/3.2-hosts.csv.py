import ipaddress
import csv

ip_subnet = ipaddress.ip_network('192.168.0.0/24')
file_name = 'hosts.csv'
count = 1
top_limit = 10

with open(file_name, 'w', newline='') as csvfile:
    csvfile_content = csv.writer(csvfile, delimiter=',')
    for ip in ip_subnet.hosts():
        # print(f"IP address: {ip}, Hostname: host{count:0>2}")
        csvfile_content.writerow([ip, f"host{count:0>2}"])
        count += 1
        if count > top_limit:
            break
