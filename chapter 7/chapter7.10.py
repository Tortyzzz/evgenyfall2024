def dfs(graph, start):

    visited = set()
    order = []

    def help_dfs(vertex):

        visited.add(vertex)
        order.append(vertex)

        # Рекурсивно обходим всех соседей
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                help_dfs(neighbor)

    help_dfs(start)
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
result = dfs(graph, start_vertex)
print("Обход в глубину:", result)
# Ожидаемый результат: ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G', 'I']