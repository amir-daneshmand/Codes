def counter_generator():
    count = 0
    while count<10:
        count += 1
        yield count


for t in counter_generator():
    print(t)

