def num_plus(num = 8, result = 0):
    if(num == 0): return result
    num += 1
    return num_plus(num - 3, result + num)

print(num_plus())
print(num_plus())
print(num_plus())
print(num_plus())
