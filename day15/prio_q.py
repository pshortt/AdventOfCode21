from dataclasses import dataclass, field
from typing import Any
from heapq import heappush, heappop
from itertools import count

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    
@dataclass()
class PriorityQueue:
    # list of entries arranged in a heap
    pq: list = field(default_factory=list) 
    # mapping of tasks to entries
    entry_finder: dict = field(default_factory=dict)
    # placeholder for a removed task
    REMOVED: str = field(default='<removed-task>')  
    # unique sequence count
    counter: count = field(default_factory=count)   

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')
    
    def __len__(self):
        return len(self.pq)
    pass

def main():
    pass
if __name__=='__main__':
    main()