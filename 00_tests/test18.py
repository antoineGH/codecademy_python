import heapq

heap = [(5, "Strawberries"), (6, "Apples"), (7, "Oranges")]

heapq.heappush(heap, (8, "Grapes"))
heapq.heappush(heap, (2, "Tomatoes"))

print("The smallest values in the heap in ascending order are:\n")
while heap:
  print(heapq.heappop(heap))




