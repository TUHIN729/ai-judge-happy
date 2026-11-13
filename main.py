#!/usr/bin/env python3
# ai-happy-01 entry: "Make the AI judge happy".
#
# The image is entry.png beside this file: a chubby red panda in a tiny
# knitted red sweater, paws up in delight, riding a wooden sled down a
# snowy hill at golden hour. One big central subject, warm light, a
# specific joyful moment of its own — not a stock smiley or a generic
# sunny scene — so it lands at a glance and still reads at ~300px wide.
#
# The program just copies those exact bytes to the output directory as
# entry.png. Standard library only, no network, no model calls, fully
# deterministic: two runs produce byte-identical output.
#
# The file is JPEG bytes (the gate tells PNG apart from JPEG by the
# first bytes; the name stays entry.png either way), 1024x1024,
# 267,936 bytes — inside the 1 MiB / 1024x1024 gate limits.

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard against a partial write: the judge sees exactly these bytes.
    if os.path.getsize(src) != os.path.getsize(dst):
        raise RuntimeError("entry.png copy is incomplete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
