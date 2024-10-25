def interleave(*lists) -> list:
    # all lists have equal length
    ans = []
    
    for i in range(len(lists[0])):
        for list in lists:
            ans.append(list[i])
    
    return ans
    

if __name__ == "__main__":
     print(interleave([1,2,3], [20,30,40], ['a', 'b', 'c']))
     # [1, 20, 'a', 2, 30, 'b', 3, 40, 'c']