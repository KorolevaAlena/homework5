immutable_var = "Sun", 745, False, 0.37
print(immutable_var)
immutable_var [1] = 5 #нельзя изменить значения элементов кортежа, так как кортеж относится к неизменяемым типам данных.
mutable_list = [5, 7, "cat", "tree"]
mutable_list [0] = 8
mutable_list [1] = "dog"
mutable_list [2] = 57
mutable_list [3] = "frog"
print(mutable_list)