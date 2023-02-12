A = (10.1, -1.2)

def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)
print(tup_r(A))