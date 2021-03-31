
def merge(list_left, list_right):
    """
    入参数组都是有序的，此处将两个有序数组合并成一个大的有序数组
    """
    # 两个数组的起始下标
    l, r = 0, 0
    new_list = []
    while l < len(list_left) and r < len(list_right):
        if list_left[l] < list_right[r]:
            new_list.append(list_left[l])
            l += 1
        else:
            new_list.append(list_right[r])
            r += 1
    new_list += list_left[l:]
    new_list += list_right[r:]
    return new_list


def merge_sort(lists):
    if len(lists)<=1 : return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left,right)


print(merge_sort([2, 6, 10, 3, 5, 8, 4]))