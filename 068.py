numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def convert_to_num(a, b, c, d, e, f, g, h, i, j):
    """
    Function to convert a-j to
    required string based on the criteria
    """
    big_num = {a: 0, d: 1, f: 2, h: 3, j: 4}
    break_num = big_num[min(big_num.keys())]
    nums = [(a, b, c), (d, c, e), (f, e, g), (h, g, i), (j, i, b)]
    nums = nums[break_num:]+nums[:break_num]
    string = ''
    for num_tup in nums:
        for num in num_tup:
            string += str(num)
    return string


# list to store solutions
avail_sol = []

# start with all the numbers
for a in numbers:
    numbers_b = numbers[:]
    numbers_b.remove(a)
    # numbers without a
    for b in numbers_b:
        numbers_c = numbers_b[:]
        numbers_c.remove(b)
        # numbers without a, b
        for c in numbers_c:
            line_sum = a+b+c
            numbers_d = numbers_c[:]
            numbers_d.remove(c)
            # numbers without a, b, c
            for d in numbers_d:
                numbers_e = numbers_d[:]
                numbers_e.remove(d)
                e = line_sum - c - d
                # numbers without a, b, c, d
                if e in numbers_e:
                    numbers_f = numbers_e[:]
                    numbers_f.remove(e)
                    # numbers without a, b, c, d, e
                    for f in numbers_f:
                        numbers_g = numbers_f[:]
                        numbers_g.remove(f)
                        g = line_sum - e - f
                        # numbers without a, b, c, d, e, f
                        if g in numbers_g:
                            numbers_h = numbers_g[:]
                            numbers_h.remove(g)
                            # numbers without a, b, c, d, e, f, g
                            for h in numbers_h:
                                numbers_i = numbers_h[:]
                                numbers_i.remove(h)
                                i = line_sum - g - h
                                # check if i is in numbers_i list
                                if i in numbers_i:
                                    j = line_sum - i - b
                                    numbers_j = numbers_i[:]
                                    numbers_j.remove(i)
                                    # numbers without a, b, c, d, e, f, g, h, i
                                    if j in numbers_j:
                                        ctn = convert_to_num(
                                            a, b, c, d, e, f, g, h, i, j)
                                        avail_sol.append(ctn)

# solution will be the maximum of all the numbers
sol = max([int(x) if len(x) == 16 else 0 for x in avail_sol])

# print the solution
print(sol)
