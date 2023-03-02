# def buble(array_):
#     check = False
#     while not check:
#         check = True
#         for i in range(len(array_)-1):
#             if array_[i] > array_[i + 1]:
#                 array_[i], array_[i + 1] = array_[i + 1], array_[i]
#                 check = False
#     return array_
#
#
# list_ = [3, 2, 1]
# sorted_list = buble(list_)
# print(sorted_list)
def selection(mass):
    for i in range(len(mass)):
        index_min = i
        for j in range(i+1, len(mass)):
            if mass[index_min] > mass[j]:
                index_min = j
        mass[i],mass[index_min] = mass[index_min], mass[i]
    return mass



if __name__ == '__main__':
    list_ = [3,2,7,1,7,8]
    sorted_list_ = selection(list_)
    print(sorted_list_)