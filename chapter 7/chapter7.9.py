def bfs(graph, start):
    visited = set()  # для посещенных вершин
    order = []  # порядок обхода
    queue = [start]  #начальная вершина

    while queue:
        vertex = queue.pop(0)  # первый элемент очереди
        if vertex not in visited:
            visited.add(vertex)  # посещенная вершина
            order.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}

# Тестовый пример
start_vertex = 'A'
result = bfs(graph, start_vertex)
print("Обход в ширину:", result)
# Ожидаемый результат: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']