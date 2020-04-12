from sys import argv

from settings import HISTORY_JSON_PATH
from utils import check_update


def cmd_init():
    with open(HISTORY_JSON_PATH, "w") as wf:
        wf.write("{}")
    check_update()


if __name__ == "__main__":
    if "init" in argv:
        cmd_init()