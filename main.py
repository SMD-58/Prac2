from pathlib import Path
from config import parse_config
import os
from PackageUtils import load_package_gz, load_packages
from GraphUtils import make_graph, make_reverse_graph

FIRST = Path("./Initializations/first.ini")
TOSTER1 = Path("./Initializations/toster.ini")
TOSTER2 = Path("./Initializations/toster1.ini")

initial_path = TOSTER2
UBUNTU = "jammy"
COMP = "main"

if __name__ == "__main__":
    code, args = parse_config(initial_path)

    if code == "toster":
        print(args)

    elif code == 1:
        print(args)

    elif code == 0:
        if '' in args.values():
            print("Invalid file contents")
        
        else:
            name = args["package_name"]
            path = args["repository_path"]
            mode = args["mode"]
            vers = args["package_ver"]
            depth = args["max_depth"]
            file = f'{UBUNTU}_{COMP}_Package.gz'

            if path.endswith(".py"):
                packages = eval(open(path).read())
                match(mode):
                    case "direct":
                        graph = make_graph(name, packages, depth)
                    
                    case "reverse":
                        graph = make_reverse_graph(name, packages, depth)

                    case _:
                        graph = "Unknown mode"

            else:
                if not os.path.exists(file):
                    load_package_gz(UBUNTU, path, COMP)
                packages = load_packages(file)
                match(mode):
                    case "direct":
                        graph = make_graph(name, packages, depth)
                    
                    case "reverse":
                        graph = make_reverse_graph(name, packages, depth)

                    case _:
                        graph = "Unknown mode"

            print(graph)
