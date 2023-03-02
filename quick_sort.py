
def quick_sort(array):
    if len(array)<=1:
        return array
    else:
        small_list = []
        large_list = []
        equal_list = []
        key_item = array[len(array)//2]
        for item in array:
            if item < key_item:
                small_list.append(item)
            elif item > key_item:
                large_list.append(item)
            else:
                equal_list.append(item)
        sorted_list = quick_sort(small_list) + equal_list + quick_sort(large_list)
    return sorted_list

if __name__ == '__main__':
    list_ = [3,2,1]
    print(quick_sort(list_))
