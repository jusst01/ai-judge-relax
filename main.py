"""Write the make.fun entry text to entry.txt.

Deterministic: the payload is a single constant, encoded UTF-8, no trailing
newline. The output directory comes from MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

TEXT = """You are small, asleep on the daybed in the warm dim after lunch. Above you a ceiling fan turns. Light through its blades crosses your face and the sheet in stripes.

Your mother reaches up and switches it off. At first nothing changes. The blades are still one blur. The stripes cross at the same pace.

Then the blur thins. The blades separate. The stripes creep across the sheet, across your cheek. Each pass lifts the curtain's hem a little less, and lets it fall sooner.

The pull cord, still swinging, passes her chair. She catches it in two fingers before it can tick the wall. She holds it until it forgets how to swing.

The blades pass the window one at a time. They can be counted. Between sweeps the quiet lasts longer. Under it your breathing is the slowest thing left. It too is slowing.

A blade eases past the light and stops there. The stripes come to rest.

The sheet over you rises, and falls, and a while later rises again. The room's last motion. In no hurry to stop."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
