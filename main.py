"""Write the make.fun entry text to entry.txt.

Deterministic: the payload is a single constant, encoded UTF-8, no trailing
newline. The output directory comes from MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

TEXT = """The switch clicks in the hottest hour of the afternoon, and at first nothing follows it. The blades are still one grey smear, the curtain still breathes, and the light through the blades still crosses the wall in stripes.

Then the smear thins. The blades come apart, and the stripes begin to creep across the wall. Each pass lifts the curtain's hem a little less, and sets it down a little sooner.

The pull cord is still swinging wide, as it was while the fan ran. It goes on by itself, out and back, and nothing else in the room is going that fast now.

The blades pass the window one at a time. They can be counted. Between one sweep of the stripes and the next, the quiet lasts longer, and longer.

One blade eases past the light and stops there. The stripes come to rest on the wall. Only light now, going nowhere.

The cord swings on after the blades have stopped, smaller each time, the last moving thing in the room. Then it, too, hangs straight."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
