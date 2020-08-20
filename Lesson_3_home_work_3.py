def my_func(arg_1, agr_2, arg_3):
    my_list =[arg_1, agr_2, arg_3]
    min_of_my_list = min(my_list)
    remove = my_list.remove(min_of_my_list)
    return sum(my_list)

print(my_func(int(input("num_1: ")), int(input("num_2: ")), int(input("num_3: "))))