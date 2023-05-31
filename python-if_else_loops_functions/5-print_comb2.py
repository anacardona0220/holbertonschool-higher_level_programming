#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{:02d}".format(i), end="\n")
        continue
    print("{:02d}{}{}".format(i, ',', ' '), end="")
    # print("{:02d}".format(item), end=", " if item < 99 else "\n") otra forma de hacerlo
