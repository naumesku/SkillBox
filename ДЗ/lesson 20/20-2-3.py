import random
def change(nums):
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    nums_l = list (nums)
    nums_l[index] = value
    return tuple(nums_l), value
my_nums = (1, 2, 3, 4, 5)

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)

new_nums = change(new_nums)[0]
rand_val += change(new_nums)[1]
print(new_nums, rand_val)
