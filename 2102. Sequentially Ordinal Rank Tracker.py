
import heapq
from functools import total_ordering

class SORTracker:
    def __init__(self):
        self.min_pq = []  # store top k elements
        self.max_pq = []  # store remining elements
    
    def add(self, name: str, score: int) -> None:
        pair = Pair(score, name)
        heapq.heappush(self.min_pq, pair)
        heapq.heappush(self.max_pq, ReversePair(heapq.heappop(self.min_pq)))
    
    def get(self) -> str:
        pair = heapq.heappop(self.max_pq)
        heapq.heappush(self.min_pq, pair.original)
        return pair.original.name

# custom comparator according to the problem statement (python specific issue)
@total_ordering
class Pair:
    def __init__(self, score: int, name: str):
        self.score = score
        self.name = name
    
    def __lt__(self, other):
        """Less than comparison - implements compareTo logic"""
        # If scores are equal, compare names in REVERSE order
        if self.score == other.score:
            return other.name < self.name
        # Negative result means this < other
        return self.score < other.score
    
    def __eq__(self, other):
        """Equality comparison"""
        return self.score == other.score and self.name == other.name
    
    def __repr__(self):
        return f"Pair({self.score}, {self.name})"


class ReversePair:
    """Wrapper to reverse the comparison for max heap"""
    def __init__(self, pair: Pair):
        self.original = pair
    
    def __lt__(self, other):
        """Reverse the comparison - implements Comparator.reverseOrder()"""
        return self.original > other.original
    
    def __eq__(self, other):
        return self.original == other.original
    
    def __repr__(self):
        return f"Reversed({self.original})"
"""
Core idea: 
*
* *
*   *           
*  *  *.        *   
      ^         * *
      |         *   *
    min top     *  *  *.
                ^
                |
              max top
[MIN HEAP]  <>   [MAX HEAP]

right top contains k elements (k is num of queries called)
the monoent we add anything we push min element from right to left, this way a rebelance happens to maintain order in log n
when we query (get), we can take the max (left top) from left heap and add it to right heap, again k + 1 rebalancing happens
we can return top of right as it will be k elements
WE ADD FROM OPPOSITE Q AND POP IT AND APPEND THE POPED ELEMENT TO THE RELEVANT QUEUE THIS WAY AUTO REBALANCING OF ELEMENTS IN 
DESCENDING ORDER IS MAINTAINED
"""

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
