'''
Filter is used to keep or remove elements of list based on a function
'''

a = [1, 2, 3, 4, 5, 6, 7, 10, 11, 99, 100]

# Keep the even numbers and less than 50

print(list(filter(lambda x: x<50 and x%2 == 0, a)))

print(2^1)

a = ['asazs\\']

print(a[0].replace('as', 'AS'))


print("check:", 'Amsir' in 'asdasdaAmir')
print(all([True, True, True]))

print(f"#{1}{'219'} {2}")

import random
a = [1, 2, 55, 6, 7]
print(random.choice(a))