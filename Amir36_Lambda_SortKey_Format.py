                                    #  LAMBDA APPLICATION
f = lambda x: 3-2*x
g = lambda x: x-1

x = 0
while abs(f(x) - g(x))>0.1:
    x += 0.05

print(x, g(x), f(x))

                                        # SORT and KEY

a = [(0,5), (10, 0), (2, 5), (-1, 2), (10, -2)]
a.sort()
print(a)

# sort based on scond value
a.sort(key = lambda x: x[1])
print(a)


                                        #Formatttt
a_str = "My name is {}, and I would like to {}"
print(a_str.format("Amir", "teach"))