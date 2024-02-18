"""Author: Shahid Zain"""
def odds(lst):
    odd_no=[]
    for i in lst:
        if i%2!=0:
            odd_no.append(i)
        else:
            pass
    odd_sum=0
    odd_pro=1
    for i in odd_no:
        odd_sum=odd_sum+i
        odd_pro=odd_pro*i
    return odd_sum,odd_pro

n=int(input("enter the size of list : "))
nums=[]
for i in range(n):
    nums.append(int(input("enter the number : ")))

odd_sum,odd_pro=odds(nums)
print(f"the sum of odd numbers in list : {odd_sum}")
print(f"the product of odd numbers in list : {odd_pro}")
