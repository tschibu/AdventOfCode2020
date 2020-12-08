with open("input") as f:
    numbers = list(map(int, f.readlines()))

# part 01
for i in numbers:
    for j in numbers:
        if i+j == 2020:
            print(i*j)
            pass


# part 02
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i+j+k == 2020:
                print(i*j*k)

