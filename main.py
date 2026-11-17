"""Write the make.fun entry text to entry.txt.

Deterministic: the payload is a single constant, encoded UTF-8, no trailing
newline. The output directory comes from MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

TEXT = """The last pot leaves the flame. The flame goes out. The ring stays warm a moment, then does not.

Chairs go up on the tables in twos, and each pair lands without a sound.

Under the bench a cat turns itself around its own warmth, tucks its nose, and sleeps again.

Then the first rain on the zinc awning, soft, the sort that settles in and asks nothing.

The owner gives the counter a last wipe, then one that was not needed, and hangs the cloth on the rail.

He goes home through the first few drops, no faster than the rain."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
