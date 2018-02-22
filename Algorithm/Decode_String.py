
def Decompression(s):
    nums = []
    holder = []
    i = 0
    while i < len(s):
        
        cur = i
        while s[i].isdigit():
            i += 1
        if cur != i:
            nums.append(int(s[cur:i]))
        
        if s[i] == "[":
            holder.append("[")
            
        elif s[i] == "]":
            sub = holder.pop()
            if sub == "[":
                pass
            else:
                sub *= nums.pop()
                holder.pop()
                holder.append(sub)
        else:
            if holder and holder[-1] != "[":
                holder[-1] += s[i]
            else:
                holder.append(s[i])
        i += 1
        
    
    return "".join(holder)
            
print Decompression(s)           