def solve(list1: list, list2: list) -> list:
    ret = []
    for c in list1:
        if c in list2 and c not in ret:
            ret.append(c)
    ret.sort()
    return ret
