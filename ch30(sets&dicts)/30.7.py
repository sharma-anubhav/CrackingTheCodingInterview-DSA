## THIS IS CORRECT BUT BAD
class Checker:
    def __init__(self, s1):
        self.s1 = s1
        self.s1_map = {ele: 0 for ele in s1}
        for ele in s1:
            self.s1_map[ele]+=1
            
    def expands_into(self, s2):
        if not len(s2) == len(self.s1)+1:
            return False
        s2_map = {ele: 0 for ele in s2}
        for ele in s2:
            s2_map[ele]+=1
            
        flag = False
        for ele, count in self.s1_map.items():
            if ele not in s2_map.keys():
                return False
            s2c = s2_map[ele]
            if s2c > count+2 or s2c < count:
                return False
            elif s2c == count+1 and flag:
                return False
            elif s2c == count+1:
                flag = True
        return True
    

# FOr anagram problems, you do not need 2 dictionaries. you can subtract
class Checker:
    def __init__(self, s1):
        self.s1 = s1
        
    def expands_into(self, s2):
        if not len(s2) == len(self.s1)+1:
            return False
            
        s2_map = {ele: 0 for ele in s2}
        for ele in s2:                      # <--- first add
            s2_map[ele]+=1

        for ele in self.s1:
            if ele not in s2_map.keys():
                return False
            s2_map[ele]-=1              # <--- Then subtract

        for count in s2_map.values():
            if count not in [0,1]:      # <--- Nothing should be anything other than 0/1
                return False    
        return True
    
        

checker = Checker("tea")
print(checker.expands_into("tea"))   # returns False
print(checker.expands_into("team"))  # returns True
print(checker.expands_into("seam"))  # returns False

checker = Checker("on")
print(checker.expands_into("nooo"))  # returns False
print(checker.expands_into("not"))   # returns True
print(checker.expands_into("now"))   # returns True




        