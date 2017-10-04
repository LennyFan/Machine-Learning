inport heapq
# for all k
# a[k] <= a[2*k+1] and a[k] <= a[2*k+2] 
# we can use this to achieve shortest-path algorithm

q = []

heapq.heappush(q, (5, 'bwa'))
heapq.heappush(q, (7, 'bwa'))
heapq.heappush(q, (2, 'bwa'))
heapq.heappush(q, (1, 'bwee'))
heapq.heappush(q, (3, 'kiki'))

print q 

while q:
    next_item = heapq.heappop(q)
    print q
    
> [(1, 'bwee'), (2, 'code'), (3, 'sleep'), (5, 'sleep'), (7, 'sleep')]
> [(2, 'code'), (3, 'sleep'), (5, 'sleep'), (7, 'sleep')]
> [(3, 'sleep'), (7, 'sleep'), (5, 'sleep')]
> [(5, 'sleep'), (7, 'sleep')]
> [(7, 'sleep')]
> []
