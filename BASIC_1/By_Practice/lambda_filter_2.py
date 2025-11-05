

    # filter(function,iterables)

my_list= [1,2,3,4,5,6,9,12]
new_list=list(filter(lambda a: a % 2 == 0, my_list))
print(new_list)