## THIS IS SNEAKY. Looks easy but really easy to mess up which i did
## TRY on your own first
words = ["abc", "fg", "hij", "klm", "nop", "qrs", "vwx"]
target = 1620

def string_to_num(s):
    sum = 0
    for ele in s:
        sum += ord("ele")-ord("a")+1
    return sum
    
def string_target(words, target):
    s = set()
    for ele in words:
        s.add(string_to_num(ele))

    for ele in s:
        if target//ele ==0:
            continue
        for ele2 in s:
            if target//(ele2*ele2) in s:
                return True
            
            