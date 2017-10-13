
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




# customized sort function
# 
a = [[1,2],[5,6]]
def cmp_items(a, b):
    if a[0] > b[0]: # 由小到大
        return 1
    elif a[0] == b[0]:
        return 0
    else:
        return -1
a.sort(cmp_items)


# customized max/min function
max(a, key = lambda p: p[2])
max(a, key = lambda p: p.score)


# Dictionary
#
# max( dic, key = func )
# https://stackoverflow.com/questions/26871866/print-highest-value-in-dict-with-key
# https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
#
# iteration
for key,val in Dic.iteritems():
    print key,val
    
# function as objects(item)
def foo():
    pass
def bar():
    pass
dic = {'foo': foo, 'bar': bar}
dic['foo']()


# bin
a = 6
bin(a)
> '0b110'

# count()
a = "aaaabbbcca"
a.count('a')
> 5
