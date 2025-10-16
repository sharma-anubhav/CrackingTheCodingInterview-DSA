answers = ['a', 'b', 'c', 'c']
m = 5
students = [
    # student ID, desk, answers
    (4, 10, ['a', 'b', 'c', 'd']),
    (1, 6,  ['a', 'b', 'c', 'd']),
    (3, 8,  ['a', 'b', 'd', 'd']),
    (5, 11, ['a', 'b', 'c', 'd']),
    (9, 7,  ['a', 'b', 'c', 'd']),
    (6, 16, ['a', 'b', 'd', 'd'])
]

## THIS IS A GOOD SOLUITON  really compact and intuitive. GOOD SELECTION
def in_same_row(desk1, desk2):
    if desk1//m == desk2//m:
        return True
    return False
    
def suspects(answers, m, students):
    d2s = {}
    for sid, desk, ans in students:
        d2s[desk] = (sid, ans)

    sus = []
    for sid, desk, ans in students:
        # if desk-1 in d2s.keys() and in_same_row(desk-1, desk):
        #     if ans == d2s[desk-1][1] and ans != answers:          ### <- WE DONT EVEN NEED TO CHECK BOTH NBR. THIS WILL AVOID REPETETION
        #        sus.append((sid, d2s[desk-1][0] ))
        if desk+1 in d2s.keys() and in_same_row(desk+1, desk):
            if ans == d2s[desk+1][1] and ans != answers:
                sus.append((sid, d2s[desk+1][0] ))
    return sus
print(suspects(answers, m, students))


## THIS also uses hashmaps but has poorly selected keys and values and usage
## while this might solve, it is really bad confusing and prone to mistake. 
## BAD DESIGNED LOGIC AND ALLs
def find_nbrs(bench, m):
    row = bench//m
    nbrs = []
    if (bench+1)//m == row:
        nbrs.append(bench+1)
    if (bench-1)//m == row:
        nbrs.append(bench-1)
    return nbrs
    
def find_suspects(benches, m):
    sus = set()
    for bench in benches:
        nbrs = find_nbrs(bench, m)
        for nbr in nbrs:
            if nbr in benches:
                sus.add((bench, nbr))
    return sus
    
def suspects2(answers, m, students):
    d = {}
    d[tuple(answers)] = []

    for sid, bench, answer in students:
        if tuple(answer) not in d.keys():
            d[tuple(answer)] = set()
        d[tuple(answer)].add(bench)

    suspects = []
    for tup, benches in d.items():
        if tup == tuple(answers):
            continue

        if len(benches)>1:
            sus = find_suspects(benches, m)
            if sus:
                suspects.extend(sus)







        
            