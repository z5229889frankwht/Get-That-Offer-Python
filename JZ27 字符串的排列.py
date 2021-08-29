a = "abc"

import itertools


def Permutation(ss):
    # write code here
    result = []
    if ss:
        res = itertools.permutations(ss)
        for i in res:
            result.append("".join(i))
        print(sorted(set(result)))
    else:
        return None


Permutation(a)
