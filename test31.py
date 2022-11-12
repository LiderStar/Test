# import re
#
# st = "(123) 456-7890"
# patt = r"\W\d{3}\W\s(\d{3})-(\d{4})"
# if re.fullmatch(patt, st):
#     print('True')


lt = [1,2,3,9]
lt[-1] = lt[-1] + 5
if lt[-1] > 9:
    lt[-1] = lt[-1] % 10
    lt[-2] = lt[-2]+1
print(lt)
lt.insert(0, 7)
print(lt)


def up_array(arr):
    print(arr)
    tmp = 0
    if arr == [] or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        arr[-1] = arr[-1] + 1
        arr1 = arr[::-1]

        for i in range(len(arr1)):
            if arr1[i] > 9:
                tmp, arr1[i] = arr1[i] // 10, arr1[i] % 10

                try:
                    arr1[i + 1] += tmp
                    if arr1[i + 1] <= 9:
                        break
                    else:
                        continue
                except IndexError:
                    arr1.append(arr1[i] + 1)
    return arr1[::-1]

def up_array(a):
    if not a or any(not 0 <= x < 10 for x in a): return
    for i in range(1, len(a)+1):
        a[-i] = (a[-i] + 1) % 10
        if a[-i]: break
    else: a[:0] = [1]
    return a
print(up_array([]))