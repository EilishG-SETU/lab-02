import re

ips = []
pattern = r"\d+\.\d+\.\d+\.\d+"
with open('auth.log', 'r') as f:
    for ip in f:
        x=re.findall(pattern, ip)
        for ip in x:
            ips.append(ip)
unique_ips = set(ips)
print("Unique IPs:")
for ip in unique_ips:
    print(ip) 

with open('unique_ips.txt', 'w') as f:
    for ip in unique_ips:
        f.write(ip+"\n")