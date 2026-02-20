
# Queue → FIFO: First in, first out

from collections import deque

queue = deque()

# Enqueue: add tasks
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

# Dequeue: process tasks in order
while queue:
    task = queue.popleft()
    print(f"Processing: {task}")
