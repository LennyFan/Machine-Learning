
# recursive
def binary(list_,l,r):
  # Basic 
  if l >= r:
    return (list_[l],lis_[l-1],lis_[l+1]) # one of them will be answer
  
  #### note:
  # l + (r-l)/2 = (l+r)/2
  mid = (l+r)/2
  if list_[mid] <= ??? :
    return binary(list_,mid+1,r)
  else:
    return binary(list_,l,mid-1)
  

# while loop
def binarySearch(nums, target):
    l, r = 0, len(nums)-1       # first position, and last position
    while l < r:
        med = (l+r)/2           # we can modify this to (l+r+1)/2 if we want to find the last target
        if nums[med] == target:
            r = med             # if we want to find first left
        elif nums[med] < target:
            l = med+1
        else:
            r = med-1
    if nums[l] == target:
        return [l,0]
    elif nums[l] < target:
        return [l,1]
    else:
        return [l,-1]
