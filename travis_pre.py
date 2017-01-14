# travis_pre.py
"""Ensure that there are no unapproved files exceeding the max filesize."""

from os import popen
from travis_common import raise_msg


# 200KB in bytes
MAX_FILESIZE = 204800


def getOutput(cmd):
    return popen(cmd).read()


def find_big_files(fatal=True):

    # Load the names of the files listed in the exceptions file.
    with open("travis_large_files.txt", 'rU') as ex:
        approved_files = {name for name in ex.read().split('\n') if name != ""}

    # Get the objects in the tree at the most recent commit.
    this_commit = getOutput("git rev-list HEAD").split()[0]
    tree = getOutput("git ls-tree -rlz {}".format(this_commit)).split("\0")

    # Check that the objects in the tree are not too big.
    violations = set()
    for obj in tree:
        try:
            data = obj.split()
            size, name = int(data[3]), data[4]
            if name not in approved_files and size > MAX_FILESIZE:
                violations.add((name, size))
        except (IndexError, ValueError):
            continue

    if violations:
        files = "\n".join(sorted(["\t{:.<50}{:.>20} bytes".format(*v)
                                                        for v in violations]))
        msg = "Large files present:\n{}\nAdd these files to ".format(files)
        msg += "'travis_large_files.txt' if they are necessary to keep."
        raise_msg(msg, fatal=fatal)


if __name__ == "__main__":
    find_big_files(True)
