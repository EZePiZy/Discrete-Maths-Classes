import numpy as np

def bool_sort(lst):
    lst_sorted = [None] * (len(lst) + 1)
    count_T = 1
    count_F = 1

    for i in range(len(lst)):
        if (lst[i] == False):
            lst_sorted[count_F] = False
            count_F += 1
        else:
            lst_sorted[len(lst) - count_T + 1] = True
            count_T += 1 

    lst_sorted.pop(0)   
    return 'The sorted list is: ' + str(lst_sorted), 'The number of occurences of "False" is: ' + str(count_F - 1), 'The number of occurences of "True" is: ' + str(count_T - 1)




test = np.random.choice(a=[False, True], size=3000000)

print(bool_sort(test))








