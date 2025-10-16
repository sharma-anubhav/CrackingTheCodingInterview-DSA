ips = ["203.0.113.10", "208.51.100.5", "202.0.2.5", "203.0.113.5"]


## THIS IS SAME AS BEFORE BUTTTTTTTT
## WHAT IS THE SPACE COMPLEXITY? FYI ITS NOT O(N) why?
def common(ips):
    d = {}
    for octet in [ip.split(".")[0] for ip in ips]:
        if not octet in d.keys():
            d[octet] = 0
        d[octet]+=1
    
    most_common = None
    for octet, count in d.items():
        if not most_common or count > d[most_common]:
            most_common = octet
    return most_common

print(common(ips))