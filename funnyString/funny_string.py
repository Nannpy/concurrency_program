import string


def funnyString(s):
    low_str = string.ascii_lowercase
    ss = []
    for i in range(len(s) - 1):
        ss.append(abs(low_str.index(s[i]) - low_str.index(s[i + 1])))

    rr = ss[-1::-1]
    if ss == rr:
        return "Funny"
    return "Not Funny"
