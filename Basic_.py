
# any() will return True if there's any truth value in the iterable.
data = [False, False, False]
not any(data)
>>> True


# copy a list
nums = [1,2,3,4]
copy = list(nums)



# replace somthing in string
s = "lenny"
print(s.replace("e", "a"))
>>> "lanny"



# list [::]
# [start:end:step]
nums = [1,2,3,4,5,6]

nums[::-1] == [6,5,4,3,2,1]
nums[:0:-2] == [6,4,2]
nums[:-1:-1] == []

nums[:-1:3] = [1,4]





