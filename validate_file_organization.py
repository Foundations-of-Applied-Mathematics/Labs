# validate_file_organization.py
"""Make sure labs.json matches the actual repository structure."""

import os
import json


JSONFILE = "labs.json"


class RepoStructureError(Exception):
    """Custom exception class for mismatch between the actual repository
    folder hierarchy and the structure indicated by labs.json.
    """
    pass


# Read labs.json.
with open(JSONFILE, 'r') as infile:
    LABS = json.load(infile)


# Check each entry for errors.
errors = []
for name in LABS:
    lab = LABS[name]

    # Check that the folder exists.
    folder = os.path.join(lab["volume"], name)
    if not os.path.isdir(folder):
        errors.append(NotADirectoryError(folder))
        continue

    # Check that the spec and solutions files exist (and are stored as lists).
    for key in ["spec", "solutions"]:
        if not isinstance(lab[key], list):
            errors.append(TypeError(f"{lab}/{key} should be a list"))
            continue
        labfiles = lab[key]
        for labfile in labfiles:
            target = os.path.join(folder, labfile)
            if not os.path.isfile(target):
                errors.append(FileNotFoundError(target))

    # Check that the test driver exists if specified.
    driver = lab["driver"]
    if driver:
        target = os.path.join(folder, driver)
        if not os.path.isfile(target):
            errors.append(FileNotFoundError(target))

    # Make sure each lab has a title.
    if "title" not in lab:
        errors.append(ValueError(name + " has no title"))

# Report errors (or lack of errors).
if errors:
    raise RepoStructureError(f"File system does not match {JSONFILE}:\n\t"
          + "\n\t".join([type(e).__name__ + ': ' + e.args[0] for e in errors]))
else:
    print(f"SUCCESS: {JSONFILE} matches repository structure")
