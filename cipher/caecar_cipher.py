import string


def caesarCipher(s, k):
    up_alp = string.ascii_uppercase
    rotate_up_alp = up_alp[k % 26 :] + up_alp[: k % 26]
    low_alp = string.ascii_lowercase
    rotate_low_alp = low_alp[k % 26 :] + low_alp[: k % 26]
    ans = ""

    for i in s:
        if i in up_alp:
            ans += rotate_up_alp[up_alp.index(i)]
        elif i in low_alp:
            ans += rotate_low_alp[low_alp.index(i)]
        else:
            ans += i
    return ans
