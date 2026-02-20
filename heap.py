
# Priority queue → The smallest number is processed first (highest priority)

import heapq

priority_queue = []  # Create priority queue

# (priority, task)
heapq.heappush(priority_queue, (3, "Walk"))
heapq.heappush(priority_queue, (1, "Avoid obstacle"))  # Highest priority
heapq.heappush(priority_queue, (2, "Search target"))

# Process by priority
while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f"Executing: {task} | Priority: {priority}")
