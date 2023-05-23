#UDF
def bubblesort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums

#Unsorted List
nums = [9, 3, 7 ,4, 6 , 2, 1, 5, 8, 0]

#Function Call
num = bubblesort(nums)
print(num)

#Another way

list = eval(input("\n\nEnter a list of elements: "))
n = len(list)
for i in range(n):
    for j in range(0, n - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print("List after sorting : ", list)