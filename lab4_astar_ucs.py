# Lab 4: A* and UCS Search


graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

heuristic = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}


def get_cost(path):
    total = 0

    for i in range(len(path) - 1):
        for node, cost in graph[path[i]]:
            if node == path[i + 1]:
                total += cost

    return total



def a_star(start, goal):

    open_list = [(start, [start], 0)]

    while open_list:

        node, path, cost = open_list.pop(0)

        if node == goal:
            return path, cost

        for next_node, edge in graph[node]:
            new_cost = cost + edge
            f = new_cost + heuristic[next_node]

            open_list.append(
                (next_node, path + [next_node], new_cost)
            )

        open_list.sort(key=lambda x: x[2] + heuristic[x[0]])

    return None



def ucs(start, goal):

    queue = [(start, [start], 0)]

    while queue:

        node, path, cost = queue.pop(0)

        if node == goal:
            return path, cost

        for next_node, edge in graph[node]:
            queue.append(
                (next_node, path + [next_node], cost + edge)
            )

        queue.sort(key=lambda x: x[2])



print("A* Search")

path, cost = a_star("S", "G")
print("Path:", path)
print("Cost:", cost)
print("Checked Cost:", get_cost(path))


print("\nUCS Search")

path, cost = ucs("S", "G")
print("Path:", path)
print("Cost:", cost)
print("Checked Cost:", get_cost(path))


print("\nHeuristic Test")

new_heuristic = heuristic.copy()
new_heuristic["C"] = 10

print("Original h(C):", heuristic["C"])
print("Changed h(C):", new_heuristic["C"])
print("Changing one heuristic value can affect A* optimality.")
