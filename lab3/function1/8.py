def spy_game(nums):
    alldig = ""
    for i in nums:
        alldig = alldig + str(i)
    for i in range(len(alldig)):
        if alldig[i:i+3] == "007":
            return True 
    return False       


a = list(map(int,input().split()))
print(spy_game(a))    