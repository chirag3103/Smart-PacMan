graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
"""
    def dfs(graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
        return visited

    print dfs(graph, 'A')
"""

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

print dfs(graph, 'C')

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print list(dfs_paths(graph, 'A', 'F'))







my code:
    def dfs(graph, start, visited=None):
    
    frontier = problem.getStartState()
    do while True:
        if frontier is None:
            pass
        else frontier.append(problem.getSuccessors(frontier)):
            node=frontier.pop()
        if node=problem.isGoalState():
            return solution
        else
            frontier.append(problem.getSuccessors(node))
            pass
        pass

    if visited is None:
        visited = problem.getStartState()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

    print dfs(graph, problem.getStartState())


#executing code
    #frontier.append(problem.getSuccessors(frontier))
    print frontier
    lst=[]
    node =[]
    lst.append(startposition)

    for i in problem.getSuccessors(startposition):
        lst.append(i[0])
    print lst
    node=lst.pop()
    print lst
    print node


    frontier = util.PriorityQueue()
    visited = []
    h = heuristic(problem.getStartState(), problem)
    g = 0
    f = g + h
    startingNode = (problem.getStartState(), None, g, []);
    frontier.push(startingNode, f)
    while not frontier.isEmpty():
        curr = frontier.pop()
        currLoc = curr[0]
        currDir = curr[1]
        currCost = curr[2]
        if currLoc not in visited:
            currPath = curr[3]
            visited.append(currLoc)
            successors = problem.getSuccessors(currLoc)
            successorsList = list(successors)
            for i in successorsList:
                if i[0] not in visited:
                    if(problem.isGoalState(i[0])):
                        return currPath + [i[1]]
                h = heuristic(i[0], problem)
                g = currCost + i[2]
                f = g + h
                newNode = (i[0], i[1], g, currPath+[i[1]])
                frontier.push(newNode, f)
    return []
