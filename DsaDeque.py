# Deque means double ended queue. means the operation upon the queue can be  performed from both sides
# if we add and  delete from one side in deque then its seems like stack
from collections import deque

L=[1, 2, 3, 1, 4, 2, 5, 3, 1, 6, 4]
q=deque(L)
print(q)

# here we add element at end(RHs) and start(LHS)
q.append(10)
print(q)

q.appendleft(7)
print(q)

# here we remove the element at end(RHs) and start(LHS)
q.pop()
print(q)

q.popleft()
print(q)

# now we add multiple elements in deque at end(RHs) and start(LHS)
q.extend([10,8,9])
print(q)

q.extendleft([5,9,6])
print(q)

# rotating queue if you enter any number then this elements are rotate
q.rotate(2)
print(q)

# removing element
q.remove(6)
print(q)


