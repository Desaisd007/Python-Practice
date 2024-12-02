# This works on one of the famous data structure that is called as Heap, and it works as a priority queue.
# Priority queue means it will try to always give you the highest priority element from the list.
# in heapq small element=high priority, high ele= low priority

import heapq
H=[]
# here we pass single as well as sequence(but it consider as a single ele)to heapq
heapq.heappush(H,[10,20,30,40])
print(H)

# whenever you entering elements. it automatically set the smallest element at 1st index
heapq.heappush(H,[30])
print(H)
# heapq is stores homogeneous objects

print('*********************************************')
# here we add integers
H1=[]
heapq.heappush(H1,10)
heapq.heappush(H1,20)
heapq.heappush(H1,30)
heapq.heappush(H1,40)
print(H1)

# pop remove smallest element(high priority) in heap
heapq.heappop(H1)
print(H1)

# here we entering multiple elements(sequence) in heapq
L=[50, 10, 30, 70, 20, 30, 10, 40]
heapq.heapify(L)
print(L)

#here we print largest element in heapq
print(heapq.nlargest(1,L))
print(heapq.nlargest(2,L))

#here we find smallest  element in heapq
print(heapq.nsmallest(1,L))
print(heapq.nsmallest(2,L))


# note: heap data strcture always give smallest element


