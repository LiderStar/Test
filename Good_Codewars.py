def score(n):
    st = ""
    sum = 0
    data = {'111': 1000, '666':600, '555':500, '444':400,'333':300,'222':200, '1':100,'5':50}
    n_new = sorted(n)       
    for i in n_new[0:]:
        d_tmp = n_new.count(i)
        if d_tmp >= 3:
            st += str(i)*3 + " " + str(i)*(d_tmp-3)
            del n_new[:d_tmp]
        elif d_tmp == 2:
            st += " " + str(i) +" " + str(i)
            del n_new[:d_tmp]
        elif d_tmp == 1:
            st += " " + str(i)
            del n_new[:d_tmp]
        
              
    for i in st.split():
        if i in data:
            sum += data[i]
    # print(st)
    return sum

print( score( [2, 3, 4, 6, 2] ))#, 0)
print( score(  [4, 4, 4, 3, 3] ))#, 400)
print( score(  [2, 4, 4, 5, 4] ))#, 450)
print( score(  [1, 1, 1, 3, 1] ))#, 450)
print( score( [1, 5, 1, 3, 4] ))#, 250)