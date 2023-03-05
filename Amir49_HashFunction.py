def _hash(s):
    code = 0
    for i, char in enumerate(s):
        code += 10**i*ord(char)
    return code

print(_hash('Amir'))
print(_hash('Jack'))
x = 'Amir'
print(hash(x), hash(x))

a = (1,2)

i, j =a
print(i, j)