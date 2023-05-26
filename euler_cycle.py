def Euler(num_vert, num_edges, edges):
    adj_list = [[] for _ in range(num_vert + 1)]

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    # check even degrees
    for vertex in range(1, num_vert + 1):
        if len(adj_list[vertex]) % 2 != 0:
            return 'No Eulerian cycle'

    # DFS
    cycle = []
    stack = [edges[0][0]]
    while stack:
        curr_vert = stack[-1]
        if adj_list[curr_vert]:
            next_vert = adj_list[curr_vert].pop()
            stack.append(next_vert)
            adj_list[next_vert].remove(curr_vert)
        else:
            cycle.append(stack.pop())

    # check if all edges visited, return the cycle
    return 'No Eulerian cycle' if len(cycle) != num_edges + 1 else cycle


f = open('euler.txt')
num_vert, num_edges = f.readline().split(' ')
num_vert, num_edges = int(num_vert), int(num_edges)

edges = []

for _ in range(num_edges):
    a, b = f.readline().split(' ')
    edges.append([int(a), int(b)])

print(Euler(num_vert, num_edges, edges))