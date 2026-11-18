"""Write the make.fun entry text to entry.txt.

Deterministic: the payload is a single constant, encoded UTF-8, no trailing
newline. The output directory comes from MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

TEXT = """You are small, asleep on the daybed in the warm, dim room after lunch. Above you the ceiling fan turns, and the light through its blades crosses your face and the sheet in stripes.

Your mother switches it off. At first nothing changes. One blur. The stripes still lie across your face.

Then the blur thins. A blade slides free, and another. The stripes creep over the sheet, over your cheek, a little further on each pass.

The pull cord, still swinging, passes her chair. She catches it in two fingers so it will not tick the wall, and holds it until it hangs still. She does not let go.

Beside you she shells peas into a bowl. Her thumbnail splits a pod. Tick. Tick.


Then nothing.

Her hands rest in the bowl. Her head tips back against the chair. She is asleep too.

A blade eases past the light and stops there, half in it. The stripes come to rest.

The sheet over you rises, and falls. A while later it rises again."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
