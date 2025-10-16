connections = [("203.0.113.10", "mike"), ("298.51.100.25", "bob"),
("292.0.2.5", "mike"), ("203.0.113.15", "bob2")]


def duplicate(connections):
    d = dict()
    maxf = None
    for ip, id in connections:
        if id not in d.keys():
            d[id] = 1
        else:
            d[id] +=1

        if not maxf:
            maxf = id
        else:                       # <------- Notice that this can get confusing and is prone to errors
            if d[id] >= d[maxf]:    # <------- Doesnt look good if you are figuring this in interviews
                maxf = id
    return maxf

print(duplicate(connections))
    

def duplicate(connections):
    d = dict()
    for ip, id in connections:
        if id not in d.keys():
            d[id] = 1
        else:
            d[id] +=1

    most_shared_user = None
    for user, count in d.items():
        if not most_shared_user or count >= d[most_shared_user]:   # <------- Notice how this is super easy to understand
            most_shared_user = user
    return most_shared_user
    

print(duplicate(connections))
    











