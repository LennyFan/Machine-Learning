
# two way to solve
# Dynamic programming or Recursive Function


# Example:
# delete minimum char with ASCII as weight to match two strings

a = "haha" 
b = "kaka"

# recursive solution
# ** only check boundary in the beginning
def check_d(a,b):
    if len(a) > len(b):
        return check_d(b,a)
  
    if not a:
        return sum([ord(char) for char in b])
    
    
    if a[0] == b[0]:
        return check_d(a[1:],b[1:])
    else:
        return min(ord(a[0]) + check_d(a[1:],b),
                   ord(b[0]) + check_d(a,b[1:]))

    
# DP solution
# ** need to check a lot of boundaries
def help(c1,c2):
    if c1 != c2:
        return ord(c1) + ord(c2)
    else:
        return 0
        
def check_d2(a,b):
    dic = {}
    for i in xrange(len(a)):
        for j in xrange(len(b)):
            if i>0 and j>0:
                dic[(i,j)] = min(
                    help(a[i],b[j]) + dic[(i-1,j-1)] ,
                    help(a[i],b[j]) + dic[(i-1,j)] - help(a[i-1],b[j]) + ord(a[i-1]),
                    help(a[i],b[j]) + dic[(i,j-1)] - help(a[i],b[j-1]) + ord(b[j-1]))
            elif i>0:
                dic[(i,j)] = help(a[i],b[j]) + dic[(i-1,j)] - help(a[i-1],b[j]) + ord(a[i-1])
            elif j>0:
                dic[(i,j)] = help(a[i],b[j]) + dic[(i,j-1)] - help(a[i],b[j-1]) + ord(b[j-1])
            else:
                dic[(i,j)] = help(a[i],b[j])
    
    # delete eveything after [i,len(b)-1]
    dic[(0, len(b))] =  dic[(0, len(b)-1)]
    for i in xrange(1,len(a)):
        dic[(i,len(b))] = min(dic[(i-1,len(b))] + ord(a[i]), dic[(i,len(b)-1)])
        
    dic[(len(a), 0)] =  dic[(len(a)-1, 0)]
    for i in xrange(1,len(b)):
        dic[(len(a),i)] = min(dic[(len(a),i-1)] + ord(b[i]), dic[(len(a)-1,i)])
    
    return min(dic[(len(a)-1,len(b)-1)],dic[(len(a)-1,len(b))], dic[(len(a),len(b)-1)])
            
print check_d2(a,b)
print check_d(a,b)
