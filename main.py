"""Write the entry patch note for make.fun's "Real-Life Patch Notes" bounty.

The entry is one original patch note for a bug in real life or human
biology: a single line of at most 160 characters, written like a real
release note. This program writes that line to entry.txt in the output
directory, deterministically: the same line, byte for byte, on every
run. Standard library only; no network.
"""

import os

LINE = "v36.2.1: Fixed a memory bug: the brain keeps every embarrassing moment from age 12 in perfect detail but deletes new passwords within the hour."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 160:
        raise ValueError("patch note must be 1 to 160 characters")
    if not LINE.strip():
        raise ValueError("patch note must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would raise PermissionError and fail the run.
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    try:
        os.chmod(DESTINATION, 0o644)
    except PermissionError:
        pass
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
