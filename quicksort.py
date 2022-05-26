import random
import pickle
import time
from matplotlib import pyplot as plt

quick_time = []
list_of_data = []

k = int(input('Введите кол-во data-set-ов: '))
n = int(input('Введите начальное кол-во элементов data-set-а: '))
l = n
s = int(input('Введите шаг элементов data-set-ов: '))
# Создание data-set
for i in range(k):
    with open(f'dataset/{n}_data_set.pickle', 'wb') as file:
        test_list = [random.randint(-1000, 1000) for x in range(n)]
        pickle.dump(test_list, file)
        print('Создан data-set: ', len(test_list))
        list_of_data.append(n)
        n += s


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


for i in range(k):
    with open(f'dataset/{l}_data_set.pickle', 'rb') as file:
        data = pickle.load(file)
        time_start = time.time()
        quicksort(data)
        time_end = time.time() - time_start
        quick_time.append(time_end)
        l += s

plt.plot(list_of_data, quick_time)
plt.show()
