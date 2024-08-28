#linear search 
#method 1

numbers = input("Enter the numbers: ").split(",")

arr= list(numbers)

finding_element = input("what are you looking for? ")

if finding_element in arr: 
    print("this number exists")

for i in range(0, len(arr)):
    if arr[i] == finding_element:
        print("this number exists")


#method 2

for num in arr:
    if num == finding_element:
        print("you got it! ")
