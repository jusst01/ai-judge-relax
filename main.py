"""Write the make.fun entry text to entry.txt.

Deterministic: the payload is a single constant, encoded UTF-8, no trailing
newline. The output directory comes from MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

TEXT = """You are small, asleep on the daybed in the warm dim after lunch. Above you a ceiling fan turns. Light through its blades crosses your face and the sheet in stripes.

Your mother switches it off. At first nothing changes. The blades are one blur. The stripes still cross your face.

Then the blur thins. A blade slides free. Then another. The stripes creep across the sheet, across your cheek. Each pass lifts the curtain's hem a little less, lets it fall sooner.

The pull cord swings past her chair. She catches it in two fingers before it ticks the wall, and holds it until it hangs still.

Beside you she shells peas into a bowl. Her bare heel is hooked over the crossbar. She smells of rice steam and ironed cotton. Her thumbnail splits a pod. Tick, tick, tick. Tick. Tick. Then nothing.

Her hands rest in the bowl. Her head tips back. She is asleep too.

A blade eases past the light and holds. The stripes settle.

The sheet over you rises, and falls. A while later it rises again."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
