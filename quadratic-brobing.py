import random

space_list=['-' for x in range(100)]

hash_list = [random.randint(0,1000) for x in range(100)]

for hash_data in hash_list:
    hash_mod = hash_data % 100
    if space_list[hash_mod]=='-':
        space_list[hash_mod]=hash_data
    else:
        num = 1
        while True:
            if space_list[(hash_mod + num*num)%100]=='-':
                space_list[(hash_mod + num*num)%100]=hash_data
                break
            num += 1

for x in space_list:
    print(x)
