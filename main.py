from pathlib import Path
from config import parse_config

initial_path = Path("./Initializations/first.ini")

if __name__ == "__main__":
    code, args = parse_config(initial_path)

    if code == "toster":
        pass
        for i in args.values():
            print(type(i))

    elif code == 1:
        print(args)

    elif code == 0:
        if "" in args.values() or "" in args.keys():
            print("Invalid file contents")
        
        else:
            for key in args:
                print(key + ": " + args[key])