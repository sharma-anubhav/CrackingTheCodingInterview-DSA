connections = [("203.0.113.10", "mike"), ("298.51.100.25", "bob"),
("292.0.2.5", "mike"), ("203.0.113.15", "bob2")]


def duplicate(connections):
    s = set()
    for ip, id in connections:
        if id in s:
            return ip
        s.add(id)
    return None

print(duplicate(connections))
    