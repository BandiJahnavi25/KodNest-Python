original = [[10 , 20] , [30 , 40]]
copy = original
copy[0][0] = 100
print(copy)
print(original)

original = [[10 , 20] , [30 , 40]]
copy = original . copy()
copy[0][0] = 100
print(copy)
print(original)

original = [[10 , 20] , [30 , 40]]
cpy_list = copy . deepcopy(original)
cpy_list[0][0] = 100
print(original)
print(cpy_list)
