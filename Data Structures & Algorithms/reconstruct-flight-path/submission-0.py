class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dest in sorted(tickets, reverse=True):
            graph[src].append(dest)

        stack = ["JFK"]
        itinerary = []

        while stack:
            curr = stack[-1]

            if graph[curr]:
                stack.append(graph[curr].pop())
            else:
                itinerary.append(stack.pop())

        return itinerary[::-1]