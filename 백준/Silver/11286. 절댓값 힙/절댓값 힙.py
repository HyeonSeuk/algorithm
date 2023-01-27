import heapq
import sys
heap = []
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(heap, (abs(a), a))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)