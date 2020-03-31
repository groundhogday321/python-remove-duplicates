



# PYTHON REMOVE DUPLICATES

# remove duplicates from a list
l1 = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 5]
l2 = list(set(l1))
print(l2)

# another way to remove duplicates from list
# this preserves order
l3 = [7, 7, 6, 6, 1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 5]
l4 = []
for i in l3:
    if i not in l4:
        l4.append(i)
print(l4)

# remove duplicates function
def remove_dups_func(numbers):
    return set(numbers)

# remove duplicates lambda function
remove_dups_lambda = lambda numbers: list(set(numbers))
print(remove_dups_lambda([1,1,1,2,3,3]))

# symmetric difference (new set with elements in either but not both)
set1 = {1, 2, 3}
set2 = {1, 2, 4}
remove_in_common_dups = set1.symmetric_difference(set2)
print(remove_in_common_dups)

# remove duplicate values from dictionary
d1 = {'exterior': ['blue', 'blue', 'green'], 'interior': ['leather', 'cloth', 'leather']}
d2 = {}
for k,v in d1.items():
    d2[k] = set(v)
print(d2)

# remove duplicates while preserving order
l5 = [10, 10, 4, 4, 7, 7, 7]
l6 = list(set(l5))
l6.sort(key=l5.index)
# print(l6.sort(key=l5.index))
print(l6)
