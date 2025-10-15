import configparser

def parse_config(path):
    parser =  configparser.ConfigParser()
    try:
        parser.read(path)
    except Exception as e:
        return 1, e
#    return "toster", parser["DEFAULT"]
    return 0, parser["DEFAULT"]