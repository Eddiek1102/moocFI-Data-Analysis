def second_occurrence(nums: list, x: int) -> int:
    seen = False
    for index, num in enumerate(nums):
        if num == x:
            if seen == True:
                return index
            else:
                seen = True
    return -1 

if __name__ == "__main__":
    print(second_occurrence([1,2,98,5,-1,2,0,5,10], 5)) # 7