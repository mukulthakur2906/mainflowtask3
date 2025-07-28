#--------------------------------------------------------
#Find Second Largest
#-------------------------------------------------------
nums = list(map(int, input("Enter numbers: ").split()))
nums = list(set(nums))  # remove duplicates
nums.sort()
if len(nums) >= 2:
    print("Second largest:", nums[-2])
else:
    print("No second largest found.")
