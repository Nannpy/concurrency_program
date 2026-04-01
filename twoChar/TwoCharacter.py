import itertools


def alternate(s):
    max_length = 0
    uniques = set(s)
    for a, b in itertools.combinations(uniques, 2):
        filtered = [i for i in s if i == a or i == b]
        l = len(filtered)
        valid = True
        for i in range(1, l):
            if filtered[i] == filtered[i - 1]:
                valid = False
                break

        if l > max_length and valid:
            max_length = l

    return max_length
