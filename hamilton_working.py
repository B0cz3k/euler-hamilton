def Hamiltonian(num_verts, num_edges, edges):
    # adjacency list
    adj_list = [[] for _ in range(num_verts + 1)]

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    # check degree
    for i in range(1, num_verts + 1):
        if len(adj_list[i]) < 2:
            return 'No Hamiltonian cycle'

    # main program
    stack = [edges[0][0]]
    visited = {edges[0][0]}
    last_visited = None
    next_neighbor = {v: 0 for v in range(1, num_verts + 1)}
    
    while stack:
        current_vertex = stack[-1]

        if next_neighbor[current_vertex] >= len(adj_list[current_vertex]):
            last_visited = stack.pop()
            visited.remove(last_visited)
            next_neighbor[last_visited] = 0
            continue

        neighbor = adj_list[current_vertex][next_neighbor[current_vertex]]
        next_neighbor[current_vertex] += 1

        if neighbor in visited:
            continue

        stack.append(neighbor)
        visited.add(neighbor)

        if len(stack) == num_verts and edges[0][0] in adj_list[neighbor - 1]:
            return stack
        

f = open('test.txt')
num_vert, num_edges = f.readline().split(' ')
num_vert, num_edges = int(num_vert), int(num_edges)

edges = []

for _ in range(num_edges):
    a, b = f.readline().split(' ')
    edges.append([int(a), int(b)])

print(Hamiltonian(num_vert, num_edges, edges))