from collections import defaultdict


word = "supercalifragilisticexpialidocious"

freq = defaultdict(int)
for char in word:
    freq[char]+=1

s = [(f, alpha) for alpha, f in freq.items()]
s = sorted(s, key = lambda x: (-x[0], x[1]))
s = [alpha for _, alpha in s]
print(s)

