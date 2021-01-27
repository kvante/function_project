def sum_element(*args):
    s = 0
    m = 0
    for i in args:
        s += i
        continue
    for i in args:
        if i == args[-1]:
            m = i

        return m, s
    print(s)

print(sum_element(1, 2, 3, 3, 5, 8))

