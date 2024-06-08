import copy
original = [1,2,3,4]
shallowcopy = copy.deepcopy(original)

print(original)
print("*******printing copy now**********")
print(shallowcopy)
#changing the copy
shallowcopy.append(5)
print(original)
print(shallowcopy)