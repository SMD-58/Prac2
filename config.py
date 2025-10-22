import configparser
import re

_TRUE = {"1", "true", "yes", "on", "y", "t"}
_FALSE = {"0", "false", "no", "off", "n", "f"}

_int_re   = re.compile(r"^[+-]?\d+$")
_float_re = re.compile(r"^[+-]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][+-]?\d+)?$")

def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    return s

def _infer_scalar(s):
    s = _unquote(s).strip()
    low = s.lower()

    if low in _TRUE:
        return True
    if low in _FALSE:
        return False

    if _int_re.match(s):
        try:
            return int(s.replace("_", ""))
        except ValueError:
            pass

    if _float_re.match(s):
        try:
            return float(s.replace("_", ""))
        except ValueError:
            pass

    return s

def parse_config(path):
    cfg = configparser.ConfigParser(interpolation=None)
    read_ok = cfg.read(path, encoding="utf-8")
    if not read_ok:
        raise FileNotFoundError("INI not found or unreadable: %s" % path)

    out = {}

    if cfg.defaults():
        out["DEFAULT"] = {}
        for k, v in cfg.defaults().items():
            val = _infer_scalar(v)
            k = f"{_unquote(k)}"
            out["DEFAULT"][k] = val

    for sec in cfg.sections():
        out[sec] = {}
        for k, v in cfg.items(sec, raw=True):
            val = _infer_scalar(v)
            out[sec][k] = val

 #   return "toster", out["DEFAULT"]
    return 0, out["DEFAULT"]


def _(path):
    parser =  configparser.ConfigParser()
    try:
        with open(path) as f:
            parser.read_file(f)
    except Exception as e:
        return 1, e

    return "toster", end
    return 0, end