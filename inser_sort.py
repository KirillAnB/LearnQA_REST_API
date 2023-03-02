def insertiom_sort(array):
    for i in range(1,len(array)):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and array[j] > item_to_insert:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = item_to_insert

    return array

if __name__ == '__main__':
    list_ = [3,2,1,0]
    sorted_list = insertiom_sort(list_)
    print(sorted_list)