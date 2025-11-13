def make_graph(root, packages, de):
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

def make_reverse_graph(pack, packages, de):
    sorte = {}
    for pkg, data in packages.items():
        for dep in data.get("dependencies", set()):
            sorte.setdefault(dep, set()).add(pkg)

    def dfs(name, depth):
        if depth == 0:
            return
        graph[name] = set()
        for dep in sorte.get(name, set()):
            if dep not in graph:
                dfs(dep, depth-1)
            graph[name].add(dep)

    graph = {}
    dfs(pack, de)
    return graph


