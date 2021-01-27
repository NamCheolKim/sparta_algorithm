# 인접 리스트가 주어질때, 모든 노드를 DFS 순서대로 방문하시오.

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):

    stack = [start_node]
    visited = []

    while stack:
        current_node = stack.pop()
        visited.append(current_node)

        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)

    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]
