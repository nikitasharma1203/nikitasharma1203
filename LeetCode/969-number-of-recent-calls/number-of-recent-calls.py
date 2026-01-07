from collections import deque

class RecentCounter:

    def __init__(self):
        # Initialize an empty queue
        self.q = deque()

    def ping(self, t: int) -> int:
        # Add the new request
        self.q.append(t)
        
        # Remove requests older than t - 3000
        while self.q[0] < t - 3000:
            self.q.popleft()
        
        # Return number of recent requests
        return len(self.q)
