# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def count_anagrams(string):
    buckets = dict()
    for i in range(len(string)):
	for j in range(1, len(string) - i + 1):
            key = frozenset(Counter(string[i:i+j]).items())
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key]-1) // 2
    return count

t = int(raw_input().strip())
for a0 in range(t):
    print count_anagrams(raw_input().strip())
   
