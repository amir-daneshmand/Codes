def is_colorful(arr):
    dic = {}
    arr_list = list(arr)
    for length in range(1, len(arr)+1):
        for starting_index in range(0, len(arr)-length+1):
            subseq = list(map(int, arr_list[starting_index:starting_index+length]))
            col_num = color_number(subseq)
            if col_num not in dic:
                dic[col_num] = 1
            else:
                return False
    return True


def color_number(arr_):
    if arr_:
        return arr_.pop(0)*color_number(arr_)
    else:
        return 1

print(is_colorful("356"))
