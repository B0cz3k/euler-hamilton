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

    while stack:
        curr_vert = stack[-1]
        found = False

        for neighbor in adj_list[curr_vert]:
            if neighbor not in visited and neighbor != last_visited:
                stack.append(neighbor)
                visited.add(neighbor)
                found = True
                last_visited = None
                break

        if not found:
            if len(stack) == num_verts and edges[0][0] in adj_list[curr_vert]:
                return stack
            
            last_visited = stack.pop()
            visited.remove(last_visited)
            while stack and adj_list[last_visited - 1] == []:
                last_visited = stack.pop()
                visited.remove(last_visited)

f = open('hamilton.txt')
num_vert, num_edges = f.readline().split(' ')
num_vert, num_edges = int(num_vert), int(num_edges)

edges = []

for _ in range(num_edges):
    a, b = f.readline().split(' ')
    edges.append([int(a), int(b)])

print(Hamiltonian(num_vert, num_edges, edges))