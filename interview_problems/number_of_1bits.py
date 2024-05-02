import collections
s = 11

def find_1bits(n):
    converted_n = bin(n)
    print(converted_n)
    count = collections.Counter(converted_n)
    print(count)
    return count.get('1')

res = find_1bits(s)
print(res)