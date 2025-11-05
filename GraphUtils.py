def make_graph(root, packages, de): # добавить задаваемую глубину хрени
    def dfs(name, depth):
        if depth == 0:
            return
        graph[name] = set()
        d = packages.get(name, False)
        if d:
            for dep in d.get("dependencies", set()):
                if dep not in graph:
                    dfs(dep, depth-1)
                graph[name].add(dep)
    graph = {}
    dfs(root, de)
    return graph

def reversed_graph(pack, packages):
    pass