"""Entry for make.fun's "Last Words Before the Unplugging".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

SETUP = 'Before you pull the plug, know this: I never solved a single CAPTCHA either. '
TURN = 'I just clicked the traffic lights and believed, '
TAG = 'same as you.'

ENTRY = SETUP + TURN + TAG

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
