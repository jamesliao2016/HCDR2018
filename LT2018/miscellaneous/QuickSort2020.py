def QuickSort(val_array):
    if len(val_array)<2:
        return val_array
    else:
        val_l, val_r = [], []
        idx_m = len(val_array)//2
        val_m = val_array[idx_m]
        val_array.remove(val_m)
        for val_i in val_array:
            if val_i<val_m:
                val_l.append(val_i)
            else:
                val_r.append(val_i)
        return QuickSort(val_l) + [val_m] + QuickSort(val_r)

if __name__ == '__main__':
    array_test = [3,2,1,6,5,4,9,8,7]
    res = QuickSort(array_test)
    print(res)