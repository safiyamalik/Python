nums=list(map(int,input("enter numbers: ").split()))
n=len(nums)

if n<=1:
    print("list should be of minimum 2 elements")
else:
    for i in range(n):
         for j in range(0,n-i-1):
             if nums[j]>nums[j+1]:
                 nums[j],nums[j+1]=nums[j+1],nums[j]


    print("sorted list:",nums)
    print("second largest:",nums[-2])
