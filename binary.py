
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
l,r = 0, len(list_)-1
res = None

while (l <= r):
  mid = (l+r)/2
  if list_[mid] <= ???:
    res = list_[mid]
    l = mid+1
  else:
    r = mid-1

return res
