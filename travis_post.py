# travis_post.py
"""Make sure that each tex file produced a pdf file."""

from os.path import isfile
from travis_common import raise_msg

def all_present(fatal=True):
    try:
        assert isfile("Vol1.pdf"), "Vol1.pdf is missing"
        assert isfile("Vol2.pdf"), "Vol2.pdf is missing"
        assert isfile("Vol3.pdf"), "Vol3.pdf is missing"
        assert isfile("Vol4.pdf"), "Vol4.pdf is missing"
        assert isfile("ExtraLabs.pdf"), "ExtraLabs.pdf is missing"
    except AssertionError as e:
        raise_msg(e, fatal)
    
if __name__ == "__main__":
    all_present(True)
