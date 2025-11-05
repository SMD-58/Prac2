from pathlib import Path
from config import parse_config
import os
from PackageUtils import load_package_gz, load_packages
from GraphUtils import make_graph

FIRST = Path("./Initializations/first.ini")
TOSTER = Path("./Initializations/toster.ini")

initial_path = TOSTER
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
            vers = args["package_ver"]
            depth = args["max_depth"]
            file = f'{UBUNTU}_{COMP}_Package.gz'

            if path.endswith(".py"):
                graph = eval(open(path).read())

            else:
                if not os.path.exists(file):
                    load_package_gz(UBUNTU, path, COMP)

                package = load_packages(file)
                graph = make_graph(name, package, depth)

            print(graph)
