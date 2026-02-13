class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# Queue(큐)
# First In First Out
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            current = new_node
            self.tail.next = current
            self.tail = current

        self.cnt += 1

    def empty(self):
        return self.head is None

    def pop(self):
        if self.empty():
            self.tail = None
            self.cnt = 0
            return -1
            
        current = self.head
        self.head = current.next
        self.cnt -= 1
        return current.data

    def size(self):
        return self.cnt

    # size
    # def size(self):
        # 큐에 들어있는 정수 개수 반환!!

        # 비어 있으면 -> 0
        # 우리에게 주어진 정보는 head, tail
        # head부터 출발해서 node 개수 세기
    def front(self):
        return -1 if self.empty() else self.head.data
        
        # if self.empty():
            # return -1
        # else:
            # return self.head.data
            
    def back(self):
        reutrn -1 if self.empty() else self.tail.data

# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

N = int(input()) # N = 4 -> 4, N = 5 -> 2

q = Queue()
for i in range(1, N+1):
    q.push(i)

while True:
    if q.size() == 1:
        break
    else:
        q.pop()
    if q.size() == 1:
        break
    else:
        q.push(q.pop())

print(q.pop())