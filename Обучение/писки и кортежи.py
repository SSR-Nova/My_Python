def count_frequency(lst):

    my_dict = {}
    for i in lst:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict

list1 = [1,2,3,4,5,2,4,5,2,3,3,3]
print(count_frequency(list1))
