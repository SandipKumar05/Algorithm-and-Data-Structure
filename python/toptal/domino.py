from collections import defaultdict

def longest_domino_chain(domino_string):
    def build_graph(domino_string):
        graph = defaultdict(list)
        domino_tiles = domino_string.split(';')

        for tile in domino_tiles:
            end1, end2 = map(int, tile.split('-'))
            graph[end1].append(end2)

        return graph

    def dfs(node, visited):
        visited[node] = True
        chain_length = 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                chain_length = max(chain_length, 1 + dfs(neighbor, visited))

        return chain_length

    graph = build_graph(domino_string)
    max_chain_length = 0

    for start_node in graph:
        visited = {node: False for node in graph}
        max_chain_length = max(max_chain_length, dfs(start_node, visited))

    return max_chain_length

# Example usage:
domino_string = "3-4;4-4;1-2;3-1;2-5"
result = longest_domino_chain(domino_string)
print(result)
