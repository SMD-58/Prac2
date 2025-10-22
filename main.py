from pathlib import Path
from config import parse_config

initial_path = Path("./Initializations/first.ini")

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
            for key in args:
                print(key + ": " + str(args[key]))