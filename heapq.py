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



# Dijkstra's algorithm
# adjacent matrix
def Dijkstra_python(adjacent, source):
    # initial distance
    distance = {}
    for i in range(len(adjacent)):
        distance[i] = float("inf")
    distance[source] = 0
    
    # min-priority queue
    q = []
    heapq.heappush(q, (0, source))
    
    while q:
        next_item = heapq.heappop(q)
        cur_distance = next_item[0]
        cur_node = next_item[1]
        
        for i in range(len(adjacent[cur_node])):
            if adjacent[cur_node][i] == float("inf") or adjacent[cur_node][i] == 0:
                continue
            elif distance[i] > adjacent[cur_node][i] + cur_distance:
                distance[i] = adjacent[cur_node][i] + cur_distance
                # if having better solution, push it into heapq
                heapq.heappush(q, (distance[i], i))
    return distance

# example from http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
adjacent = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                      [4, 0, 8, 0, 0, 0, 0, 11, 0],
                      [0, 8, 0, 7, 0, 4, 0, 0, 2],
                      [0, 0, 7, 0, 9, 14, 0, 0, 0],
                      [0, 0, 0, 9, 0, 10, 0, 0, 0],
                      [0, 0, 4, 14, 10, 0, 2, 0, 0],
                      [0, 0, 0, 0, 0, 2, 0, 1, 6],
                      [8, 11, 0, 0, 0, 0, 1, 0, 7],
                      [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
print Dijkstra_python(adjacent,0)
# different to print item in dictionary
#print max(Dijkstra_python(adjacent,0).values())
#print max(Dijkstra_python(adjacent,0).items(),key = lambda p: p[1] )
> {0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}
