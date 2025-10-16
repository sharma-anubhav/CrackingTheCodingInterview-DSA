def robot2(s):
    if len(s) < 1:
        return
        
    if len(s) ==  1:
        return s[0]
        
    if s[0] in "LR":
       return s[0]+robot2(s[1:])  # <- Inefficient because we have to pass in a new string each time as argument.
                                  # <- but this is traditional recursion 
    else:
        a = robot2(s[1:])
        if len(s) >=2:
            return a + robot2(s[2:])
        return a

        


def robot2(s):  # <------------- More efficient since we do not pass any substring rather just a pointer 
    i = 0
    ans = []
    
    def robot_helper(i):  
        if i >= len(s):       # <------------ Easier to manage out of bounds since we can check index before accessing
            return 
        if s[i] in ["L", "R"]:
            ans.append(s[i])
            robot_helper(i+1)
        else:
            robot_helper(i+1)
            robot_helper(i+2)
    robot_helper(i)
    
    return "".join(ans)
    
print(robot2("LL2R2L"))


# How about this. This is more traditional recursion but still has the index efficiency
# IMPORTANT THING IS TO MOVE TOWARDS BASE CASE AND HERE IT IS TO REACH i>len(s)
def robot3(s):  # <------------- More efficient since we do not pass any substring rather just a pointer 
    i = 0
    
    def robot_helper(i):  
        if i >= len(s):       # <------------ Easier to manage out of bounds since we can check index before accessing
            return ""
            
        if s[i] in ["L", "R"]:
            return s[i] + robot_helper(i+1)
        else:
            return robot_helper(i+1) + robot_helper(i+2)
            
    return robot_helper(i)

print(robot2("LL2R2L"))
    
            
        










