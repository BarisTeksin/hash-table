import random

space_list=['-' for x in range(100)]

hash_list = [random.randint(0,1000) for x in range(100)]

for hash_data in hash_list:
    hash_mod = hash_data % 100
    if space_list[hash_mod]=='-':
        space_list[hash_mod]=hash_data
    else:
        if isinstance(space_list[hash_mod], int):
            temp = []
            temp.append(space_list[hash_mod])
            temp.append(hash_data)
            space_list[hash_mod] = temp
        else:
            temp = []
            for mini_data in space_list[hash_mod]:
                temp.append(mini_data)
            temp.append(hash_data)
            space_list[hash_mod] = temp

for x in space_list:
    print(x)
