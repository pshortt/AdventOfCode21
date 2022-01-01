from dataclasses import dataclass, field
from typing import Any
from heapq import heappush, heappop
from itertools import count
from rich.console import Console

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    
@dataclass()
class PriorityQueue:
    pq: list = field(default_factory=list)                         # list of entries arranged in a heap
    entry_finder: dict = field(default_factory=dict)               # mapping of tasks to entries
    REMOVED: str = field(default='<removed-task>')      # placeholder for a removed task
    counter: count = field(default_factory=count)     # unique sequence count

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
    console = Console()
    pq = PriorityQueue()
    console.print(bool(pq))
    tasks = [
        'task1',
        'task2',
        'task3',
    ]
    prios = [
        1,
        3,
        2,
    ]
    for t, p in zip(tasks, prios):
        pq.add_task(t, p)
        console.print(f'Added task: [green]{t}[/] with prio:[purple]{p}[/]')
    
    while pq:
        console.print(f'Popped task: {pq.pop_task()}')
    

if __name__=='__main__':
    main()