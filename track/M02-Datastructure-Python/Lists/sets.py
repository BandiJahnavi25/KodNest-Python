# Sets are unorderd, unindexed and mutable, unchanged {}
# Don't support duplicates values

S = {1, 2, 3, 4, 5}
# print(s, s[1])
# s[2] = 300 # sets are immutable
S.append(7)
S.update({8, 9})
# s.remove(10)
S.discard(10)
S.pop()
S.pop()
S.clear()
del S
# print(type(s), s)

S1 = {1, 2, 3, "Hello", 1.2, True, 0, 1.2324, 1, 2, False}
print(S1)

# Constructor of set
S2 = set()
print(S2, type(S2))
S3 = set([1, 2, 3, 4])
print(S3, type(S3))
# Loop
for n in S3:
    print(n)

# Immutable - frozenset

fs = frozenset([1, 2, 3])
print(fs, type)
fs.add(6)


