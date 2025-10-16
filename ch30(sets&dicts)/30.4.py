users = [
  ("mike", ["203.0.3.10", "208.51.0.5", "52.0.2.5"]),
  ("bob", ["111.0.0.10", "222.0.0.5", "222.0.0.8"]),
  ("bob2", ["222.0.0.5", "222.0.0.8", "111.0.0.10"])
]

# EFFICEIENT USE OF HASHMAPS
# Single pass over users (N)
def cheater(users):
    s = set()
    for user, ips in users:
        hashable_ips = tuple(sorted(ips))  # <---- tuples are ordered so we need to sort
        if hashable_ips not in s:
            s.add(hashable_ips)
        else:
            return True, user
    return False

print(cheater(users))

# INEFFICEINT USE OF HASHMAPS
# N+N^2 passes over users SO WORSE IF YOU DIRECTLY USE HASMAPS
def cheater2(users):
    d = dict([(user, set(ips)) for user, ips in users])
    for user, ips in users:
        for h_user, h_s in d.items():
            if user!=h_user:
                match = True
                for ip in ips:
                    if not ip in h_s:
                        match = False
                        break
                if match:
                    return True, user, h_user
    return False
                        

