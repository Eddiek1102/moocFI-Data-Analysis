def merge(list1: list, list2: list) -> list:
    merged_list = []
    
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list

if __name__ == "__main__":
    list1 = [9, 5, 3, 7, 88, 324, 432]
    list2 = [6543, 78, 3, 4, 22, 4, 65, 43, 67, 8, 5]
    
    merged_list = merge(sorted(list1), sorted(list2))
    print(merged_list)
    
